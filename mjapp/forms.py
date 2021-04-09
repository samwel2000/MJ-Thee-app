from django import forms

from mjapp.models import Purchases, Services, Bookings, ServiceOffered


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = '__all__'
        widgets = {
            'date':forms.DateInput(
                attrs={
                    'type':'date',
                    'required':True
                }
            ),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        exclude = ['status']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'required': True
                }
            ),
        }

class ServiceOfferedForm(forms.ModelForm):
    class Meta:
        model = ServiceOffered
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'required': True
                }
            ),
        }
