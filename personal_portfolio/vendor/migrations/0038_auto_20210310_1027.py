# Generated by Django 3.1.6 on 2021-03-10 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0037_auto_20210310_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorperorangan',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]