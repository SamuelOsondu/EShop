from django.shortcuts import render

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
    return render(request, "shop/signup.html")
