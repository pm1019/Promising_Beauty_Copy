from django.db import models
from DASHBOARD.models import Customer_details
from PRODUCT.models import P_Details

# Create your models here.
class Add_to_cart(models.Model):
    cart_id=models.IntegerField(primary_key=True)
    cust_id=models.ForeignKey('DASHBOARD.Customer_details',default=0,on_delete=models.SET_DEFAULT )
    p_id=models.ForeignKey('PRODUCT.P_Details',default=0,on_delete=models.SET_DEFAULT )
   