from django import forms


class SubscriptionForm(forms.Form):
  name = forms.CharField(label='Nome:')
  email = forms.EmailField(label='Email:')
  cpf = forms.CharField(label='CPF:')
  phone = forms.CharField(label='Telefone:')