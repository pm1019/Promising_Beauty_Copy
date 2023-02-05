from django.shortcuts import render

# Create your views here.
def addtocart(request):
    return render(request,'shop-cart.html')
