from copy import deepcopy

from django import forms
from django.db.models import QuerySet
from django.forms import HiddenInput
from django.http import JsonResponse
from django.shortcuts import render
from oscar.apps.address.models import Country
from oscar.apps.basket.models import Basket
from oscar.apps.checkout.views import PaymentDetailsView as BasePaymentDetailsView
from oscar.apps.order.models import ShippingAddress, Order
from oscar.apps.partner.strategy import Selector
from oscar.apps.payment.models import SourceType, Source
from oscar.core.prices import Price

from accounts.models import User
from iamport.models import Payment
from shop.checkout.consts import PaymentEvents


def get_product_name(lines: QuerySet):
    total = len(lines)
    return f'{lines[0].product.title} 외 {total} 건'


def get_total_amount(basket: Basket):
    strategy = Selector().strategy()
    basket.strategy = strategy
    return int(basket.total_incl_tax)


class CheckoutForm(forms.Form):
    merchant_uid = forms.CharField(widget=HiddenInput())
    name = forms.CharField(widget=HiddenInput())
    amount = forms.CharField(widget=HiddenInput())
    buyer_email = forms.EmailField(widget=HiddenInput())
    buyer_name = forms.CharField(widget=HiddenInput())
    buyer_addr = forms.CharField(widget=HiddenInput())
    buyer_tel = forms.CharField(widget=HiddenInput())
    buyer_postcode = forms.CharField(widget=HiddenInput())


class PaymentDetailsView(BasePaymentDetailsView):

    def __init__(self, **kwargs):
        super(PaymentDetailsView, self).__init__(**kwargs)
        self._pg_provider = None
        self._payment_result = None
        self._country = Country.objects.get(iso_3166_1_a2='KR')

    def get_context_data(self, **kwargs):
        context = super(PaymentDetailsView, self).get_context_data(**kwargs)
        user: User = context['user']
        basket: Basket = context['basket']
        shipping_address: ShippingAddress = context['shipping_address']
        cart_data = {
            'merchant_uid': self.generate_order_number(basket),
            'name': get_product_name(basket.all_lines()),
            'amount': get_total_amount(basket),
            'buyer_email': user.email,
            'buyer_name': user.username,
            'buyer_addr': shipping_address.summary,
            'buyer_tel': shipping_address.phone_number,
            'buyer_postcode': shipping_address.postcode,
        }
        context['form'] = CheckoutForm(initial=cart_data)
        return context

    def _pre_process_payment(self, request):
        self.preview = True
        post_data = deepcopy(request.POST.dict())
        post_data.pop('action')
        self._payment_result = post_data

        self.checkout_session._set('shipping', 'country', self._country)

    def post(self, request, *args, **kwargs):
        self._pre_process_payment(request)
        response = super(PaymentDetailsView, self).post(request, *args, **kwargs)
        data = {'url': response.url}
        return JsonResponse(data)

    def handle_order_placement(self, order_number, user, basket,
                               shipping_address, shipping_method,
                               shipping_charge, billing_address, order_total,
                               surcharges=None, **kwargs):
        order_placement = super(PaymentDetailsView, self).handle_order_placement(
            order_number, user, basket,
            shipping_address, shipping_method,
            shipping_charge, billing_address, order_total,
            surcharges, **kwargs
        )
        order = Order.objects.get(number=self._payment_result['merchant_uid'])
        Payment.add_payment(order, self._payment_result)
        return order_placement

    def handle_payment(self, order_number, order_total: Price, **kwargs):
        pg_provider = self._payment_result['pg_provider']
        source_type = SourceType.objects.get(name=pg_provider)
        source = Source(
            amount_allocated=order_total.incl_tax,
            currency=order_total.currency,
            source_type=source_type,
        )
        self.add_payment_source(source)
        self.add_payment_event(PaymentEvents.paid, order_total.incl_tax)