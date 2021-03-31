# Generated by Django 3.1.6 on 2021-02-17 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TipePerusahaan',
            new_name='BentukPerusahaan',
        ),
        migrations.RenameField(
            model_name='vendorperusahaan',
            old_name='tipe_perusahaan',
            new_name='bentuk_perusahaan',
        ),
        migrations.AlterField(
            model_name='vendorgeneral',
            name='disclaimer',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='vendorperusahaan',
            name='grade',
            field=models.CharField(choices=[(1, 'GRADE 1'), (2, 'GRADE 2'), (3, 'GRADE 3'), (4, 'GRADE 4'), (5, 'GRADE 5'), (6, 'GRADE 6'), (7, 'GRADE 7')], max_length=2),
        ),
        migrations.AlterField(
            model_name='vendorperusahaan',
            name='kualifikasi',
            field=models.CharField(choices=[(1, 'Tidak Dikualifikasi'), (2, 'Kecil'), (3, 'Besar')], max_length=2),
        ),
        migrations.AlterField(
            model_name='vendorperusahaan',
            name='no_pkp',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='vendorperusahaan',
            name='tipe_pkp',
            field=models.CharField(choices=[(0, 'Non PKP'), (1, 'PKP')], max_length=2),
        ),
    ]
