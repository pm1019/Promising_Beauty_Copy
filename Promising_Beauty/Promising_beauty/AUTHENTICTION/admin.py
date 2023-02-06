from django.contrib import admin
from django.contrib.admin.sites import site
from AUTHENTICTION.models import user_registration

admin.site.register(user_registration)
