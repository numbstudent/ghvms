# Generated by Django 3.1.6 on 2021-03-10 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0042_auto_20210310_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorperorangan',
            name='kota_perorangan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kota_perorangan', to='vendor.masterkota'),
        ),
    ]
