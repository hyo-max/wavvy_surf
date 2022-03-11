from django import forms
from oscar.apps.address.models import Country
from oscar.apps.checkout import forms as checkout_forms


class ShippingAddressForm(checkout_forms.ShippingAddressForm):

    def __init__(self, *args, **kwargs):
        super(ShippingAddressForm, self).__init__(*args, **kwargs)

    def set_country_and_region_code(self):
        self.country = Country.objects.get(iso_3166_1_a2='KR')
        self.region_code = self.country.iso_3166_1_a2

    class Meta(checkout_forms.ShippingAddressForm.Meta):
        fields = ['first_name', 'last_name', 'postcode', 'line1', 'line2', 'phone_number', 'notes', 'country']
        