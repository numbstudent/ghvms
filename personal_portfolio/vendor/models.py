import os
from django.db.models import F
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, FileExtensionValidator
models.CharField.register_lookup(models.functions.Length, 'length')

# Create your models here.

#master data


class MasterProvinsi(models.Model):
    provinsi = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.provinsi)


class MasterKota(models.Model):
    kota = models.CharField(max_length=50)
    provinsi = models.ForeignKey(
        MasterProvinsi, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.kota)


class MasterDokumen(models.Model):
    nama = models.CharField(max_length=20, unique=True)
    label = models.CharField(max_length=250)
    ada_berakhir = models.BooleanField()
    is_required = models.BooleanField()
    for_perusahaan = models.BooleanField()
    for_perorangan = models.BooleanField()


class MasterKbli(models.Model):
    kbli = models.CharField(max_length=10)
    judul = models.CharField(max_length=100)


class MasterBidangUsaha(models.Model):
    nama = models.CharField(max_length=150)

    def __str__(self):
        return self.nama

#non-master data


class BentukPerusahaan(models.Model):
    nama = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.nama)


class VendorGeneral(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    PERUSAHAAN = 'PE'
    PERORANGAN = 'PO'
    INTERNASIONAL = 'IN'
    TIPE_VENDOR_CHOICES = [
        (PERUSAHAAN, 'Vendor lokal - Perusahaan'),
        (PERORANGAN, 'Vendor lokal - Perorangan'),
        (INTERNASIONAL, 'Vendor internasional'),
    ]
    tipe_perusahaan = models.CharField(
        max_length=2,
        choices=TIPE_VENDOR_CHOICES,
        default=PERUSAHAAN,
    )
    disclaimer = models.BooleanField()
    ada_pengalaman = models.BooleanField(default=True)
    dalam_verifikasi = models.BooleanField(default=False)
    disetujui = models.BooleanField(default=False)
    tanggal_persetujuan= models.DateField(null=True)


class VendorPerusahaan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_pkp = models.CharField(max_length=30, blank=True)

    P0 = 'C0'
    P1 = 'C1'
    KUALIFIKASI_CHOICES = [
        (P0, 'Non PKP'),
        (P1, 'PKP'),
    ]
    tipe_pkp = models.CharField(
        max_length=2,
        choices=KUALIFIKASI_CHOICES,
    )

    C1 = 'C1'
    C2 = 'C2'
    C3 = 'C3'
    KUALIFIKASI_CHOICES = [
        (C1, 'Tidak Dikualifikasi'),
        (C2, 'Kecil'),
        (C3, 'Besar'),
    ]
    kualifikasi = models.CharField(
        max_length=2,
        choices=KUALIFIKASI_CHOICES,
    )

    G1 = 'C1'
    G2 = 'C2'
    G3 = 'C3'
    G4 = 'C4'
    G5 = 'C5'
    G6 = 'C6'
    G7 = 'C7'
    GRADE_CHOICES = [
        (G1, 'GRADE 1'),
        (G2, 'GRADE 2'),
        (G3, 'GRADE 3'),
        (G4, 'GRADE 4'),
        (G5, 'GRADE 5'),
        (G6, 'GRADE 6'),
        (G7, 'GRADE 7'),
    ]
    grade = models.CharField(
        max_length=2,
        choices=GRADE_CHOICES,
        null=True
    )

    nama_perusahaan = models.CharField(max_length=100)
    bentuk_perusahaan = models.ForeignKey(
        BentukPerusahaan, on_delete=models.CASCADE)
    npwp_perusahaan = models.CharField(max_length=100)
    no_akte_perusahaan = models.CharField(max_length=100)
    tanggal_berdiri_perusahaan = models.DateField()
    tanggal_perubahan = models.DateField()
    nama_singkatan = models.CharField(max_length=100)
    website = models.CharField(max_length=30)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Nomor telepon / fax harus mengikuti format: '+999999999'.")
    nomor_telepon = models.CharField(
        validators=[phone_regex], max_length=17)
    nomor_fax = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)


class VendorPerorangan(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Nomor telepon / fax harus mengikuti format: '+999999999'.")
    ############

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_perorangan = models.CharField(max_length=100)
    nama_singkatan = models.CharField(max_length=50)
    alamat_perorangan = models.TextField()
    kota_perorangan = models.ForeignKey(
        MasterKota, on_delete=models.CASCADE, related_name='kota_perorangan')
    kode_pos_perorangan = models.CharField(max_length=5)
    nomor_ktp = models.CharField(max_length=20)
    tanggal_berakhir = models.DateTimeField(blank=True, null=True)
    npwp_perorangan = models.CharField(max_length=50)
    nomor_telepon = models.CharField(
        validators=[phone_regex], max_length=17)
    nomor_fax = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=30)
    nomor_hp = models.CharField(
        validators=[phone_regex], max_length=17)


class AlamatVendorPerusahaan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ############
    alamat_kantor = models.TextField()
    kota_kantor = models.ForeignKey(
        MasterKota, on_delete=models.CASCADE, related_name='kota_kantor')
    kode_pos_kantor = models.CharField(max_length=5)
    ############
    alamat_npwp = models.TextField()
    kota_npwp = models.ForeignKey(
        MasterKota, on_delete=models.CASCADE, related_name='kota_npwp')
    kode_pos_npwp = models.CharField(max_length=5)
    ############
    alamat_gudang = models.TextField(blank=True)
    kota_gudang = models.ForeignKey(
        MasterKota, on_delete=models.CASCADE, related_name='kota_gudang', blank=True)
    kode_pos_gudang = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return '%s' % (self.id)

class PenanngungjawabVendorPerusahaan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Nomor telepon / fax harus mengikuti format: '+999999999'.")
    ############
    nama_pemilik = models.CharField(max_length=100)
    email_pemilik = models.EmailField(max_length=30)
    hp_pemilik = models.CharField(
        validators=[phone_regex], max_length=17)
    ############
    nama_pimpinan = models.CharField(max_length=100)
    email_pimpinan = models.EmailField(max_length=30)
    hp_pimpinan = models.CharField(
        validators=[phone_regex], max_length=17)
    ktp_pimpinan = models.CharField(max_length=16)
    ############
    nama_marketing = models.CharField(max_length=100)
    email_marketing = models.EmailField(max_length=30)
    hp_marketing = models.CharField(
        validators=[phone_regex], max_length=17)

    def __str__(self):
        return '%s' % (self.id)


class DokumenVendorPerusahaan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    akte = models.FileField(upload_to='vendor/akte/')
    tdp = models.FileField(upload_to='vendor/tdp/')
    siup_nib = models.FileField(upload_to='vendor/siup_nib/')
    domisili = models.FileField(upload_to='vendor/domisili/')
    sppkp = models.FileField(upload_to='vendor/sppkp/')
    setor_pajak = models.FileField(upload_to='vendor/setor_pajak/')
    spt_masa = models.FileField(upload_to='vendor/spt_masa/')
    pph = models.FileField(upload_to='vendor/pph/')
    lap_keu = models.FileField(upload_to='vendor/lap_keu/')
    akte_perubahan = models.FileField(upload_to='vendor/akte_perubahan/')
    siujk = models.FileField(upload_to='vendor/siujk/')


