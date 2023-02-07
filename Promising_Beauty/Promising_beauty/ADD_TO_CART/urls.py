from django.urls import path
from . import views

urlpatterns = [
    path('Addtocart',views.add_to_cart,name='CART'),
    path('add',views.show_cart,name='add')
]
