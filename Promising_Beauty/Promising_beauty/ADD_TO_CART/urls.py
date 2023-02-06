from django.urls import path
from . import views

urlpatterns = [
    path('Addtocart',views.cart,name='CART')
]
