from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('myorder',views.orders,name="order")
]