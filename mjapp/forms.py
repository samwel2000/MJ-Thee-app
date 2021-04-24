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
    service = forms.ModelMultipleChoiceField(
        queryset=Services.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = ServiceOffered
        fields = ['name','service','amount','date','payment']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'required': True
                }
            ),
        }
