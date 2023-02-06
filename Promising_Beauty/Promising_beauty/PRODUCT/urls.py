from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('product',views.product,name="shop"),
]