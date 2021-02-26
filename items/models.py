from django.db import models


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
    image = models.ImageField(upload_to='image_files/', blank=True)

    def __str__(self):
        return self.name

    def update_sale_price(self, discount, isCreated):
        if isCreated is True:
            self.sale_price = round(self.base_price*(100 - discount)/100, 2)
            print(self.sale_price)
        else:
            self.sale_price = None
        self.save()

    def update_score(self, score):
        self.average_rating = score
        self.save()

    def __delete__(self, *args, **kwargs):
        self.image.delete()
        super(Item, self).delete(*args, **kwargs)


# sale model #
class Sale(models.Model):
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 null=True, related_name='sale')
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=0,
                                          blank=False, null=False)

    def save(self, *args, **kwargs):
        items = self.category.items.all()
        discount = self.discount_amount
        for item in items:
            item.update_sale_price(discount, True)
        super(Sale, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        items = self.category.items.all()
        for item in items:
            item.update_sale_price(0, False)
        super(Sale, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name
