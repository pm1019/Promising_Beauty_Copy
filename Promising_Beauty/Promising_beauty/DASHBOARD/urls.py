from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('dashboard',views.DASHBOARD,name="dash")
]