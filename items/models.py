from django.db import models

from decimal import Decimal

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
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL, null=True,
                                 related_name="items")
    description = models.TextField(blank=False)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    average_rating = models.DecimalField(max_digits=2,
                                         decimal_places=1, null=True,
                                         blank=True)
    sale_price = models.DecimalField(max_digits=10,
                                     decimal_places=2, null=True,
                                     blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def update_sale_price(self, discount, isCreated):
        decimal_corrector = Decimal('0.01')
        if isCreated == True:
            self.sale_price = Decimal(self.base_price*(100 - discount)/100).quantize(decimal_corrector)
        else:
            self.sale_price = None
        self.save()


# sale model #
class Sale(models.Model):
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 null=True, related_name='sale')
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=0,
                                          blank=False, null=False)

    def save(self, *args, **kwargs):
        items = self.category.items.all()
        for item in items:
            item.update_sale_price(self.discount_amount, True)
        super(Sale, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        items = self.category.items.all()
        for item in items:
            item.update_sale_price('', False)
        super(Sale, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name
