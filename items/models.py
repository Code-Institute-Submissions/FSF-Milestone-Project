from django.db import models


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
    isAuction = models.BooleanField(default=False)
    currentPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    averageRating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    # will need a recalc function
    imageUrl = models.URLField(max_length=1024, blank=True)
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
