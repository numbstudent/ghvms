# Generated by Django 3.1.6 on 2021-02-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0018_tenagaahliperusahaan'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterDokumen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20, unique=True)),
                ('label', models.CharField(max_length=100)),
            ],
        ),
    ]
