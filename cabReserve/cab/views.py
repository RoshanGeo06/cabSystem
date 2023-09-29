from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, TravelForm, VehicleForm, PaymentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import VehicleInfo, TravelInfo, Vehicle, Payment


def home(request):
    return render(request, 'cab/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'cab/register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'cab/profile.html')

def location(request):
    if request.POST:
        form = TravelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(vehicle)
    return render(request, 'cab/location.html', {'form': TravelForm})


def payment(request):
    if request.POST:
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, f'BOOKED uccessfully')
        return redirect(home)
    return render(request, 'cab/payment.html', {'form': PaymentForm})

def receipt(request):
    all_member1 = TravelInfo.objects.all
    return render(request, 'cab/receipt.html', {'all': all_member1})


def vehicle(request):
    all_member = VehicleInfo.objects.all
    if request.POST:
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(payment)
    return render(request, 'cab/vehicle.html', {'form': VehicleForm, 'all': all_member})


def discover(request):
    return render(request, 'cab/discover.html')


