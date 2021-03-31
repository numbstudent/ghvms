# Generated by Django 3.1.6 on 2021-02-22 09:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import vendor.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0010_auto_20210222_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileVendorPerusahaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_file', models.FileField(upload_to=vendor.models.FileVendorPerusahaan.get_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('jenis_file', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
