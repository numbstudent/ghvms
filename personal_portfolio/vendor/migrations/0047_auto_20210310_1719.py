# Generated by Django 3.1.6 on 2021-03-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0046_auto_20210310_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filevendorperusahaan',
            name='tanggal_berakhir',
            field=models.DateField(blank=True, null=True),
        ),
    ]
