from django.db import models


# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=32, editable=False)
    user = models.ForeignKey('UserProfile', on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    county = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    postcode = models.CharField(max_length=30, blank=True)
    address_line1 = models.CharField(max_length=30, blank=False)
    address_line2 = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)


class OrderItem(models.Model):
    order = models.CharField(max_length=30, blank=True)
    item = models.CharField(max_length=30, blank=True)
    quantity = models.CharField(max_length=30, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
