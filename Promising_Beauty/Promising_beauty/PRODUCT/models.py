from django.db import models
from DASHBOARD.models import Customer_details



# Create your models here.
class Cat(models.Model):
    cat_id=models.IntegerField(primary_key=True)
    cat_name=models.CharField(max_length=50)

class SubCat(models.Model):
    subcat_id=models.IntegerField(primary_key=True)
    cat_id=models.ForeignKey('Cat',default=0,on_delete=models.SET_DEFAULT)
    subcat_name=models.CharField(max_length=50)

class P_Details(models.Model):
    product_id=models.IntegerField(primary_key=True)
    subcat_id=models.ForeignKey('SubCat',default=0,on_delete=models.SET_DEFAULT)
    p_name=models.CharField(max_length=50)
    p_price=models.IntegerField()
    p_label=models.CharField(max_length=20,default="NEW")
    p_qty=models.IntegerField()
    p_type=models.CharField(max_length=30)
    p_fabric=models.CharField(max_length=30)
    p_size=models.CharField(max_length=30)
    p_img=models.ImageField(upload_to='Products')
    p_desc=models.CharField(max_length=100)
    p_color=models.CharField(max_length=50)

class Add_to_cart(models.Model):
    cart_id=models.IntegerField(primary_key=True)
    cust_id=models.ForeignKey('DASHBOARD.Customer_details',default=0,on_delete=models.SET_DEFAULT )
    p_id=models.ForeignKey('P_Details',default=0,on_delete=models.SET_DEFAULT )
    cart_qty=models.IntegerField(default=1)    