from django.contrib import admin

from .models import Company,Product,Purchase

admin.site.register(Company)
admin.site.register(Product)

admin.site.register(Purchase)
