from django.shortcuts import render


# Create your views here.
def ADD_TO_CART(request):
    return render(request,'shop-cart.html')
