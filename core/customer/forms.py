from django import forms
from django.contrib.auth.models import User
from core.models import Customer,Job



class BasicUserForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ('first_name','last_name')


class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('avatar',)

class JobCreateStep1Form(forms.ModelForm):
  class Meta:
    model = Job
    fields = ('name', 'description', 'category', 'size', 'quantity', 'photo')


class JobCreateStep2Form(forms.ModelForm):
    pickup_address=forms.CharField(required=True,label ='Адрес получения посылки',help_text="Адрес получения посылки")
    pickup_name = forms.CharField(required=True,label ='Дополнительные данные',help_text="Дополнительные данные")
    pickup_phone = forms.CharField(required=True,label ='Номер для связи',help_text="Номер для связи")

    class Meta:
        model = Job
        fields = ('pickup_address', 'pickup_lat', 'pickup_lng', 'pickup_name', 'pickup_phone')



class JobCreateStep3Form(forms.ModelForm):
  delivery_address = forms.CharField(required=True,label ='Адрес доставки посылки',help_text="Адрес доставки посылки")
  delivery_name = forms.CharField(required=True,label ='Номер для связи',help_text="Номер для связи",)
  delivery_phone = forms.CharField(required=True,label ='Номер для связи',help_text="Номер для связи",)

  class Meta:
    model = Job
    fields = ('delivery_address', 'delivery_lat', 'delivery_lng', 'delivery_name', 'delivery_phone')