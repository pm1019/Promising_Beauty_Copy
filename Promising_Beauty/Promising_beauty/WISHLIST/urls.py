from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('wishlist',views.wishlist,name="wish")
]