from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from shop.forms import SignUpForm
from shop.models import Customer


# Create your views here.


def home(request):
    return render(request, "shop/index.html")


def cart(request):
    return render(request, "shop/cart.html")


def checkout(request):
    return render(request, "shop/checkout.html")


def detail(request):
    return render(request, "shop/detail.html")


def shop(request):
    return render(request, "shop/shop.html")


def test(request):
    return render(request, "shop/test.html")


def login(request):

    return render(request, "shop/login.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'shop/signup.html', {'form': form})

    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         customer = Customer.objects.create(user=user, shipping_address=request.POST['shipping_address'],
    #                                            billing_address=request.POST['billing_address'],
    #                                            phone_number=request.POST['phone_number'])
    #         return redirect('home')
    #     else:
    #         form = UserCreationForm()
    #
    #     return render(request, "shop/signup.html", {'form': form})
