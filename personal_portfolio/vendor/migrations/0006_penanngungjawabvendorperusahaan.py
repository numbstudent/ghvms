# Generated by Django 3.1.6 on 2021-02-19 07:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0005_auto_20210219_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='PenanngungjawabVendorPerusahaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pemilik', models.CharField(max_length=100)),
                ('email_pemilik', models.EmailField(max_length=30)),
                ('hp_pemilik', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Nomor telepon / fax harus mengikuti format: '+999999999'.", regex='^\\+?1?\\d{9,15}$')])),
                ('nama_pimpinan', models.CharField(max_length=100)),
                ('email_pimpinan', models.EmailField(max_length=30)),
                ('hp_pimpinan', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Nomor telepon / fax harus mengikuti format: '+999999999'.", regex='^\\+?1?\\d{9,15}$')])),
                ('ktp_pimpinan', models.CharField(max_length=16)),
                ('nama_marketing', models.CharField(max_length=100)),
                ('email_marketing', models.EmailField(max_length=30)),
                ('hp_marketing', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Nomor telepon / fax harus mengikuti format: '+999999999'.", regex='^\\+?1?\\d{9,15}$')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
