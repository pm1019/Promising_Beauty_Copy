from django.db import models
from DASHBOARD.models import Customer_details
from ORDERS.models import details
from PRODUCT.models import P_Details
# Create your models here.
class Pay_details(models.Model):
    pay_id=models.IntegerField(primary_key=True)
    cust_id=models.ForeignKey('DASHBOARD.Customer_details',on_delete=models.CASCADE)
    o_id=models.ForeignKey('ORDERS.details',on_delete=models.CASCADE)
    p_id=models.ForeignKey('PRODUCT.P_Details',on_delete=models.CASCADE)
    pay_type=models.CharField(max_length=100)
    pay_upiId=models.CharField(max_length=100)
    pay_NameOnCard=models.CharField(max_length=100)
    pay_CardNum=models.IntegerField()