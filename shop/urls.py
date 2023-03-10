from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('detail/', views.detail, name="detail"),
    path('shop/', views.shop, name="shop"),
    path('text/', views.test, name="test"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
]

