from django.forms import ModelForm
from .models import Register

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['company_name', 'owner', 'CNPJ', 'email', 'phone', 'business', 'country', 'state', 'city', 'neighborhood', 'street', 'number', 'complement']
