from django.contrib import admin
from .models import Brand, Product, Customer, Order, CustomerPANDetails

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(CustomerPANDetails)