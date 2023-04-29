from django.conf import settings
from django.conf.urls.static import static
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
    path('logout/', views.logout_request, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('add_product/', views.add_product, name="add_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

