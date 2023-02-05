from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('cart_page',views.ADD_TO_CART,name="Addtocart")
]