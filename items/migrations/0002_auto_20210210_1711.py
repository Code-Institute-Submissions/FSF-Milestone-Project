# Generated by Django 3.1.5 on 2021-02-10 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='averageRating',
            new_name='average_rating',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='imageUrl',
            new_name='image_URL',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='isAuction',
            new_name='is_auction',
        ),
        migrations.RemoveField(
            model_name='item',
            name='currentPrice',
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
                ('last_bidder', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
