from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('payment',views.payment,name="pay")
]