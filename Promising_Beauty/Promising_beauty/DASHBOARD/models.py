from django.db import models

# Create your models here.
class Customer_details(models.Model):
    cust_id=models.IntegerField(primary_key=True)
    cust_name=models.CharField(max_length=50)
    cust_surname=models.CharField(max_length=50)
    cust_phoneno=models.IntegerField()
    cust_address1=models.CharField(max_length=150)
    cust_address2=models.CharField(max_length=150)
    cust_postcode=models.IntegerField()
    cust_state=models.CharField(max_length=50)
    cust_area=models.CharField(max_length=50)
    cust_emailid=models.EmailField(max_length=50)
    cust_country=models.CharField(max_length=50)
    cust_state=models.CharField(max_length=20)

class Delivery_details(models.Model):
    del_id=models.IntegerField(primary_key=True)
    del_name=models.CharField(max_length=50)
    del_surname=models.CharField(max_length=50)
    del_phoneno=models.IntegerField()
    del_address1=models.CharField(max_length=150)
    del_address2=models.CharField(max_length=150)
    del_postcode=models.IntegerField()
    del_state=models.CharField(max_length=50)
    del_area=models.CharField(max_length=50)
    del_emailid=models.EmailField(max_length=50)
    del_country=models.CharField(max_length=50)
    del_state=models.CharField(max_length=20)
    del_adharno=models.IntegerField()