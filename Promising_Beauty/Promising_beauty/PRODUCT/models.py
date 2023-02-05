from django.db import models

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
    p_qty=models.IntegerField()
    p_type=models.CharField(max_length=30)
    p_fabric=models.CharField(max_length=30)
    p_size=models.CharField(max_length=30)
    p_img=models.CharField(max_length=50)
    p_desc=models.CharField(max_length=100)
    p_color=models.CharField(max_length=50)
