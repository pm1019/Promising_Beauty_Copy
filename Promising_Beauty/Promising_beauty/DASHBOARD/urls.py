from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('dash',views.DASHBOARD,name="dash")
]