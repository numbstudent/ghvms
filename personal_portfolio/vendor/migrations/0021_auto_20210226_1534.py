# Generated by Django 3.1.6 on 2021-02-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0020_auto_20210226_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterdokumen',
            name='label',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='masterkbli',
            name='judul',
            field=models.CharField(max_length=100),
        ),
    ]
