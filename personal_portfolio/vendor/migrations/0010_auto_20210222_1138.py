# Generated by Django 3.1.6 on 2021-02-22 04:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0009_auto_20210219_1703'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DokumenVendor',
            new_name='DokumenVendorPerusahaan',
        ),
    ]