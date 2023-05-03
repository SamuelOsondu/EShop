import random
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from shop.forms import SignUpForm, ProductForm
from shop.models import Product


# Create your views here.


def home(request):
    products = list(Product.objects.all())
    random_products = random.sample(products, 8)
    return render(request, "shop/index.html", {'logged_in': request.user.is_authenticated, 'products': random_products})


@login_required(login_url='signup')
def cart(request):
    return render(request, "shop/cart.html")


def checkout(request):
    return render(request, "shop/checkout.html")


def detail(request):
    return render(request, "shop/detail.html")


def shop(request):
    products = Product.objects.all()
    return render(request, "shop/shop.html", {"products": products})


def test(request):
    return render(request, "shop/test.html")


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_product')
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
    return redirect('home')


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
