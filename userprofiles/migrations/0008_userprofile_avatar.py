# Generated by Django 3.1.5 on 2021-02-25 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0007_userprofile_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='', verbose_name='User Avatar'),
        ),
    ]
