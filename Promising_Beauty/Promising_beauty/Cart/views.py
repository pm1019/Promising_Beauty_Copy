from django.shortcuts import render

# Create your views here.
def shopcart(request):
    return render(request,'shop-cart.html')