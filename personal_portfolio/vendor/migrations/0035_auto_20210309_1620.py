# Generated by Django 3.1.6 on 2021-03-09 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0034_auto_20210309_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorgeneral',
            name='ada_pengalaman',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='alamatvendorperusahaan',
            name='alamat_gudang',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alamatvendorperusahaan',
            name='kode_pos_gudang',
            field=models.CharField(blank=True, default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alamatvendorperusahaan',
            name='kota_gudang',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='kota_gudang', to='vendor.masterkota'),
            preserve_default=False,
        ),
    ]
