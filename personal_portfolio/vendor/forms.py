from django import forms
from django.forms import ModelForm
from .models import *


class FormTipePerusahaan(ModelForm):
    class Meta:
        model = VendorGeneral
        fields = ('tipe_perusahaan',)
        widgets = {
            'tipe_perusahaan': forms.RadioSelect(),
        }


class FormDisclaimer(ModelForm):
    class Meta:
        model = VendorGeneral
        fields = ('disclaimer',)
        widgets = {
            'disclaimer': forms.HiddenInput(attrs={'value': 1})
        }


class FormDataPerusahaan(ModelForm):
    class Meta:
        model = VendorPerusahaan
        fields = (
            'tipe_pkp',
            'no_pkp',
            'kualifikasi',
            'grade',
            'nama_perusahaan',
            'bentuk_perusahaan',
            'npwp_perusahaan',
            'no_akte_perusahaan',
            'tanggal_berdiri_perusahaan',
            'tanggal_perubahan',
            'nama_singkatan',
            'website',
        )
        labels = {
            'tipe_pkp': 'Tipe PKP',
            'no_pkp': 'Nomor PKP',
            'npwp_perusahaan': 'NPWP Perusahaan',
        }
        widgets = {
            'tipe_pkp': forms.Select(),
            'no_pkp': forms.TextInput(
                attrs={'disabled': 'disabled'}),
            'tipe_perusahaan': forms.Select(),
            'website': forms.URLInput(),
            'tanggal_berdiri_perusahaan': forms.TextInput(
                attrs={'type': 'date'}),
            'tanggal_perubahan': forms.TextInput(
                attrs={'type': 'date'},),
        }


class FormDataPerorangan(ModelForm):
    class Meta:
        model = VendorPerorangan
        fields = (
            'nama_perorangan',
            'nama_singkatan',
            'alamat_perorangan',
            'kota_perorangan',
            'kode_pos_perorangan',
            'nomor_ktp',
            'tanggal_berakhir',
            'npwp_perorangan',
            'nomor_telepon',
            'nomor_fax',
            'email',
            'nomor_hp',
        )
        labels = {
            'nomor_ktp': 'Nomor KTP / SIM / Passport',
            'tanggal_berakhir': 'Tanggal Berakhir (jika ada)',
        }
        widgets = {
            'kota_perorangan': forms.Select(
                attrs={'class': 'select2bs4'},
            ),
            'tanggal_berakhir': forms.TextInput(
                attrs={'type': 'date'},),
        }


class FormAlamatPerusahaan(ModelForm):
    class Meta:
        model = AlamatVendorPerusahaan
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        fields = (
            'alamat_kantor',
            'kota_kantor',
            'kode_pos_kantor',
            'alamat_npwp',
            'kota_npwp',
            'kode_pos_npwp',
            'alamat_gudang',
            'kota_gudang',
            'kode_pos_gudang',
        )
        widgets = {
            'kota_kantor': forms.Select(
                attrs={'class': 'select2bs4'},
            ),
            'kota_npwp': forms.Select(
                attrs={'class': 'select2bs4'},
            ),
            'kota_gudang': forms.Select(
                attrs={'class': 'select2bs4'},
            ),
        }


class FormTeleponPerusahaan(ModelForm):
    class Meta:
        model = VendorPerusahaan
        fields = (
            'nomor_telepon',
            'nomor_fax',
        )


class FormPenanggungjawabPerusahaan(ModelForm):
    class Meta:
        model = PenanngungjawabVendorPerusahaan
        fields = (
            'nama_pemilik',
            'email_pemilik',
            'hp_pemilik',
            'nama_pimpinan',
            'email_pimpinan',
            'hp_pimpinan',
            'ktp_pimpinan',
            'nama_marketing',
            'email_marketing',
            'hp_marketing',
        )


class FormDokumenPerusahaan(ModelForm):
    class Meta:
        model = FileVendorPerusahaan
        fields = (
            'nama_file',
            'jenis_file',
        )


class FormBank(ModelForm):
    class Meta:
        model = BankVendorPerusahaan
        fields = (
            'nama',
            'cabang',
            'alamat',
            'kota',
            'negara',
            'nomor_rekening',
            'nama_nasabah',
            'mata_uang',
        )

