from django.db import models

# Create your models here.
class Wishlist(models.Model):
    wishlist_id=models.IntegerField(primary_key=True)
    cust_id=models.ForeignKey('Customer_details',default=0,on_delete=models.SET_DEFAULT )
    p_id=models.ForeignKey('P_Details',default=0,on_delete=models.SET_DEFAULT )
    