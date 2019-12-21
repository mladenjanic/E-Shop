from django import forms
from django_countries.fields import CountryField


PAYMENT_CHOICES = (
  ('S', 'Stripe'),
  ('P', 'PayPal')
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
      'placeholder': 'Main St',
      'class': 'form-control'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
      'placeholder': 'Apartment or Suite',
      'class': 'form-control'
    }))
    country = CountryField(blank_label='(select country)').formfield(widget=forms.Select(attrs={
      'class':'custom-select d-block w-100'
    }))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={
      'class': 'form-control'
    }))
    same_billing_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(attrs={
      'class': 'custom-control-input' }), choices=PAYMENT_CHOICES)

