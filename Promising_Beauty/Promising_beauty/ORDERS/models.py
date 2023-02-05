from django.db import models
from DASHBOARD.models import Customer_details
from PRODUCT.models import P_Details
# Create your models here.
class order(models.Model):
    o_id=models.IntegerField(primary_key=True)
    cusT_id=models.ForeignKey('DASHBOARD.Customer_details',on_delete=models.CASCADE)
    p_id=models.ForeignKey('PRODUCT.P_Details',on_delete=models.CASCADE)
    o_qty=models.IntegerField()
    o_netamount=models.IntegerField()
    o_date=models.DateField()
    o_details=models.CharField(max_length=100)
    o_status=models.BooleanField()