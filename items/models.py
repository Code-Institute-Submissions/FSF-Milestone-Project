from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    # more human-readable for site management
    internal_name = models.CharField(max_length=30)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


# item model #
class Item(models.Model):
    # ID is autogen by django, so no need to add it manually.
    name = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    # will need a recalc function
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


# sale model #
class Sale(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    discount_amount = models.IntegerField()

    def __str__(self):
        return self.name
