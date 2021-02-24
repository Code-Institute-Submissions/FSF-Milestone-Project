import uuid

from math import trunc
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField

from userprofiles.models import UserProfile
from items.models import Item



# Create your models here.
class Order(models.Model):
    order_no = models.CharField(max_length=32, editable=False)
    user = models.ForeignKey('userprofiles.UserProfile',
                             on_delete=models.SET_NULL,
                             null=True, related_name='orders')
    full_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=30, blank=False)
    phone = models.CharField(max_length=30, blank=True)
    country = CountryField(blank_label="Choose Country *", blank=True)
    county = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=False)
    postcode = models.CharField(max_length=30, blank=False)
    address_line1 = models.CharField(max_length=30, blank=False)
    address_line2 = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_total = models.DecimalField(max_digits=10,
                                         decimal_places=2, null=False,
                                         default=0)
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, null=False,
                                      default=0)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254,
                                  null=False, blank=False, default='')

    def _generate_order_no(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = self.order_items.aggregate(Sum('order_item_total'))['order_item_total__sum'] or 0
        item_count = self.order_items.count()
        delivery_cost = trunc((6+(6*(item_count))**.5)*100)
        self.delivery_total = Decimal(delivery_cost)/100
        self.grand_total = self.order_total + self.delivery_total
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_no:
            self.order_no = self._generate_order_no()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_no


class OrderItem(models.Model):
    order = models.ForeignKey('Order',
                              on_delete=models.CASCADE,
                              related_name='order_items')
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    order_item_total = models.DecimalField(max_digits=10, decimal_places=2,
                                           null=False, blank=False,
                                           editable=False)

    def save(self, *args, **kwargs):
        if self.item.sale_price:
            self.order_item_total = self.item.sale_price * self.quantity
        else:
            self.order_item_total = self.item.base_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Item {self.item.name} on order {self.order.order_no}'
