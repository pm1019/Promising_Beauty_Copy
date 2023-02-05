from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('',views.home,name="home")
]