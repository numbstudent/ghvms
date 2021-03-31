# Generated by Django 3.1.6 on 2021-03-09 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0031_auto_20210308_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterdokumen',
            name='is_required',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alamatvendorperusahaan',
            name='alamat_gudang',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='alamatvendorperusahaan',
            name='kode_pos_gudang',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='alamatvendorperusahaan',
            name='kota_gudang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kota_gudang', to='vendor.masterkota'),
        ),
        migrations.AlterField(
            model_name='vendorperorangan',
            name='nomor_fax',
            field=models.CharField(max_length=50, null=True),
        ),
    ]