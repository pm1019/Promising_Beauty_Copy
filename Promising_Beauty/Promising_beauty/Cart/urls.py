from django.urls import path
from . import views

urlpatterns = [
    path('cart',views.shopcart,name='home')
]
