from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from shop.forms import SignUpForm, LoginForm, ProductForm
from shop.models import Customer


# Create your views here.


def home(request):
    return render(request, "shop/index.html", {'logged_in': request.user.is_authenticated})


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


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = ProductForm()

    return render(request, "shop/add_product.html", {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request, "shop/index.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return HttpResponseRedirect('/shop')
            else:
                messages.error(request, form.errors)
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()

    return render(request, "shop/login.html", {'form': form})


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