class FileVendorPerusahaan(models.Model):
    def get_upload_path(instance, nama_file):
        # return "/vendor/user_" + instance.user.id+ "/" % instance.jenis_file, nama_file)
        return "vendor/"+str(instance.user.id)+"/"+str(instance.jenis_file)+"/"+nama_file

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_file = models.FileField(upload_to=get_upload_path,
                                 validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    # nama_file = models.FileField(upload_to='vendor/plslawork/')

    jenis_file = models.CharField(max_length=50)
    tanggal_berakhir = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BankVendorPerusahaan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    cabang = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    kota = models.CharField(max_length=100)
    negara = models.CharField(max_length=100)
    nomor_rekening = models.CharField(max_length=100)
    nama_nasabah = models.CharField(max_length=100)
    MATA_UANG_CHOICES = [
        ('ADP', 'ADP - Andoran peseta'),
        ('AED', 'AED - United Arab Emirates Dirham'),
        ('AFA', 'AFA - Afghani (Old)'),
        ('AFN', 'AFN - Afghani'),
        ('ALL', 'ALL - Albanian Lek'),
        ('AMD', 'AMD - Armenian Dram'),
        ('ANG', 'ANG - West Indian Guilder'),
        ('AOA', 'AOA - Angolanische Kwanza'),
        ('AON', 'AON - Angolan New Kwanza (Old)'),
        ('AOR', 'AOR - Angolan Kwanza Reajustado (Old)'),
        ('ARS', 'ARS - Argentine Peso'),
        ('ATS', 'ATS - Austrian Schilling'),
        ('AUD', 'AUD - Australian Dollar'),
        ('AWG', 'AWG - Aruban Guilder'),
        ('AZM', 'AZM - Azerbaijan Manat'),
        ('BAM', 'BAM - Bosnia and Herzegovina Convertible Mark'),
        ('BBD', 'BBD - Barbados Dollar'),
        ('BDT', 'BDT - Bangladesh Taka'),
        ('BEF', 'BEF - Belgian Franc'),
        ('BGN', 'BGN - Bulgarian Lev'),
        ('BHD', 'BHD - Bahrain Dinar'),
        ('BIF', 'BIF - Burundi Franc'),
        ('BMD', 'BMD - Bermudan Dollar'),
        ('BND', 'BND - Brunei Dollar'),
        ('BOB', 'BOB - Boliviano'),
        ('BRL', 'BRL - Brazilian Real'),
        ('BSD', 'BSD - Bahaman Dollar'),
        ('BTN', 'BTN - Bhutan Ngultrum'),
        ('BWP', 'BWP - Botswana Pula'),
        ('BYB', 'BYB - Belorussian Ruble (Old)'),
        ('BYR', 'BYR - Belorussian Ruble'),
        ('BZD', 'BZD - Belize Dollar'),
        ('CAD', 'CAD - Canadian Dollar'),
        ('CDF', 'CDF - Congolese Franc'),
        ('CFP', 'CFP - French Franc (Pacific Islands)'),
        ('CHF', 'CHF - Swiss Franc'),
        ('CLP', 'CLP - Chilean Peso'),
        ('CNY', 'CNY - Chinesische Yuan (international)'),
        ('COP', 'COP - Colombian Peso'),
        ('CRC', 'CRC - Costa Rica Colon'),
        ('CSD', 'CSD - Serbian Dinar'),
        ('CUP', 'CUP - Cuban Peso'),
        ('CVE', 'CVE - Cape Verde Escudo'),
        ('CYP', 'CYP - Cyprus Pound'),
        ('CZK', 'CZK - Czech Krona'),
        ('DEM', 'DEM - German Mark'),
        ('DEM3', 'DEM3 - (Internal) German Mark (3 dec.places)'),
        ('DJF', 'DJF - Djibouti Franc'),
        ('DKK', 'DKK - Danish Krone'),
        ('DOP', 'DOP - Dominican Peso'),
        ('DZD', 'DZD - Algerian Dinar'),
        ('ECS', 'ECS - Ecuadorian Sucre (  &gt; USD)'),
        ('EEK', 'EEK - Estonian Krone'),
        ('EGP', 'EGP - Egyptian Pound'),
        ('ERN', 'ERN - Eritrean Nafka'),
        ('ESP', 'ESP - Spanish Peseta'),
        ('ETB', 'ETB - Ethiopian Birr'),
        ('EUR', 'EUR - European Euro'),
        ('FIM', 'FIM - Finnish markka'),
        ('FJD', 'FJD - Fiji Dollar'),
        ('FKP', 'FKP - Falkland Pound'),
        ('FRF', 'FRF - French Franc'),
        ('GEL', 'GEL - Georgian Lari'),
        ('GHC', 'GHC - Ghanian Cedi'),
        ('GIP', 'GIP - Gibraltar Pound'),
        ('GMD', 'GMD - Gambian Dalasi'),
        ('GNF', 'GNF - Guinean Franc'),
        ('GRD', 'GRD - Greek Drachma'),
        ('GTQ', 'GTQ - Guatemalan Quetzal'),
        ('GWP', 'GWP - Guinea Peso'),
        ('GYD', 'GYD - Guyana Dollar'),
        ('HKD', 'HKD - Hong Kong Dollar'),
        ('HNL', 'HNL - Honduran Lempira'),
        ('HRK', 'HRK - Croatian Kuna'),
        ('HTG', 'HTG - Haitian Gourde'),
        ('HUF', 'HUF - Hungarian Forint'),
        ('IDR', 'IDR - Indonesian Rupiah'),
        ('IEP', 'IEP - Irish Punt'),
        ('ILS', 'ILS - Israeli Scheckel'),
        ('INR', 'INR - Indian Rupee'),
        ('IQD', 'IQD - Iraqui Dinar'),
        ('IRR', 'IRR - Iranian Rial'),
        ('ISK', 'ISK - Iceland Krona'),
        ('ITL', 'ITL - Italian Lira'),
        ('JMD', 'JMD - Jamaican Dollar'),
        ('JOD', 'JOD - Jordanian Dinar'),
        ('JPY', 'JPY - Japanese Yen'),
        ('KES', 'KES - Kenyan Shilling'),
        ('KGS', 'KGS - Kyrgyzstan Som'),
        ('KHR', 'KHR - Cambodian Riel'),
        ('KMF', 'KMF - Comoros Franc'),
        ('KPW', 'KPW - North Korean Won'),
        ('KRW', 'KRW - South Korean Won'),
        ('KWD', 'KWD - Kuwaiti Dinar'),
        ('KYD', 'KYD - Cayman Dollar'),
        ('KZT', 'KZT - Kazakstanian Tenge'),
        ('LAK', 'LAK - Laotian Kip'),
        ('LBP', 'LBP - Lebanese Pound'),
        ('LKR', 'LKR - Sri Lankan Rupee'),
        ('LRD', 'LRD - Liberian Dollar'),
        ('LSL', 'LSL - Lesotho Loti'),
        ('LTL', 'LTL - Lithuanian Lita'),
        ('LUF', 'LUF - Luxembourg Franc'),
        ('LVL', 'LVL - Latvian Lat'),
        ('LYD', 'LYD - Libyan Dinar'),
        ('MAD', 'MAD - Moroccan Dirham'),
        ('MDL', 'MDL - Moldavian Leu'),
        ('MGA', 'MGA - Madagascan Ariary (New)'),
        ('MGF', 'MGF - Madagascan Franc (Old'),
        ('MKD', 'MKD - Macedonian Denar'),
        ('MMK', 'MMK - Myanmar Kyat'),
        ('MNT', 'MNT - Mongolian Tugrik'),
        ('MOP', 'MOP - Macao Pataca'),
        ('MRO', 'MRO - Mauritanian Ouguiya'),
        ('MTL', 'MTL - Maltese Lira'),
        ('MUR', 'MUR - Mauritian Rupee'),
        ('MVR', 'MVR - Maldive Rufiyaa'),
        ('MWK', 'MWK - Malawi Kwacha'),
        ('MXN', 'MXN - Mexican Pesos'),
        ('MYR', 'MYR - Malaysian Ringgit'),
        ('MZM', 'MZM - Mozambique Metical'),
        ('NAD', 'NAD - Namibian Dollar'),
        ('NGN', 'NGN - Nigerian Naira'),
        ('NIO', 'NIO - Nicaraguan Cordoba Oro'),
        ('NLG', 'NLG - Dutch Guilder'),
        ('NOK', 'NOK - Norwegian Krone'),
        ('NPR', 'NPR - Nepalese Rupee'),
        ('NZD', 'NZD - New Zealand Dollars'),
        ('NZD5', 'NZD5 - New Zealand Dollars'),
        ('OMR', 'OMR - Omani Rial'),
        ('PAB', 'PAB - Panamanian Balboa'),
        ('PEN', 'PEN - Peruvian New Sol'),
        ('PGK', 'PGK - Papua New Guinea Kina'),
        ('PHP', 'PHP - Philippine Peso'),
        ('PKR', 'PKR - Pakistani Rupee'),
        ('PLN', 'PLN - Polish Zloty (new)'),
        ('PTE', 'PTE - Portuguese Escudo'),
        ('PYG', 'PYG - Paraguayan Guarani'),
        ('QAR', 'QAR - Qatar Rial'),
        ('RMB', 'RMB - Chinesische Renminbi (national)'),
        ('ROL', 'ROL - Romanian Leu'),
        ('RUB', 'RUB - Russian Ruble'),
        ('RWF', 'RWF - Rwandan Franc'),
        ('SAR', 'SAR - Saudi Riyal'),
        ('SBD', 'SBD - Solomon Islands Dollar'),
        ('SCR', 'SCR - Seychelles Rupee'),
        ('SDD', 'SDD - Sudanese Dinar'),
        ('SDP', 'SDP - Sudanese Pound'),
        ('SEK', 'SEK - Swedish Krona'),
        ('SGD', 'SGD - Singapore Dollar'),
        ('SHP', 'SHP - St.Helena Pound'),
        ('SIT', 'SIT - Slovenian Tolar'),
        ('SKK', 'SKK - Slovakian Krona'),
        ('SLL', 'SLL - Sierra Leone Leone'),
        ('SOS', 'SOS - Somalian Shilling'),
        ('SRD', 'SRD - Surinam Dollar'),
        ('SRG', 'SRG - Surinam Guilder (Old)'),
        ('STD', 'STD - Sao Tome / Principe Dobra'),
        ('SVC', 'SVC - El Salvador Colon'),
        ('SYP', 'SYP - Syrian Pound'),
        ('SZL', 'SZL - Swaziland Lilangeni'),
        ('THB', 'THB - Thailand Baht'),
        ('TJR', 'TJR - Tajikistani Ruble (Old)'),
        ('TJS', 'TJS - Tajikistani Somoni'),
        ('TMM', 'TMM - Turkmenistani Manat'),
        ('TND', 'TND - Tunisian Dinar'),
        ('TOP', 'TOP - Tongan Pa\'anga'),
        ('TPE', 'TPE - Timor Escudo'),
        ('TRL', 'TRL - Turkish Lira (Old)'),
        ('TRY', 'TRY - Turkish Lira'),
        ('TTD', 'TTD - Trinidad and Tobago Dollar'),
        ('TWD', 'TWD - New Taiwan Dollar'),
        ('TZS', 'TZS - Tanzanian Shilling'),
        ('UAH', 'UAH - Ukraine Hryvnia'),
        ('UGX', 'UGX - Ugandan Shilling'),
        ('USD', 'USD - United States Dollar'),
        ('USDN', 'USDN - (Internal) United States Dollar (5 Dec.)'),
        ('UYU', 'UYU - Uruguayan Peso (new)'),
        ('UZS', 'UZS - Uzbekistan Som'),
        ('VEB', 'VEB - Venezuelan Bolivar'),
        ('VEF', 'VEF - Venezuelan Bolivar Hard'),
        ('VND', 'VND - Vietnamese Dong'),
        ('VUV', 'VUV - Vanuatu Vatu'),
        ('WST', 'WST - Samoan Tala'),
        ('XAF', 'XAF - Gabon CFA Franc BEAC'),
        ('XCD', 'XCD - East Carribean Dollar'),
        ('XDS', 'XDS - St. Christopher Dollar'),
        ('XEU', 'XEU - European Currency Unit (E.C.U.)'),
        ('XOF', 'XOF - Benin CFA Franc BCEAO'),
        ('XPF', 'XPF - CFP Franc'),
        ('YER', 'YER - Yemeni Ryal'),
        ('YUM', 'YUM - New Yugoslavian Dinar (Old)'),
        ('ZAR', 'ZAR - South African Rand'),
        ('ZMK', 'ZMK - Zambian Kwacha'),
        ('ZRN', 'ZRN - Zaire (Old)'),
        ('ZWD', 'ZWD - Zimbabwean Dollar'),
    ]
    mata_uang = models.CharField(
        max_length=4,
        choices=MATA_UANG_CHOICES,
    )




class PeralatanPerusahaan(models.Model):
    def get_upload_path(instance, dokumen_bukti_kepemilikan):
        return "vendor/"+str(instance.user.id)+"/peralatan/"+dokumen_bukti_kepemilikan
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jenis = models.CharField(max_length=50)
    jumlah = models.SmallIntegerField()
    kapasitas = models.CharField(max_length=50)
    merk = models.CharField(max_length=50)
    tahun_pembuatan = models.SmallIntegerField()

    C1 = 'Baik'
    C2 = 'Cukup'
    C3 = 'Kurang'
    KONDISI_CHOICES = [
        (C1, 'Baik'),
        (C2, 'Cukup'),
        (C3, 'Kurang'),
    ]
    kondisi = models.CharField(
        max_length=6,
        choices=KONDISI_CHOICES,
    )

    lokasi= models.CharField(max_length=150)
    bukti_kepemilikan= models.CharField(max_length=100)
    dokumen_bukti_kepemilikan = models.FileField(upload_to=get_upload_path, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])


