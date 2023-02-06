from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('register',views.register,name="register")

]