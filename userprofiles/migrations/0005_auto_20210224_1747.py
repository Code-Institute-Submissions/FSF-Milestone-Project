# Generated by Django 3.1.5 on 2021-02-24 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0004_auto_20210224_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address1',
            new_name='address_line1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='address2',
            new_name='address_line2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone_number',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='town_city',
            new_name='phone',
        ),
    ]
