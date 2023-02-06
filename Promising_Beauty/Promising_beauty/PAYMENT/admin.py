from django.contrib import admin
from django.contrib.admin.sites import site
from PAYMENT.models import Pay_details
from DASHBOARD.models import Customer_details
from ORDERS.models import details
from PRODUCT.models import P_Details


admin.site.register(Pay_details)