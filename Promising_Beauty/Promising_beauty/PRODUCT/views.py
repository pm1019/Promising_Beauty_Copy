from django.shortcuts import render
from .models import P_Details

# Create your views here.
def product(request):
    Prods=P_Details.objects.all()
    return render(request,'shop.html',{'Prods':Prods})