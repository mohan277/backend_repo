from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    brand_score = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    average_rating = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    email_address = models.EmailField(max_length=100)
    products = models.ManyToManyField('Product', through='Order')
    
class CustomerPANDetails(models.Model):
    pan_number = models.IntegerField()
    name_as_per_pan = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    check_if_pan_details_verified = models.BooleanField()
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    
    
class Order(models.Model):
    total_order_value = models.IntegerField()
    estimated_delivery_date = models.DateField()
    purchase_date = models.DateField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)