"""allinone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.urls import path
from . import views
from relax_n_shop.views import ProductListView, ProductDetailView
from cart.views import cart_home, cart_update, checkout_home,checkout_done_view
from addresses.views import checkout_address_create_view,checkout_address_reuse_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('cart/', cart_home, name="cart"),
    path('checkout/success/', checkout_done_view, name="success"),
    path('update/', cart_update, name="update"),
    path('checkout/address/create/', checkout_address_create_view, name="checkout_address_create"),
    path('checkout/address/reuse/', checkout_address_reuse_view, name="checkout_address_reuse"),
    path('contact/', views.contact,name="contact"),
    path('login/',views.login_page,name="login"),
    path('register/',views.register_page,name="register"),
    path('products/',ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>',ProductDetailView.as_view(), name='product-detail'),
    path('checkout/',checkout_home,name="checkout"),
    path("logout/", views.logout_x, name="logout"),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
