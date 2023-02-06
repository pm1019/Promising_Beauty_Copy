from django.contrib import admin
from django.contrib.admin.sites import site
from PRODUCT.models import Cat,SubCat,P_Details

admin.site.register(Cat)
admin.site.register(SubCat)
admin.site.register(P_Details)
