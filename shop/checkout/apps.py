import oscar.apps.checkout.apps as apps
from django.urls import path


class CheckoutConfig(apps.CheckoutConfig):
    name = 'shop.checkout'

    def get_urls(self):
        from shop.checkout.views import PaymentDetailsView

        urls = super().get_urls()
        urls += [
            path('payment-details/', PaymentDetailsView.as_view(), name='payment-details')
        ]

        return self.post_process_urls(urls)