class FormSegmentasiPerusahaan(ModelForm):
    class Meta:
        model = SegmentasiPerusahaan
        fields = (
            'kbli',
        )

class FormTenagaAhliPerusahaan(ModelForm):
    class Meta:
        model = TenagaAhliPerusahaan
        fields = (
            'nama_tenaga_ahli',
            'tanggal_lahir',
            'pendidikan',
            'pengalaman',
            'profesi',
            'dokumen',
        )

        widgets = {
            'pendidikan': forms.Select(
                attrs={'class': 'select2bs4'},
            ),
            'tanggal_lahir': forms.TextInput(
                attrs={'type': 'date'},),
        }

class FormPeralatanPerusahaan(ModelForm):
    class Meta:
        model = PeralatanPerusahaan
        fields = (
            'jenis',
            'jumlah',
            'kapasitas',
            'merk',
            'tahun_pembuatan',
            'lokasi',
            'bukti_kepemilikan',
            'dokumen_bukti_kepemilikan',
        )

        widgets = {
            'kondisi': forms.Select(
                attrs={'class': 'select2bs4'},
            )
        }


class FormPengalamanPerusahaan(ModelForm):
    class Meta:
        model = PengalamanPerusahaan
        fields = (
            'p_nama',
            'p_lokasi',
            'p_bidang_usaha',
            'p_mulai_kerjasama',
            'p_nilai_kontrak',
            'p_mata_uang',
            'p_dokumen',
        )

        labels = {
            'p_nama': 'Nama Pekerjaan',
            'p_lokasi': 'Lokasi Pekerjaan',
            'p_bidang_usaha': 'Bidang Usaha',
            'p_mulai_kerjasama': 'Mulai Kerjasama',
            'p_nilai_kontrak': 'Nilai Kontrak',
            'p_mata_uang': 'Mata Uang',
            'p_dokumen': 'Bukti Kerjasama',
        }

        widgets = {
            'p_mata_uang': forms.Select(
                attrs={'class': 'select2bs4'},
            ),
            'p_mulai_kerjasama': forms.TextInput(
                attrs={'type': 'date'},),
        }


class FormPengalamanMitraKerjaPerusahaan(ModelForm):
    class Meta:
        model = PengalamanMitraKerjaPerusahaan
        fields = (
            'm_nama',
            'm_lokasi',
            'm_bidang_usaha',
            'm_mulai_kerjasama',
            'm_nilai_kontrak',
            'm_mata_uang',
            'm_dokumen',
        )

        labels = {
            'm_nama': 'Nama Pekerjaan',
            'm_lokasi': 'Lokasi Pekerjaan',
            'm_bidang_usaha': 'Bidang Usaha',
            'm_mulai_kerjasama': 'Mulai Kerjasama',
            'm_nilai_kontrak': 'Nilai Kontrak',
            'm_mata_uang': 'Mata Uang',
            'm_dokumen': 'Bukti Kerjasama',
        }

        widgets = {
            'm_mata_uang': forms.Select(
                attrs={'class': 'select2bs4'},
            ),
            'm_mulai_kerjasama': forms.TextInput(
                attrs={'type': 'date'},),
        }

class FormPekerjaanBerjalanPerusahaan(ModelForm):
    class Meta:
        model = PekerjaanBerjalanPerusahaan
        fields = (
            'b_nama',
            'b_lokasi',
            'b_bidang_usaha',
            'b_mulai_kerjasama',
            'b_nilai_kontrak',
            'b_mata_uang',
            'b_dokumen',
        )

        labels = {
            'b_nama' : 'Nama Pekerjaan',
            'b_lokasi' : 'Lokasi Pekerjaan',
            'b_bidang_usaha' : 'Bidang Usaha',
            'b_mulai_kerjasama' : 'Mulai Kerjasama',
            'b_nilai_kontrak' : 'Nilai Kontrak',
            'b_mata_uang' : 'Mata Uang',
            'b_dokumen' : 'Bukti Kerjasama',
        }

        widgets = {
            'b_mata_uang': forms.Select(
                attrs={'class': 'select2bs4'},
            ),
            'b_mulai_kerjasama': forms.TextInput(
                attrs={'type': 'date'},
            ),
        }
