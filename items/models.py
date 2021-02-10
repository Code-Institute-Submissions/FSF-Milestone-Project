from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    # more human-readable for site management
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


# item model #
class Item(models.Model):
    # ID is autogen by django, so no need to add it manually.
    name = models.CharField(max_length=30, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_auction = models.BooleanField(default=False)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    # will need a recalc function
    image_URL = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Auction(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    last_bidder = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.item.name


# sale model #
class Sale(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    discount_amount = models.IntegerField()

    def __str__(self):
        return self.name
