from django.shortcuts import render,redirect
from .models import P_Details,Add_to_cart,Customer_details
from django.contrib.auth.models import User

# Create your views here.
def product(request):
    Prods=P_Details.objects.all()
    return render(request,'shop.html',{'Prods':Prods})

def prods_detail(request,id):
    detail=P_Details.objects.get(p_id=id)
    return render(request,'product-details.html',{'data':detail})

def show_cart(request):
    user=request.user
    cart=Add_to_cart.objects.filter(cust_id=user)
    return render(request,'shop-cart.html',{'carts':cart})

def add_to_cart(request):
    user=request.Customer_details
    product_id=request.GET.get('id')
    product=P_Details.objects.get(p_id=product_id)
    Add_to_cart(cust_id=user,p_id=product).save()
    return redirect("/cart")