class SegmentasiPerusahaan(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    kbli= models.ForeignKey(MasterKbli, on_delete=models.CASCADE)


class TenagaAhliPerusahaan(models.Model):
    def get_upload_path(instance, dokumen):
        # return "/vendor/user_" + instance.user.id+ "/" % instance.jenis_file, nama_file)
        return "vendor/"+str(instance.user.id)+"/tenagaahli/"+dokumen

    user= models.ForeignKey(User, on_delete=models.CASCADE)
    nama_tenaga_ahli= models.CharField(max_length=100)
    tanggal_lahir= models.DateField()
    C1= 'SMA'
    C2= 'Diploma'
    C3= 'Sarjana (S1)'
    C4= 'Magister (S2)'
    C5= 'Doktor (S3)'
    C6= 'Professor'
    PENDIDIKAN_CHOICES= [
        (C1, 'SMA'),
        (C2, 'Diploma'),
        (C3, 'Sarjana (S1)'),
        (C4, 'Magister(S2)'),
        (C5, 'Doktor (S3)'),
        (C6, 'Professor'),
    ]
    pendidikan= models.CharField(
        max_length=15,
        choices=PENDIDIKAN_CHOICES,
    )
    pengalaman= models.SmallIntegerField()
    profesi= models.CharField(max_length=100)
    dokumen= models.FileField(upload_to=get_upload_path,
                               validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
                               

class PengalamanPerusahaan(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    def get_upload_path(instance, p_dokumen):
        return "vendor/"+str(instance.user.id)+"/pengalaman/"+p_dokumen

    p_nama =  models.CharField(max_length=150)
    p_lokasi = models.TextField(max_length=200)
    p_bidang_usaha = models.ForeignKey(
        MasterBidangUsaha, on_delete=models.CASCADE)
    p_mulai_kerjasama = models.DateField()
    p_nilai_kontrak = models.BigIntegerField()
    MATA_UANG_CHOICES = [
        ('ADP', 'ADP - Andoran peseta'),
        ('AED', 'AED - United Arab Emirates Dirham'),
        ('AFA', 'AFA - Afghani (Old)'),
        ('AFN', 'AFN - Afghani'),
        ('ALL', 'ALL - Albanian Lek'),
        ('AMD', 'AMD - Armenian Dram'),
        ('ANG', 'ANG - West Indian Guilder'),
        ('AOA', 'AOA - Angolanische Kwanza'),
        ('AON', 'AON - Angolan New Kwanza (Old)'),
        ('AOR', 'AOR - Angolan Kwanza Reajustado (Old)'),
        ('ARS', 'ARS - Argentine Peso'),
        ('ATS', 'ATS - Austrian Schilling'),
        ('AUD', 'AUD - Australian Dollar'),
        ('AWG', 'AWG - Aruban Guilder'),
        ('AZM', 'AZM - Azerbaijan Manat'),
        ('BAM', 'BAM - Bosnia and Herzegovina Convertible Mark'),
        ('BBD', 'BBD - Barbados Dollar'),
        ('BDT', 'BDT - Bangladesh Taka'),
        ('BEF', 'BEF - Belgian Franc'),
        ('BGN', 'BGN - Bulgarian Lev'),
        ('BHD', 'BHD - Bahrain Dinar'),
        ('BIF', 'BIF - Burundi Franc'),
        ('BMD', 'BMD - Bermudan Dollar'),
        ('BND', 'BND - Brunei Dollar'),
        ('BOB', 'BOB - Boliviano'),
        ('BRL', 'BRL - Brazilian Real'),
        ('BSD', 'BSD - Bahaman Dollar'),
        ('BTN', 'BTN - Bhutan Ngultrum'),
        ('BWP', 'BWP - Botswana Pula'),
        ('BYB', 'BYB - Belorussian Ruble (Old)'),
        ('BYR', 'BYR - Belorussian Ruble'),
        ('BZD', 'BZD - Belize Dollar'),
        ('CAD', 'CAD - Canadian Dollar'),
        ('CDF', 'CDF - Congolese Franc'),
        ('CFP', 'CFP - French Franc (Pacific Islands)'),
        ('CHF', 'CHF - Swiss Franc'),
        ('CLP', 'CLP - Chilean Peso'),
        ('CNY', 'CNY - Chinesische Yuan (international)'),
        ('COP', 'COP - Colombian Peso'),
        ('CRC', 'CRC - Costa Rica Colon'),
        ('CSD', 'CSD - Serbian Dinar'),
        ('CUP', 'CUP - Cuban Peso'),
        ('CVE', 'CVE - Cape Verde Escudo'),
        ('CYP', 'CYP - Cyprus Pound'),
        ('CZK', 'CZK - Czech Krona'),
        ('DEM', 'DEM - German Mark'),
        ('DEM3', 'DEM3 - (Internal) German Mark (3 dec.places)'),
        ('DJF', 'DJF - Djibouti Franc'),
        ('DKK', 'DKK - Danish Krone'),
        ('DOP', 'DOP - Dominican Peso'),
        ('DZD', 'DZD - Algerian Dinar'),
        ('ECS', 'ECS - Ecuadorian Sucre (  &gt; USD)'),
        ('EEK', 'EEK - Estonian Krone'),
        ('EGP', 'EGP - Egyptian Pound'),
        ('ERN', 'ERN - Eritrean Nafka'),
        ('ESP', 'ESP - Spanish Peseta'),
        ('ETB', 'ETB - Ethiopian Birr'),
        ('EUR', 'EUR - European Euro'),
        ('FIM', 'FIM - Finnish markka'),
        ('FJD', 'FJD - Fiji Dollar'),
        ('FKP', 'FKP - Falkland Pound'),
        ('FRF', 'FRF - French Franc'),
        ('GEL', 'GEL - Georgian Lari'),
        ('GHC', 'GHC - Ghanian Cedi'),
        ('GIP', 'GIP - Gibraltar Pound'),
        ('GMD', 'GMD - Gambian Dalasi'),
        ('GNF', 'GNF - Guinean Franc'),
        ('GRD', 'GRD - Greek Drachma'),
        ('GTQ', 'GTQ - Guatemalan Quetzal'),
        ('GWP', 'GWP - Guinea Peso'),
        ('GYD', 'GYD - Guyana Dollar'),
        ('HKD', 'HKD - Hong Kong Dollar'),
        ('HNL', 'HNL - Honduran Lempira'),
        ('HRK', 'HRK - Croatian Kuna'),
        ('HTG', 'HTG - Haitian Gourde'),
        ('HUF', 'HUF - Hungarian Forint'),
        ('IDR', 'IDR - Indonesian Rupiah'),
        ('IEP', 'IEP - Irish Punt'),
        ('ILS', 'ILS - Israeli Scheckel'),
        ('INR', 'INR - Indian Rupee'),
        ('IQD', 'IQD - Iraqui Dinar'),
        ('IRR', 'IRR - Iranian Rial'),
        ('ISK', 'ISK - Iceland Krona'),
        ('ITL', 'ITL - Italian Lira'),
        ('JMD', 'JMD - Jamaican Dollar'),
        ('JOD', 'JOD - Jordanian Dinar'),
        ('JPY', 'JPY - Japanese Yen'),
        ('KES', 'KES - Kenyan Shilling'),
        ('KGS', 'KGS - Kyrgyzstan Som'),
        ('KHR', 'KHR - Cambodian Riel'),
        ('KMF', 'KMF - Comoros Franc'),
        ('KPW', 'KPW - North Korean Won'),
        ('KRW', 'KRW - South Korean Won'),
        ('KWD', 'KWD - Kuwaiti Dinar'),
        ('KYD', 'KYD - Cayman Dollar'),
        ('KZT', 'KZT - Kazakstanian Tenge'),
        ('LAK', 'LAK - Laotian Kip'),
        ('LBP', 'LBP - Lebanese Pound'),
        ('LKR', 'LKR - Sri Lankan Rupee'),
        ('LRD', 'LRD - Liberian Dollar'),
        ('LSL', 'LSL - Lesotho Loti'),
        ('LTL', 'LTL - Lithuanian Lita'),
        ('LUF', 'LUF - Luxembourg Franc'),
        ('LVL', 'LVL - Latvian Lat'),
        ('LYD', 'LYD - Libyan Dinar'),
        ('MAD', 'MAD - Moroccan Dirham'),
        ('MDL', 'MDL - Moldavian Leu'),
        ('MGA', 'MGA - Madagascan Ariary (New)'),
        ('MGF', 'MGF - Madagascan Franc (Old'),
        ('MKD', 'MKD - Macedonian Denar'),
        ('MMK', 'MMK - Myanmar Kyat'),
        ('MNT', 'MNT - Mongolian Tugrik'),
        ('MOP', 'MOP - Macao Pataca'),
        ('MRO', 'MRO - Mauritanian Ouguiya'),
        ('MTL', 'MTL - Maltese Lira'),
        ('MUR', 'MUR - Mauritian Rupee'),
        ('MVR', 'MVR - Maldive Rufiyaa'),
        ('MWK', 'MWK - Malawi Kwacha'),
        ('MXN', 'MXN - Mexican Pesos'),
        ('MYR', 'MYR - Malaysian Ringgit'),
        ('MZM', 'MZM - Mozambique Metical'),
        ('NAD', 'NAD - Namibian Dollar'),
        ('NGN', 'NGN - Nigerian Naira'),
        ('NIO', 'NIO - Nicaraguan Cordoba Oro'),
        ('NLG', 'NLG - Dutch Guilder'),
        ('NOK', 'NOK - Norwegian Krone'),
        ('NPR', 'NPR - Nepalese Rupee'),
        ('NZD', 'NZD - New Zealand Dollars'),
        ('NZD5', 'NZD5 - New Zealand Dollars'),
        ('OMR', 'OMR - Omani Rial'),
        ('PAB', 'PAB - Panamanian Balboa'),
        ('PEN', 'PEN - Peruvian New Sol'),
        ('PGK', 'PGK - Papua New Guinea Kina'),
        ('PHP', 'PHP - Philippine Peso'),
        ('PKR', 'PKR - Pakistani Rupee'),
        ('PLN', 'PLN - Polish Zloty (new)'),
        ('PTE', 'PTE - Portuguese Escudo'),
        ('PYG', 'PYG - Paraguayan Guarani'),
        ('QAR', 'QAR - Qatar Rial'),
        ('RMB', 'RMB - Chinesische Renminbi (national)'),
        ('ROL', 'ROL - Romanian Leu'),
        ('RUB', 'RUB - Russian Ruble'),
        ('RWF', 'RWF - Rwandan Franc'),
        ('SAR', 'SAR - Saudi Riyal'),
        ('SBD', 'SBD - Solomon Islands Dollar'),
        ('SCR', 'SCR - Seychelles Rupee'),
        ('SDD', 'SDD - Sudanese Dinar'),
        ('SDP', 'SDP - Sudanese Pound'),
        ('SEK', 'SEK - Swedish Krona'),
        ('SGD', 'SGD - Singapore Dollar'),
        ('SHP', 'SHP - St.Helena Pound'),
        ('SIT', 'SIT - Slovenian Tolar'),
        ('SKK', 'SKK - Slovakian Krona'),
        ('SLL', 'SLL - Sierra Leone Leone'),
        ('SOS', 'SOS - Somalian Shilling'),
        ('SRD', 'SRD - Surinam Dollar'),
        ('SRG', 'SRG - Surinam Guilder (Old)'),
        ('STD', 'STD - Sao Tome / Principe Dobra'),
        ('SVC', 'SVC - El Salvador Colon'),
        ('SYP', 'SYP - Syrian Pound'),
        ('SZL', 'SZL - Swaziland Lilangeni'),
        ('THB', 'THB - Thailand Baht'),
        ('TJR', 'TJR - Tajikistani Ruble (Old)'),
        ('TJS', 'TJS - Tajikistani Somoni'),
        ('TMM', 'TMM - Turkmenistani Manat'),
        ('TND', 'TND - Tunisian Dinar'),
        ('TOP', 'TOP - Tongan Pa\'anga'),
        ('TPE', 'TPE - Timor Escudo'),
        ('TRL', 'TRL - Turkish Lira (Old)'),
        ('TRY', 'TRY - Turkish Lira'),
        ('TTD', 'TTD - Trinidad and Tobago Dollar'),
        ('TWD', 'TWD - New Taiwan Dollar'),
        ('TZS', 'TZS - Tanzanian Shilling'),
        ('UAH', 'UAH - Ukraine Hryvnia'),
        ('UGX', 'UGX - Ugandan Shilling'),
        ('USD', 'USD - United States Dollar'),
        ('USDN', 'USDN - (Internal) United States Dollar (5 Dec.)'),
        ('UYU', 'UYU - Uruguayan Peso (new)'),
        ('UZS', 'UZS - Uzbekistan Som'),
        ('VEB', 'VEB - Venezuelan Bolivar'),
        ('VEF', 'VEF - Venezuelan Bolivar Hard'),
        ('VND', 'VND - Vietnamese Dong'),
        ('VUV', 'VUV - Vanuatu Vatu'),
        ('WST', 'WST - Samoan Tala'),
        ('XAF', 'XAF - Gabon CFA Franc BEAC'),
        ('XCD', 'XCD - East Carribean Dollar'),
        ('XDS', 'XDS - St. Christopher Dollar'),
        ('XEU', 'XEU - European Currency Unit (E.C.U.)'),
        ('XOF', 'XOF - Benin CFA Franc BCEAO'),
        ('XPF', 'XPF - CFP Franc'),
        ('YER', 'YER - Yemeni Ryal'),
        ('YUM', 'YUM - New Yugoslavian Dinar (Old)'),
        ('ZAR', 'ZAR - South African Rand'),
        ('ZMK', 'ZMK - Zambian Kwacha'),
        ('ZRN', 'ZRN - Zaire (Old)'),
        ('ZWD', 'ZWD - Zimbabwean Dollar'),
    ]
    p_mata_uang = models.CharField(
        max_length=4,
        choices=MATA_UANG_CHOICES,
    )
    p_dokumen = models.FileField(upload_to=get_upload_path,
                               validators=[FileExtensionValidator(allowed_extensions=['pdf'])])


class PengalamanMitraKerjaPerusahaan(models.Model):
    def get_upload_path(instance, m_dokumen):
        return "vendor/"+str(instance.user.id)+"/pengalaman/"+m_dokumen
  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    m_nama = models.CharField(max_length=150)
    m_lokasi = models.TextField(max_length=200)
    m_bidang_usaha = models.ForeignKey(
        MasterBidangUsaha, on_delete=models.CASCADE)
    m_mulai_kerjasama = models.DateField()
    m_nilai_kontrak = models.BigIntegerField()
    MATA_UANG_CHOICES = [
        ('ADP', 'ADP - Andoran peseta'),
        ('AED', 'AED - United Arab Emirates Dirham'),
        ('AFA', 'AFA - Afghani (Old)'),
        ('AFN', 'AFN - Afghani'),
        ('ALL', 'ALL - Albanian Lek'),
        ('AMD', 'AMD - Armenian Dram'),
        ('ANG', 'ANG - West Indian Guilder'),
        ('AOA', 'AOA - Angolanische Kwanza'),
        ('AON', 'AON - Angolan New Kwanza (Old)'),
        ('AOR', 'AOR - Angolan Kwanza Reajustado (Old)'),
        ('ARS', 'ARS - Argentine Peso'),
        ('ATS', 'ATS - Austrian Schilling'),
        ('AUD', 'AUD - Australian Dollar'),
        ('AWG', 'AWG - Aruban Guilder'),
        ('AZM', 'AZM - Azerbaijan Manat'),
        ('BAM', 'BAM - Bosnia and Herzegovina Convertible Mark'),
        ('BBD', 'BBD - Barbados Dollar'),
        ('BDT', 'BDT - Bangladesh Taka'),
        ('BEF', 'BEF - Belgian Franc'),
        ('BGN', 'BGN - Bulgarian Lev'),
        ('BHD', 'BHD - Bahrain Dinar'),
        ('BIF', 'BIF - Burundi Franc'),
        ('BMD', 'BMD - Bermudan Dollar'),
        ('BND', 'BND - Brunei Dollar'),
        ('BOB', 'BOB - Boliviano'),
        ('BRL', 'BRL - Brazilian Real'),
        ('BSD', 'BSD - Bahaman Dollar'),
        ('BTN', 'BTN - Bhutan Ngultrum'),
        ('BWP', 'BWP - Botswana Pula'),
        ('BYB', 'BYB - Belorussian Ruble (Old)'),
        ('BYR', 'BYR - Belorussian Ruble'),
        ('BZD', 'BZD - Belize Dollar'),
        ('CAD', 'CAD - Canadian Dollar'),
        ('CDF', 'CDF - Congolese Franc'),
        ('CFP', 'CFP - French Franc (Pacific Islands)'),
        ('CHF', 'CHF - Swiss Franc'),
        ('CLP', 'CLP - Chilean Peso'),
        ('CNY', 'CNY - Chinesische Yuan (international)'),
        ('COP', 'COP - Colombian Peso'),
        ('CRC', 'CRC - Costa Rica Colon'),
        ('CSD', 'CSD - Serbian Dinar'),
        ('CUP', 'CUP - Cuban Peso'),
        ('CVE', 'CVE - Cape Verde Escudo'),
        ('CYP', 'CYP - Cyprus Pound'),
        ('CZK', 'CZK - Czech Krona'),
        ('DEM', 'DEM - German Mark'),
        ('DEM3', 'DEM3 - (Internal) German Mark (3 dec.places)'),
        ('DJF', 'DJF - Djibouti Franc'),
        ('DKK', 'DKK - Danish Krone'),
        ('DOP', 'DOP - Dominican Peso'),
        ('DZD', 'DZD - Algerian Dinar'),
        ('ECS', 'ECS - Ecuadorian Sucre (  &gt; USD)'),
        ('EEK', 'EEK - Estonian Krone'),
        ('EGP', 'EGP - Egyptian Pound'),
        ('ERN', 'ERN - Eritrean Nafka'),
        ('ESP', 'ESP - Spanish Peseta'),
        ('ETB', 'ETB - Ethiopian Birr'),
        ('EUR', 'EUR - European Euro'),
        ('FIM', 'FIM - Finnish markka'),
        ('FJD', 'FJD - Fiji Dollar'),
        ('FKP', 'FKP - Falkland Pound'),
        ('FRF', 'FRF - French Franc'),
        ('GEL', 'GEL - Georgian Lari'),
        ('GHC', 'GHC - Ghanian Cedi'),
        ('GIP', 'GIP - Gibraltar Pound'),
        ('GMD', 'GMD - Gambian Dalasi'),
        ('GNF', 'GNF - Guinean Franc'),
        ('GRD', 'GRD - Greek Drachma'),
        ('GTQ', 'GTQ - Guatemalan Quetzal'),
        ('GWP', 'GWP - Guinea Peso'),
        ('GYD', 'GYD - Guyana Dollar'),
        ('HKD', 'HKD - Hong Kong Dollar'),
        ('HNL', 'HNL - Honduran Lempira'),
        ('HRK', 'HRK - Croatian Kuna'),
        ('HTG', 'HTG - Haitian Gourde'),
        ('HUF', 'HUF - Hungarian Forint'),
        ('IDR', 'IDR - Indonesian Rupiah'),
        ('IEP', 'IEP - Irish Punt'),
        ('ILS', 'ILS - Israeli Scheckel'),
        ('INR', 'INR - Indian Rupee'),
        ('IQD', 'IQD - Iraqui Dinar'),
        ('IRR', 'IRR - Iranian Rial'),
        ('ISK', 'ISK - Iceland Krona'),
        ('ITL', 'ITL - Italian Lira'),
        ('JMD', 'JMD - Jamaican Dollar'),
        ('JOD', 'JOD - Jordanian Dinar'),
        ('JPY', 'JPY - Japanese Yen'),
        ('KES', 'KES - Kenyan Shilling'),
        ('KGS', 'KGS - Kyrgyzstan Som'),
        ('KHR', 'KHR - Cambodian Riel'),
        ('KMF', 'KMF - Comoros Franc'),
        ('KPW', 'KPW - North Korean Won'),
        ('KRW', 'KRW - South Korean Won'),
        ('KWD', 'KWD - Kuwaiti Dinar'),
        ('KYD', 'KYD - Cayman Dollar'),
        ('KZT', 'KZT - Kazakstanian Tenge'),
        ('LAK', 'LAK - Laotian Kip'),
        ('LBP', 'LBP - Lebanese Pound'),
        ('LKR', 'LKR - Sri Lankan Rupee'),
        ('LRD', 'LRD - Liberian Dollar'),
        ('LSL', 'LSL - Lesotho Loti'),
        ('LTL', 'LTL - Lithuanian Lita'),
        ('LUF', 'LUF - Luxembourg Franc'),
        ('LVL', 'LVL - Latvian Lat'),
        ('LYD', 'LYD - Libyan Dinar'),
        ('MAD', 'MAD - Moroccan Dirham'),
        ('MDL', 'MDL - Moldavian Leu'),
        ('MGA', 'MGA - Madagascan Ariary (New)'),
        ('MGF', 'MGF - Madagascan Franc (Old'),
        ('MKD', 'MKD - Macedonian Denar'),
        ('MMK', 'MMK - Myanmar Kyat'),
        ('MNT', 'MNT - Mongolian Tugrik'),
        ('MOP', 'MOP - Macao Pataca'),
        ('MRO', 'MRO - Mauritanian Ouguiya'),
        ('MTL', 'MTL - Maltese Lira'),
        ('MUR', 'MUR - Mauritian Rupee'),
        ('MVR', 'MVR - Maldive Rufiyaa'),
        ('MWK', 'MWK - Malawi Kwacha'),
        ('MXN', 'MXN - Mexican Pesos'),
        ('MYR', 'MYR - Malaysian Ringgit'),
        ('MZM', 'MZM - Mozambique Metical'),
        ('NAD', 'NAD - Namibian Dollar'),
        ('NGN', 'NGN - Nigerian Naira'),
        ('NIO', 'NIO - Nicaraguan Cordoba Oro'),
        ('NLG', 'NLG - Dutch Guilder'),
        ('NOK', 'NOK - Norwegian Krone'),
        ('NPR', 'NPR - Nepalese Rupee'),
        ('NZD', 'NZD - New Zealand Dollars'),
        ('NZD5', 'NZD5 - New Zealand Dollars'),
        ('OMR', 'OMR - Omani Rial'),
        ('PAB', 'PAB - Panamanian Balboa'),
        ('PEN', 'PEN - Peruvian New Sol'),
        ('PGK', 'PGK - Papua New Guinea Kina'),
        ('PHP', 'PHP - Philippine Peso'),
        ('PKR', 'PKR - Pakistani Rupee'),
        ('PLN', 'PLN - Polish Zloty (new)'),
        ('PTE', 'PTE - Portuguese Escudo'),
        ('PYG', 'PYG - Paraguayan Guarani'),
        ('QAR', 'QAR - Qatar Rial'),
        ('RMB', 'RMB - Chinesische Renminbi (national)'),
        ('ROL', 'ROL - Romanian Leu'),
        ('RUB', 'RUB - Russian Ruble'),
        ('RWF', 'RWF - Rwandan Franc'),
        ('SAR', 'SAR - Saudi Riyal'),
        ('SBD', 'SBD - Solomon Islands Dollar'),
        ('SCR', 'SCR - Seychelles Rupee'),
        ('SDD', 'SDD - Sudanese Dinar'),
        ('SDP', 'SDP - Sudanese Pound'),
        ('SEK', 'SEK - Swedish Krona'),
        ('SGD', 'SGD - Singapore Dollar'),
        ('SHP', 'SHP - St.Helena Pound'),
        ('SIT', 'SIT - Slovenian Tolar'),
        ('SKK', 'SKK - Slovakian Krona'),
        ('SLL', 'SLL - Sierra Leone Leone'),
        ('SOS', 'SOS - Somalian Shilling'),
        ('SRD', 'SRD - Surinam Dollar'),
        ('SRG', 'SRG - Surinam Guilder (Old)'),
        ('STD', 'STD - Sao Tome / Principe Dobra'),
        ('SVC', 'SVC - El Salvador Colon'),
        ('SYP', 'SYP - Syrian Pound'),
        ('SZL', 'SZL - Swaziland Lilangeni'),
        ('THB', 'THB - Thailand Baht'),
        ('TJR', 'TJR - Tajikistani Ruble (Old)'),
        ('TJS', 'TJS - Tajikistani Somoni'),
        ('TMM', 'TMM - Turkmenistani Manat'),
        ('TND', 'TND - Tunisian Dinar'),
        ('TOP', 'TOP - Tongan Pa\'anga'),
        ('TPE', 'TPE - Timor Escudo'),
        ('TRL', 'TRL - Turkish Lira (Old)'),
        ('TRY', 'TRY - Turkish Lira'),
        ('TTD', 'TTD - Trinidad and Tobago Dollar'),
        ('TWD', 'TWD - New Taiwan Dollar'),
        ('TZS', 'TZS - Tanzanian Shilling'),
        ('UAH', 'UAH - Ukraine Hryvnia'),
        ('UGX', 'UGX - Ugandan Shilling'),
        ('USD', 'USD - United States Dollar'),
        ('USDN', 'USDN - (Internal) United States Dollar (5 Dec.)'),
        ('UYU', 'UYU - Uruguayan Peso (new)'),
        ('UZS', 'UZS - Uzbekistan Som'),
        ('VEB', 'VEB - Venezuelan Bolivar'),
        ('VEF', 'VEF - Venezuelan Bolivar Hard'),
        ('VND', 'VND - Vietnamese Dong'),
        ('VUV', 'VUV - Vanuatu Vatu'),
        ('WST', 'WST - Samoan Tala'),
        ('XAF', 'XAF - Gabon CFA Franc BEAC'),
        ('XCD', 'XCD - East Carribean Dollar'),
        ('XDS', 'XDS - St. Christopher Dollar'),
        ('XEU', 'XEU - European Currency Unit (E.C.U.)'),
        ('XOF', 'XOF - Benin CFA Franc BCEAO'),
        ('XPF', 'XPF - CFP Franc'),
        ('YER', 'YER - Yemeni Ryal'),
        ('YUM', 'YUM - New Yugoslavian Dinar (Old)'),
        ('ZAR', 'ZAR - South African Rand'),
        ('ZMK', 'ZMK - Zambian Kwacha'),
        ('ZRN', 'ZRN - Zaire (Old)'),
        ('ZWD', 'ZWD - Zimbabwean Dollar'),
    ]
    m_mata_uang = models.CharField(
        max_length=4,
        choices=MATA_UANG_CHOICES,
    )
    m_dokumen = models.FileField(upload_to=get_upload_path,
                               validators=[FileExtensionValidator(allowed_extensions=['pdf'])])


class PekerjaanBerjalanPerusahaan(models.Model):
    def get_upload_path(instance, b_dokumen):
        return "vendor/"+str(instance.user.id)+"/pengalaman/"+b_dokumen

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    b_nama = models.CharField(max_length=150)
    b_lokasi = models.TextField(max_length=200)
    b_bidang_usaha = models.ForeignKey(
        MasterBidangUsaha, on_delete=models.CASCADE)
    b_mulai_kerjasama = models.DateField()
    b_nilai_kontrak = models.BigIntegerField()
    MATA_UANG_CHOICES = [
        ('ADP', 'ADP - Andoran peseta'),
        ('AED', 'AED - United Arab Emirates Dirham'),
        ('AFA', 'AFA - Afghani (Old)'),
        ('AFN', 'AFN - Afghani'),
        ('ALL', 'ALL - Albanian Lek'),
        ('AMD', 'AMD - Armenian Dram'),
        ('ANG', 'ANG - West Indian Guilder'),
        ('AOA', 'AOA - Angolanische Kwanza'),
        ('AON', 'AON - Angolan New Kwanza (Old)'),
        ('AOR', 'AOR - Angolan Kwanza Reajustado (Old)'),
        ('ARS', 'ARS - Argentine Peso'),
        ('ATS', 'ATS - Austrian Schilling'),
        ('AUD', 'AUD - Australian Dollar'),
        ('AWG', 'AWG - Aruban Guilder'),
        ('AZM', 'AZM - Azerbaijan Manat'),
        ('BAM', 'BAM - Bosnia and Herzegovina Convertible Mark'),
        ('BBD', 'BBD - Barbados Dollar'),
        ('BDT', 'BDT - Bangladesh Taka'),
        ('BEF', 'BEF - Belgian Franc'),
        ('BGN', 'BGN - Bulgarian Lev'),
        ('BHD', 'BHD - Bahrain Dinar'),
        ('BIF', 'BIF - Burundi Franc'),
        ('BMD', 'BMD - Bermudan Dollar'),
        ('BND', 'BND - Brunei Dollar'),
        ('BOB', 'BOB - Boliviano'),
        ('BRL', 'BRL - Brazilian Real'),
        ('BSD', 'BSD - Bahaman Dollar'),
        ('BTN', 'BTN - Bhutan Ngultrum'),
        ('BWP', 'BWP - Botswana Pula'),
        ('BYB', 'BYB - Belorussian Ruble (Old)'),
        ('BYR', 'BYR - Belorussian Ruble'),
        ('BZD', 'BZD - Belize Dollar'),
        ('CAD', 'CAD - Canadian Dollar'),
        ('CDF', 'CDF - Congolese Franc'),
        ('CFP', 'CFP - French Franc (Pacific Islands)'),
        ('CHF', 'CHF - Swiss Franc'),
        ('CLP', 'CLP - Chilean Peso'),
        ('CNY', 'CNY - Chinesische Yuan (international)'),
        ('COP', 'COP - Colombian Peso'),
        ('CRC', 'CRC - Costa Rica Colon'),
        ('CSD', 'CSD - Serbian Dinar'),
        ('CUP', 'CUP - Cuban Peso'),
        ('CVE', 'CVE - Cape Verde Escudo'),
        ('CYP', 'CYP - Cyprus Pound'),
        ('CZK', 'CZK - Czech Krona'),
        ('DEM', 'DEM - German Mark'),
        ('DEM3', 'DEM3 - (Internal) German Mark (3 dec.places)'),
        ('DJF', 'DJF - Djibouti Franc'),
        ('DKK', 'DKK - Danish Krone'),
        ('DOP', 'DOP - Dominican Peso'),
        ('DZD', 'DZD - Algerian Dinar'),
        ('ECS', 'ECS - Ecuadorian Sucre (  &gt; USD)'),
        ('EEK', 'EEK - Estonian Krone'),
        ('EGP', 'EGP - Egyptian Pound'),
        ('ERN', 'ERN - Eritrean Nafka'),
        ('ESP', 'ESP - Spanish Peseta'),
        ('ETB', 'ETB - Ethiopian Birr'),
        ('EUR', 'EUR - European Euro'),
        ('FIM', 'FIM - Finnish markka'),
        ('FJD', 'FJD - Fiji Dollar'),
        ('FKP', 'FKP - Falkland Pound'),
        ('FRF', 'FRF - French Franc'),
        ('GEL', 'GEL - Georgian Lari'),
        ('GHC', 'GHC - Ghanian Cedi'),
        ('GIP', 'GIP - Gibraltar Pound'),
        ('GMD', 'GMD - Gambian Dalasi'),
        ('GNF', 'GNF - Guinean Franc'),
        ('GRD', 'GRD - Greek Drachma'),
        ('GTQ', 'GTQ - Guatemalan Quetzal'),
        ('GWP', 'GWP - Guinea Peso'),
        ('GYD', 'GYD - Guyana Dollar'),
        ('HKD', 'HKD - Hong Kong Dollar'),
        ('HNL', 'HNL - Honduran Lempira'),
        ('HRK', 'HRK - Croatian Kuna'),
        ('HTG', 'HTG - Haitian Gourde'),
        ('HUF', 'HUF - Hungarian Forint'),
        ('IDR', 'IDR - Indonesian Rupiah'),
        ('IEP', 'IEP - Irish Punt'),
        ('ILS', 'ILS - Israeli Scheckel'),
        ('INR', 'INR - Indian Rupee'),
        ('IQD', 'IQD - Iraqui Dinar'),
        ('IRR', 'IRR - Iranian Rial'),
        ('ISK', 'ISK - Iceland Krona'),
        ('ITL', 'ITL - Italian Lira'),
        ('JMD', 'JMD - Jamaican Dollar'),
        ('JOD', 'JOD - Jordanian Dinar'),
        ('JPY', 'JPY - Japanese Yen'),
        ('KES', 'KES - Kenyan Shilling'),
        ('KGS', 'KGS - Kyrgyzstan Som'),
        ('KHR', 'KHR - Cambodian Riel'),
        ('KMF', 'KMF - Comoros Franc'),
        ('KPW', 'KPW - North Korean Won'),
        ('KRW', 'KRW - South Korean Won'),
        ('KWD', 'KWD - Kuwaiti Dinar'),
        ('KYD', 'KYD - Cayman Dollar'),
        ('KZT', 'KZT - Kazakstanian Tenge'),
        ('LAK', 'LAK - Laotian Kip'),
        ('LBP', 'LBP - Lebanese Pound'),
        ('LKR', 'LKR - Sri Lankan Rupee'),
        ('LRD', 'LRD - Liberian Dollar'),
        ('LSL', 'LSL - Lesotho Loti'),
        ('LTL', 'LTL - Lithuanian Lita'),
        ('LUF', 'LUF - Luxembourg Franc'),
        ('LVL', 'LVL - Latvian Lat'),
        ('LYD', 'LYD - Libyan Dinar'),
        ('MAD', 'MAD - Moroccan Dirham'),
        ('MDL', 'MDL - Moldavian Leu'),
        ('MGA', 'MGA - Madagascan Ariary (New)'),
        ('MGF', 'MGF - Madagascan Franc (Old'),
        ('MKD', 'MKD - Macedonian Denar'),
        ('MMK', 'MMK - Myanmar Kyat'),
        ('MNT', 'MNT - Mongolian Tugrik'),
        ('MOP', 'MOP - Macao Pataca'),
        ('MRO', 'MRO - Mauritanian Ouguiya'),
        ('MTL', 'MTL - Maltese Lira'),
        ('MUR', 'MUR - Mauritian Rupee'),
        ('MVR', 'MVR - Maldive Rufiyaa'),
        ('MWK', 'MWK - Malawi Kwacha'),
        ('MXN', 'MXN - Mexican Pesos'),
        ('MYR', 'MYR - Malaysian Ringgit'),
        ('MZM', 'MZM - Mozambique Metical'),
        ('NAD', 'NAD - Namibian Dollar'),
        ('NGN', 'NGN - Nigerian Naira'),
        ('NIO', 'NIO - Nicaraguan Cordoba Oro'),
        ('NLG', 'NLG - Dutch Guilder'),
        ('NOK', 'NOK - Norwegian Krone'),
        ('NPR', 'NPR - Nepalese Rupee'),
        ('NZD', 'NZD - New Zealand Dollars'),
        ('NZD5', 'NZD5 - New Zealand Dollars'),
        ('OMR', 'OMR - Omani Rial'),
        ('PAB', 'PAB - Panamanian Balboa'),
        ('PEN', 'PEN - Peruvian New Sol'),
        ('PGK', 'PGK - Papua New Guinea Kina'),
        ('PHP', 'PHP - Philippine Peso'),
        ('PKR', 'PKR - Pakistani Rupee'),
        ('PLN', 'PLN - Polish Zloty (new)'),
        ('PTE', 'PTE - Portuguese Escudo'),
        ('PYG', 'PYG - Paraguayan Guarani'),
        ('QAR', 'QAR - Qatar Rial'),
        ('RMB', 'RMB - Chinesische Renminbi (national)'),
        ('ROL', 'ROL - Romanian Leu'),
        ('RUB', 'RUB - Russian Ruble'),
        ('RWF', 'RWF - Rwandan Franc'),
        ('SAR', 'SAR - Saudi Riyal'),
        ('SBD', 'SBD - Solomon Islands Dollar'),
        ('SCR', 'SCR - Seychelles Rupee'),
        ('SDD', 'SDD - Sudanese Dinar'),
        ('SDP', 'SDP - Sudanese Pound'),
        ('SEK', 'SEK - Swedish Krona'),
        ('SGD', 'SGD - Singapore Dollar'),
        ('SHP', 'SHP - St.Helena Pound'),
        ('SIT', 'SIT - Slovenian Tolar'),
        ('SKK', 'SKK - Slovakian Krona'),
        ('SLL', 'SLL - Sierra Leone Leone'),
        ('SOS', 'SOS - Somalian Shilling'),
        ('SRD', 'SRD - Surinam Dollar'),
        ('SRG', 'SRG - Surinam Guilder (Old)'),
        ('STD', 'STD - Sao Tome / Principe Dobra'),
        ('SVC', 'SVC - El Salvador Colon'),
        ('SYP', 'SYP - Syrian Pound'),
        ('SZL', 'SZL - Swaziland Lilangeni'),
        ('THB', 'THB - Thailand Baht'),
        ('TJR', 'TJR - Tajikistani Ruble (Old)'),
        ('TJS', 'TJS - Tajikistani Somoni'),
        ('TMM', 'TMM - Turkmenistani Manat'),
        ('TND', 'TND - Tunisian Dinar'),
        ('TOP', 'TOP - Tongan Pa\'anga'),
        ('TPE', 'TPE - Timor Escudo'),
        ('TRL', 'TRL - Turkish Lira (Old)'),
        ('TRY', 'TRY - Turkish Lira'),
        ('TTD', 'TTD - Trinidad and Tobago Dollar'),
        ('TWD', 'TWD - New Taiwan Dollar'),
        ('TZS', 'TZS - Tanzanian Shilling'),
        ('UAH', 'UAH - Ukraine Hryvnia'),
        ('UGX', 'UGX - Ugandan Shilling'),
        ('USD', 'USD - United States Dollar'),
        ('USDN', 'USDN - (Internal) United States Dollar (5 Dec.)'),
        ('UYU', 'UYU - Uruguayan Peso (new)'),
        ('UZS', 'UZS - Uzbekistan Som'),
        ('VEB', 'VEB - Venezuelan Bolivar'),
        ('VEF', 'VEF - Venezuelan Bolivar Hard'),
        ('VND', 'VND - Vietnamese Dong'),
        ('VUV', 'VUV - Vanuatu Vatu'),
        ('WST', 'WST - Samoan Tala'),
        ('XAF', 'XAF - Gabon CFA Franc BEAC'),
        ('XCD', 'XCD - East Carribean Dollar'),
        ('XDS', 'XDS - St. Christopher Dollar'),
        ('XEU', 'XEU - European Currency Unit (E.C.U.)'),
        ('XOF', 'XOF - Benin CFA Franc BCEAO'),
        ('XPF', 'XPF - CFP Franc'),
        ('YER', 'YER - Yemeni Ryal'),
        ('YUM', 'YUM - New Yugoslavian Dinar (Old)'),
        ('ZAR', 'ZAR - South African Rand'),
        ('ZMK', 'ZMK - Zambian Kwacha'),
        ('ZRN', 'ZRN - Zaire (Old)'),
        ('ZWD', 'ZWD - Zimbabwean Dollar'),
    ]
    b_mata_uang = models.CharField(
        max_length=4,
        choices=MATA_UANG_CHOICES,
    )
    b_dokumen = models.FileField(upload_to=get_upload_path,
                               validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
