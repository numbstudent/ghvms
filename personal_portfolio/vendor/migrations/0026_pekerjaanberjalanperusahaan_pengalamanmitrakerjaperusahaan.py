# Generated by Django 3.1.6 on 2021-03-01 03:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import vendor.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0025_auto_20210301_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='PengalamanMitraKerjaPerusahaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=150)),
                ('lokasi', models.TextField(max_length=200)),
                ('mulai_kerjasama', models.DateField()),
                ('nilai_kontrak', models.IntegerField()),
                ('mata_uang', models.CharField(choices=[('ADP', 'ADP - Andoran peseta'), ('AED', 'AED - United Arab Emirates Dirham'), ('AFA', 'AFA - Afghani (Old)'), ('AFN', 'AFN - Afghani'), ('ALL', 'ALL - Albanian Lek'), ('AMD', 'AMD - Armenian Dram'), ('ANG', 'ANG - West Indian Guilder'), ('AOA', 'AOA - Angolanische Kwanza'), ('AON', 'AON - Angolan New Kwanza (Old)'), ('AOR', 'AOR - Angolan Kwanza Reajustado (Old)'), ('ARS', 'ARS - Argentine Peso'), ('ATS', 'ATS - Austrian Schilling'), ('AUD', 'AUD - Australian Dollar'), ('AWG', 'AWG - Aruban Guilder'), ('AZM', 'AZM - Azerbaijan Manat'), ('BAM', 'BAM - Bosnia and Herzegovina Convertible Mark'), ('BBD', 'BBD - Barbados Dollar'), ('BDT', 'BDT - Bangladesh Taka'), ('BEF', 'BEF - Belgian Franc'), ('BGN', 'BGN - Bulgarian Lev'), ('BHD', 'BHD - Bahrain Dinar'), ('BIF', 'BIF - Burundi Franc'), ('BMD', 'BMD - Bermudan Dollar'), ('BND', 'BND - Brunei Dollar'), ('BOB', 'BOB - Boliviano'), ('BRL', 'BRL - Brazilian Real'), ('BSD', 'BSD - Bahaman Dollar'), ('BTN', 'BTN - Bhutan Ngultrum'), ('BWP', 'BWP - Botswana Pula'), ('BYB', 'BYB - Belorussian Ruble (Old)'), ('BYR', 'BYR - Belorussian Ruble'), ('BZD', 'BZD - Belize Dollar'), ('CAD', 'CAD - Canadian Dollar'), ('CDF', 'CDF - Congolese Franc'), ('CFP', 'CFP - French Franc (Pacific Islands)'), ('CHF', 'CHF - Swiss Franc'), ('CLP', 'CLP - Chilean Peso'), ('CNY', 'CNY - Chinesische Yuan (international)'), ('COP', 'COP - Colombian Peso'), ('CRC', 'CRC - Costa Rica Colon'), ('CSD', 'CSD - Serbian Dinar'), ('CUP', 'CUP - Cuban Peso'), ('CVE', 'CVE - Cape Verde Escudo'), ('CYP', 'CYP - Cyprus Pound'), ('CZK', 'CZK - Czech Krona'), ('DEM', 'DEM - German Mark'), ('DEM3', 'DEM3 - (Internal) German Mark (3 dec.places)'), ('DJF', 'DJF - Djibouti Franc'), ('DKK', 'DKK - Danish Krone'), ('DOP', 'DOP - Dominican Peso'), ('DZD', 'DZD - Algerian Dinar'), ('ECS', 'ECS - Ecuadorian Sucre (  &gt; USD)'), ('EEK', 'EEK - Estonian Krone'), ('EGP', 'EGP - Egyptian Pound'), ('ERN', 'ERN - Eritrean Nafka'), ('ESP', 'ESP - Spanish Peseta'), ('ETB', 'ETB - Ethiopian Birr'), ('EUR', 'EUR - European Euro'), ('FIM', 'FIM - Finnish markka'), ('FJD', 'FJD - Fiji Dollar'), ('FKP', 'FKP - Falkland Pound'), ('FRF', 'FRF - French Franc'), ('GEL', 'GEL - Georgian Lari'), ('GHC', 'GHC - Ghanian Cedi'), ('GIP', 'GIP - Gibraltar Pound'), ('GMD', 'GMD - Gambian Dalasi'), ('GNF', 'GNF - Guinean Franc'), ('GRD', 'GRD - Greek Drachma'), ('GTQ', 'GTQ - Guatemalan Quetzal'), ('GWP', 'GWP - Guinea Peso'), ('GYD', 'GYD - Guyana Dollar'), ('HKD', 'HKD - Hong Kong Dollar'), ('HNL', 'HNL - Honduran Lempira'), ('HRK', 'HRK - Croatian Kuna'), ('HTG', 'HTG - Haitian Gourde'), ('HUF', 'HUF - Hungarian Forint'), ('IDR', 'IDR - Indonesian Rupiah'), ('IEP', 'IEP - Irish Punt'), ('ILS', 'ILS - Israeli Scheckel'), ('INR', 'INR - Indian Rupee'), ('IQD', 'IQD - Iraqui Dinar'), ('IRR', 'IRR - Iranian Rial'), ('ISK', 'ISK - Iceland Krona'), ('ITL', 'ITL - Italian Lira'), ('JMD', 'JMD - Jamaican Dollar'), ('JOD', 'JOD - Jordanian Dinar'), ('JPY', 'JPY - Japanese Yen'), ('KES', 'KES - Kenyan Shilling'), ('KGS', 'KGS - Kyrgyzstan Som'), ('KHR', 'KHR - Cambodian Riel'), ('KMF', 'KMF - Comoros Franc'), ('KPW', 'KPW - North Korean Won'), ('KRW', 'KRW - South Korean Won'), ('KWD', 'KWD - Kuwaiti Dinar'), ('KYD', 'KYD - Cayman Dollar'), ('KZT', 'KZT - Kazakstanian Tenge'), ('LAK', 'LAK - Laotian Kip'), ('LBP', 'LBP - Lebanese Pound'), ('LKR', 'LKR - Sri Lankan Rupee'), ('LRD', 'LRD - Liberian Dollar'), ('LSL', 'LSL - Lesotho Loti'), ('LTL', 'LTL - Lithuanian Lita'), ('LUF', 'LUF - Luxembourg Franc'), ('LVL', 'LVL - Latvian Lat'), ('LYD', 'LYD - Libyan Dinar'), ('MAD', 'MAD - Moroccan Dirham'), ('MDL', 'MDL - Moldavian Leu'), ('MGA', 'MGA - Madagascan Ariary (New)'), ('MGF', 'MGF - Madagascan Franc (Old'), ('MKD', 'MKD - Macedonian Denar'), ('MMK', 'MMK - Myanmar Kyat'), ('MNT', 'MNT - Mongolian Tugrik'), ('MOP', 'MOP - Macao Pataca'), ('MRO', 'MRO - Mauritanian Ouguiya'), ('MTL', 'MTL - Maltese Lira'), ('MUR', 'MUR - Mauritian Rupee'), ('MVR', 'MVR - Maldive Rufiyaa'), ('MWK', 'MWK - Malawi Kwacha'), ('MXN', 'MXN - Mexican Pesos'), ('MYR', 'MYR - Malaysian Ringgit'), ('MZM', 'MZM - Mozambique Metical'), ('NAD', 'NAD - Namibian Dollar'), ('NGN', 'NGN - Nigerian Naira'), ('NIO', 'NIO - Nicaraguan Cordoba Oro'), ('NLG', 'NLG - Dutch Guilder'), ('NOK', 'NOK - Norwegian Krone'), ('NPR', 'NPR - Nepalese Rupee'), ('NZD', 'NZD - New Zealand Dollars'), ('NZD5', 'NZD5 - New Zealand Dollars'), ('OMR', 'OMR - Omani Rial'), ('PAB', 'PAB - Panamanian Balboa'), ('PEN', 'PEN - Peruvian New Sol'), ('PGK', 'PGK - Papua New Guinea Kina'), ('PHP', 'PHP - Philippine Peso'), ('PKR', 'PKR - Pakistani Rupee'), ('PLN', 'PLN - Polish Zloty (new)'), ('PTE', 'PTE - Portuguese Escudo'), ('PYG', 'PYG - Paraguayan Guarani'), ('QAR', 'QAR - Qatar Rial'), ('RMB', 'RMB - Chinesische Renminbi (national)'), ('ROL', 'ROL - Romanian Leu'), ('RUB', 'RUB - Russian Ruble'), ('RWF', 'RWF - Rwandan Franc'), ('SAR', 'SAR - Saudi Riyal'), ('SBD', 'SBD - Solomon Islands Dollar'), ('SCR', 'SCR - Seychelles Rupee'), ('SDD', 'SDD - Sudanese Dinar'), ('SDP', 'SDP - Sudanese Pound'), ('SEK', 'SEK - Swedish Krona'), ('SGD', 'SGD - Singapore Dollar'), ('SHP', 'SHP - St.Helena Pound'), ('SIT', 'SIT - Slovenian Tolar'), ('SKK', 'SKK - Slovakian Krona'), ('SLL', 'SLL - Sierra Leone Leone'), ('SOS', 'SOS - Somalian Shilling'), ('SRD', 'SRD - Surinam Dollar'), ('SRG', 'SRG - Surinam Guilder (Old)'), ('STD', 'STD - Sao Tome / Principe Dobra'), ('SVC', 'SVC - El Salvador Colon'), ('SYP', 'SYP - Syrian Pound'), ('SZL', 'SZL - Swaziland Lilangeni'), ('THB', 'THB - Thailand Baht'), ('TJR', 'TJR - Tajikistani Ruble (Old)'), ('TJS', 'TJS - Tajikistani Somoni'), ('TMM', 'TMM - Turkmenistani Manat'), ('TND', 'TND - Tunisian Dinar'), ('TOP', "TOP - Tongan Pa'anga"), ('TPE', 'TPE - Timor Escudo'), ('TRL', 'TRL - Turkish Lira (Old)'), ('TRY', 'TRY - Turkish Lira'), ('TTD', 'TTD - Trinidad and Tobago Dollar'), ('TWD', 'TWD - New Taiwan Dollar'), ('TZS', 'TZS - Tanzanian Shilling'), ('UAH', 'UAH - Ukraine Hryvnia'), ('UGX', 'UGX - Ugandan Shilling'), ('USD', 'USD - United States Dollar'), ('USDN', 'USDN - (Internal) United States Dollar (5 Dec.)'), ('UYU', 'UYU - Uruguayan Peso (new)'), ('UZS', 'UZS - Uzbekistan Som'), ('VEB', 'VEB - Venezuelan Bolivar'), ('VEF', 'VEF - Venezuelan Bolivar Hard'), ('VND', 'VND - Vietnamese Dong'), ('VUV', 'VUV - Vanuatu Vatu'), ('WST', 'WST - Samoan Tala'), ('XAF', 'XAF - Gabon CFA Franc BEAC'), ('XCD', 'XCD - East Carribean Dollar'), ('XDS', 'XDS - St. Christopher Dollar'), ('XEU', 'XEU - European Currency Unit (E.C.U.)'), ('XOF', 'XOF - Benin CFA Franc BCEAO'), ('XPF', 'XPF - CFP Franc'), ('YER', 'YER - Yemeni Ryal'), ('YUM', 'YUM - New Yugoslavian Dinar (Old)'), ('ZAR', 'ZAR - South African Rand'), ('ZMK', 'ZMK - Zambian Kwacha'), ('ZRN', 'ZRN - Zaire (Old)'), ('ZWD', 'ZWD - Zimbabwean Dollar')], max_length=4)),
                ('dokumen', models.FileField(upload_to=vendor.models.PengalamanMitraKerjaPerusahaan.get_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('bidang_usaha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.masterbidangusaha')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PekerjaanBerjalanPerusahaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=150)),
                ('lokasi', models.TextField(max_length=200)),
                ('mulai_kerjasama', models.DateField()),
                ('nilai_kontrak', models.IntegerField()),
                ('mata_uang', models.CharField(choices=[('ADP', 'ADP - Andoran peseta'), ('AED', 'AED - United Arab Emirates Dirham'), ('AFA', 'AFA - Afghani (Old)'), ('AFN', 'AFN - Afghani'), ('ALL', 'ALL - Albanian Lek'), ('AMD', 'AMD - Armenian Dram'), ('ANG', 'ANG - West Indian Guilder'), ('AOA', 'AOA - Angolanische Kwanza'), ('AON', 'AON - Angolan New Kwanza (Old)'), ('AOR', 'AOR - Angolan Kwanza Reajustado (Old)'), ('ARS', 'ARS - Argentine Peso'), ('ATS', 'ATS - Austrian Schilling'), ('AUD', 'AUD - Australian Dollar'), ('AWG', 'AWG - Aruban Guilder'), ('AZM', 'AZM - Azerbaijan Manat'), ('BAM', 'BAM - Bosnia and Herzegovina Convertible Mark'), ('BBD', 'BBD - Barbados Dollar'), ('BDT', 'BDT - Bangladesh Taka'), ('BEF', 'BEF - Belgian Franc'), ('BGN', 'BGN - Bulgarian Lev'), ('BHD', 'BHD - Bahrain Dinar'), ('BIF', 'BIF - Burundi Franc'), ('BMD', 'BMD - Bermudan Dollar'), ('BND', 'BND - Brunei Dollar'), ('BOB', 'BOB - Boliviano'), ('BRL', 'BRL - Brazilian Real'), ('BSD', 'BSD - Bahaman Dollar'), ('BTN', 'BTN - Bhutan Ngultrum'), ('BWP', 'BWP - Botswana Pula'), ('BYB', 'BYB - Belorussian Ruble (Old)'), ('BYR', 'BYR - Belorussian Ruble'), ('BZD', 'BZD - Belize Dollar'), ('CAD', 'CAD - Canadian Dollar'), ('CDF', 'CDF - Congolese Franc'), ('CFP', 'CFP - French Franc (Pacific Islands)'), ('CHF', 'CHF - Swiss Franc'), ('CLP', 'CLP - Chilean Peso'), ('CNY', 'CNY - Chinesische Yuan (international)'), ('COP', 'COP - Colombian Peso'), ('CRC', 'CRC - Costa Rica Colon'), ('CSD', 'CSD - Serbian Dinar'), ('CUP', 'CUP - Cuban Peso'), ('CVE', 'CVE - Cape Verde Escudo'), ('CYP', 'CYP - Cyprus Pound'), ('CZK', 'CZK - Czech Krona'), ('DEM', 'DEM - German Mark'), ('DEM3', 'DEM3 - (Internal) German Mark (3 dec.places)'), ('DJF', 'DJF - Djibouti Franc'), ('DKK', 'DKK - Danish Krone'), ('DOP', 'DOP - Dominican Peso'), ('DZD', 'DZD - Algerian Dinar'), ('ECS', 'ECS - Ecuadorian Sucre (  &gt; USD)'), ('EEK', 'EEK - Estonian Krone'), ('EGP', 'EGP - Egyptian Pound'), ('ERN', 'ERN - Eritrean Nafka'), ('ESP', 'ESP - Spanish Peseta'), ('ETB', 'ETB - Ethiopian Birr'), ('EUR', 'EUR - European Euro'), ('FIM', 'FIM - Finnish markka'), ('FJD', 'FJD - Fiji Dollar'), ('FKP', 'FKP - Falkland Pound'), ('FRF', 'FRF - French Franc'), ('GEL', 'GEL - Georgian Lari'), ('GHC', 'GHC - Ghanian Cedi'), ('GIP', 'GIP - Gibraltar Pound'), ('GMD', 'GMD - Gambian Dalasi'), ('GNF', 'GNF - Guinean Franc'), ('GRD', 'GRD - Greek Drachma'), ('GTQ', 'GTQ - Guatemalan Quetzal'), ('GWP', 'GWP - Guinea Peso'), ('GYD', 'GYD - Guyana Dollar'), ('HKD', 'HKD - Hong Kong Dollar'), ('HNL', 'HNL - Honduran Lempira'), ('HRK', 'HRK - Croatian Kuna'), ('HTG', 'HTG - Haitian Gourde'), ('HUF', 'HUF - Hungarian Forint'), ('IDR', 'IDR - Indonesian Rupiah'), ('IEP', 'IEP - Irish Punt'), ('ILS', 'ILS - Israeli Scheckel'), ('INR', 'INR - Indian Rupee'), ('IQD', 'IQD - Iraqui Dinar'), ('IRR', 'IRR - Iranian Rial'), ('ISK', 'ISK - Iceland Krona'), ('ITL', 'ITL - Italian Lira'), ('JMD', 'JMD - Jamaican Dollar'), ('JOD', 'JOD - Jordanian Dinar'), ('JPY', 'JPY - Japanese Yen'), ('KES', 'KES - Kenyan Shilling'), ('KGS', 'KGS - Kyrgyzstan Som'), ('KHR', 'KHR - Cambodian Riel'), ('KMF', 'KMF - Comoros Franc'), ('KPW', 'KPW - North Korean Won'), ('KRW', 'KRW - South Korean Won'), ('KWD', 'KWD - Kuwaiti Dinar'), ('KYD', 'KYD - Cayman Dollar'), ('KZT', 'KZT - Kazakstanian Tenge'), ('LAK', 'LAK - Laotian Kip'), ('LBP', 'LBP - Lebanese Pound'), ('LKR', 'LKR - Sri Lankan Rupee'), ('LRD', 'LRD - Liberian Dollar'), ('LSL', 'LSL - Lesotho Loti'), ('LTL', 'LTL - Lithuanian Lita'), ('LUF', 'LUF - Luxembourg Franc'), ('LVL', 'LVL - Latvian Lat'), ('LYD', 'LYD - Libyan Dinar'), ('MAD', 'MAD - Moroccan Dirham'), ('MDL', 'MDL - Moldavian Leu'), ('MGA', 'MGA - Madagascan Ariary (New)'), ('MGF', 'MGF - Madagascan Franc (Old'), ('MKD', 'MKD - Macedonian Denar'), ('MMK', 'MMK - Myanmar Kyat'), ('MNT', 'MNT - Mongolian Tugrik'), ('MOP', 'MOP - Macao Pataca'), ('MRO', 'MRO - Mauritanian Ouguiya'), ('MTL', 'MTL - Maltese Lira'), ('MUR', 'MUR - Mauritian Rupee'), ('MVR', 'MVR - Maldive Rufiyaa'), ('MWK', 'MWK - Malawi Kwacha'), ('MXN', 'MXN - Mexican Pesos'), ('MYR', 'MYR - Malaysian Ringgit'), ('MZM', 'MZM - Mozambique Metical'), ('NAD', 'NAD - Namibian Dollar'), ('NGN', 'NGN - Nigerian Naira'), ('NIO', 'NIO - Nicaraguan Cordoba Oro'), ('NLG', 'NLG - Dutch Guilder'), ('NOK', 'NOK - Norwegian Krone'), ('NPR', 'NPR - Nepalese Rupee'), ('NZD', 'NZD - New Zealand Dollars'), ('NZD5', 'NZD5 - New Zealand Dollars'), ('OMR', 'OMR - Omani Rial'), ('PAB', 'PAB - Panamanian Balboa'), ('PEN', 'PEN - Peruvian New Sol'), ('PGK', 'PGK - Papua New Guinea Kina'), ('PHP', 'PHP - Philippine Peso'), ('PKR', 'PKR - Pakistani Rupee'), ('PLN', 'PLN - Polish Zloty (new)'), ('PTE', 'PTE - Portuguese Escudo'), ('PYG', 'PYG - Paraguayan Guarani'), ('QAR', 'QAR - Qatar Rial'), ('RMB', 'RMB - Chinesische Renminbi (national)'), ('ROL', 'ROL - Romanian Leu'), ('RUB', 'RUB - Russian Ruble'), ('RWF', 'RWF - Rwandan Franc'), ('SAR', 'SAR - Saudi Riyal'), ('SBD', 'SBD - Solomon Islands Dollar'), ('SCR', 'SCR - Seychelles Rupee'), ('SDD', 'SDD - Sudanese Dinar'), ('SDP', 'SDP - Sudanese Pound'), ('SEK', 'SEK - Swedish Krona'), ('SGD', 'SGD - Singapore Dollar'), ('SHP', 'SHP - St.Helena Pound'), ('SIT', 'SIT - Slovenian Tolar'), ('SKK', 'SKK - Slovakian Krona'), ('SLL', 'SLL - Sierra Leone Leone'), ('SOS', 'SOS - Somalian Shilling'), ('SRD', 'SRD - Surinam Dollar'), ('SRG', 'SRG - Surinam Guilder (Old)'), ('STD', 'STD - Sao Tome / Principe Dobra'), ('SVC', 'SVC - El Salvador Colon'), ('SYP', 'SYP - Syrian Pound'), ('SZL', 'SZL - Swaziland Lilangeni'), ('THB', 'THB - Thailand Baht'), ('TJR', 'TJR - Tajikistani Ruble (Old)'), ('TJS', 'TJS - Tajikistani Somoni'), ('TMM', 'TMM - Turkmenistani Manat'), ('TND', 'TND - Tunisian Dinar'), ('TOP', "TOP - Tongan Pa'anga"), ('TPE', 'TPE - Timor Escudo'), ('TRL', 'TRL - Turkish Lira (Old)'), ('TRY', 'TRY - Turkish Lira'), ('TTD', 'TTD - Trinidad and Tobago Dollar'), ('TWD', 'TWD - New Taiwan Dollar'), ('TZS', 'TZS - Tanzanian Shilling'), ('UAH', 'UAH - Ukraine Hryvnia'), ('UGX', 'UGX - Ugandan Shilling'), ('USD', 'USD - United States Dollar'), ('USDN', 'USDN - (Internal) United States Dollar (5 Dec.)'), ('UYU', 'UYU - Uruguayan Peso (new)'), ('UZS', 'UZS - Uzbekistan Som'), ('VEB', 'VEB - Venezuelan Bolivar'), ('VEF', 'VEF - Venezuelan Bolivar Hard'), ('VND', 'VND - Vietnamese Dong'), ('VUV', 'VUV - Vanuatu Vatu'), ('WST', 'WST - Samoan Tala'), ('XAF', 'XAF - Gabon CFA Franc BEAC'), ('XCD', 'XCD - East Carribean Dollar'), ('XDS', 'XDS - St. Christopher Dollar'), ('XEU', 'XEU - European Currency Unit (E.C.U.)'), ('XOF', 'XOF - Benin CFA Franc BCEAO'), ('XPF', 'XPF - CFP Franc'), ('YER', 'YER - Yemeni Ryal'), ('YUM', 'YUM - New Yugoslavian Dinar (Old)'), ('ZAR', 'ZAR - South African Rand'), ('ZMK', 'ZMK - Zambian Kwacha'), ('ZRN', 'ZRN - Zaire (Old)'), ('ZWD', 'ZWD - Zimbabwean Dollar')], max_length=4)),
                ('dokumen', models.FileField(upload_to=vendor.models.PekerjaanBerjalanPerusahaan.get_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('bidang_usaha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.masterbidangusaha')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
