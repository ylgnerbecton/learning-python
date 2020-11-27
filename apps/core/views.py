from django.shortcuts import render
from .models import Register
from .form import RegisterForm

def Registration(request):
    data = {}
    data['Registration'] = Register.objects.all()
    return render(request, 'core/register.html', data)

def New_Register(request):
    data = {}
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return Registration(request)
    data['form'] = form
    return render(request, 'core/form.html', data)

# Create your views here.
