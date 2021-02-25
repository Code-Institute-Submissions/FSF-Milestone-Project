from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from django_countries.fields import CountryField

from decimal import Decimal


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=24, default='Anonymous User')
    avatar = models.ImageField(upload_to='user_avatars/', verbose_name="User Avatar", null=True, blank=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    country = CountryField(blank_label="Choose Country *", blank=True, null=True)
    county = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    address_line1 = models.CharField(max_length=80, blank=True, null=True)
    address_line2 = models.CharField(max_length=80, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    #  avatar = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    posting_user = models.ForeignKey('userprofiles.UserProfile',
                                     on_delete=models.CASCADE,
                                     related_name='reviews')
    item = models.ForeignKey('items.Item',
                             on_delete=models.CASCADE,
                             related_name='reviews')
    content = models.TextField()
    score = models.DecimalField(max_digits=2,
                                decimal_places=1, null=True,
                                blank=True, default=0)

    def save(self, *args, **kwargs):
        target_item = self.item
        existing_reviews = target_item.reviews.all()
        other_count = existing_reviews.count()
        for review in existing_reviews:
            if review.id is self.id:
                other_count -= 1
        if other_count >= 0:

            sum_score = self.score

            for review in existing_reviews:
                if review.id is not self.id:
                    sum_score += review.score

            averaged_score = round(sum_score/(other_count+1), 1)
            target_item.update_score(averaged_score)

        else:
            target_item.update_score(self.score)

        super(Review, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        target_item = self.item
        existing_reviews = target_item.reviews.all()
        other_count = existing_reviews.count() - 1
        print(other_count)
        if other_count > 0:

            sum_score = 0

            for review in existing_reviews:
                if review.id is not self.id:
                    sum_score += review.score

            averaged_score = round(sum_score/(other_count), 1)
            target_item.update_score(averaged_score)
        else:
            target_item.update_score(None)
        super(Review, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.posting_user.username}'s review of {self.item.name}"


# user profile signal, no need for a file if it's just the one.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created is True:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
