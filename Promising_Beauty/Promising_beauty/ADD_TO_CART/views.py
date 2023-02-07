from django.shortcuts import render,redirect
from .models import Add_to_cart
from PRODUCT.models import P_Details
from django.contrib.auth.models import User

# Create your views here.
def show_cart(request):
    user=request.user
    cart=Add_to_cart.objects.filter(cust_id=user)
    return render(request,'shop-cart.html',{'carts':cart})

def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('id')
    product=P_Details.objects.get(p_id=product_id)
    Add_to_cart(cust_id=user,p_id=product).save()
    return redirect("/cart")
