from django.core import serializers
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .forms import *
from .models import *
from administrator.models import Disclaimer as admindisclaimer
from django.http import JsonResponse, HttpResponse

# Create your views here.


def get_tipe_perusahaan(loggeduser):
    tipe_perusahaan = VendorGeneral.objects.get(
        user=loggeduser, disclaimer=True).tipe_perusahaan
    return tipe_perusahaan

@login_required(login_url='/front/login')
def summaryDataVendor(request):
    loggeduser = request.user
    tipe_perusahaan = get_tipe_perusahaan(loggeduser)
    if tipe_perusahaan == 'PO':
        if VendorPerorangan.objects.filter(user=loggeduser).exists():
            data_perorangan = VendorPerorangan.objects.get(user=loggeduser)
            datab = BankVendorPerusahaan.objects.filter(user=loggeduser)
            datad = MasterDokumen.objects.filter(for_perorangan=1)
            datad7 = FileVendorPerusahaan.objects.filter(user=loggeduser)
            datac7 = SegmentasiPerusahaan.objects.filter(
                user=loggeduser).values('kbli__kbli', 'kbli__judul')
            datac8 = TenagaAhliPerusahaan.objects.filter(user=loggeduser)
            datac10 = PeralatanPerusahaan.objects.filter(user=loggeduser)
            datac91 = PengalamanPerusahaan.objects.filter(user=loggeduser)
            datac92 = PengalamanMitraKerjaPerusahaan.objects.filter(
                user=loggeduser)
            datac93 = PekerjaanBerjalanPerusahaan.objects.filter(user=loggeduser)
            return render(request, 'summary-data-vendor.html', {'data_perorangan': data_perorangan, 'datab': datab,
            'datac7':datac7, 'datad':datad, 'datad7':datad7, 'datac8': datac8, 'datac91':datac91,'datac92':datac92,
            'datac93':datac93,'datac10':datac10})

    else:
        data_perorangan = 'akwowakoawk'


def dataVendor(request):
    loggeduser = request.user
    datac1 = VendorGeneral.objects.filter(user=loggeduser).exists()
    datac2 = VendorGeneral.objects.filter(
        user=loggeduser, disclaimer=True).exists()
    if datac1 and datac2:
        tipe_perusahaan = get_tipe_perusahaan(loggeduser)
        formc3 = ''
        datac3 = ''
        if tipe_perusahaan == 'PE' or tipe_perusahaan == 'IN':
            formc3 = FormDataPerusahaan()
            datac3 = VendorPerusahaan.objects.filter(user=loggeduser)
            datad = MasterDokumen.objects.filter(for_perusahaan=1)
            datad7required = MasterDokumen.objects.filter(
                for_perusahaan=True, is_required=True)
        elif tipe_perusahaan == 'PO':
            formc3 = FormDataPerorangan()
            datac3 = VendorPerorangan.objects.filter(user=loggeduser)
            datad = MasterDokumen.objects.filter(for_perorangan=1)
            datad7required = MasterDokumen.objects.filter(
                for_perorangan=True, is_required=True)
        formc4 = FormAlamatPerusahaan()
        formc5 = FormTeleponPerusahaan()
        formc6 = FormPenanggungjawabPerusahaan()
        formc8 = FormTenagaAhliPerusahaan()
        formc91 = FormPengalamanPerusahaan()
        formc92 = FormPengalamanMitraKerjaPerusahaan()
        formc93 = FormPekerjaanBerjalanPerusahaan()
        formd = FormDokumenPerusahaan()
        formb = FormBank()

        
        datac4 = AlamatVendorPerusahaan.objects.filter(user=loggeduser)
        datac5 = VendorPerusahaan.objects.filter(user=loggeduser, nomor_telepon__exact='').exists
        datac6 = PenanngungjawabVendorPerusahaan.objects.filter(
            user=loggeduser)
        datac7 = SegmentasiPerusahaan.objects.filter(
            user=loggeduser).values('kbli__kbli', 'kbli__judul')
        datac8 = TenagaAhliPerusahaan.objects.filter(user=loggeduser)
        datac91 = PengalamanPerusahaan.objects.filter(user=loggeduser)
        datac92 = PengalamanMitraKerjaPerusahaan.objects.filter(user=loggeduser)
        datac93 = PekerjaanBerjalanPerusahaan.objects.filter(user=loggeduser)
        datab = BankVendorPerusahaan.objects.filter(user=loggeduser)
        datad7 = FileVendorPerusahaan.objects.filter(user=loggeduser)
        dalamverifikasi = VendorGeneral.objects.filter(user=loggeduser, dalam_verifikasi=True).exists()
        return render(request, 'data-vendor.html', {'formc3': formc3,
                                                    'formc4': formc4, 'formc5': formc5, 'formc6': formc6,
                                                    'formc8': formc8, 'formc91': formc91, 'formc92': formc92, 
                                                    'formc93': formc93, 'formd': formd, 'formb': formb,

                                                    'datac1': datac1, 'datac2': datac2, 'datac3': datac3,
                                                    'datac4': datac4, 'datac5': datac5, 'datac6': datac6,
                                                    'datac7': datac7, 'datac8': datac8, 'datac91': datac91,
                                                    'datac92': datac92, 'datac93': datac93,
                                                    'datab': datab, 'datad': datad, 'datad7': datad7, 'datad7required': datad7required,
                                                    'dalamverifikasi':dalamverifikasi, 'tipe_perusahaan':tipe_perusahaan})
    else:
        form = FormTipePerusahaan()
        formc2 = FormDisclaimer()
        datac21 = admindisclaimer.objects.get(id=1)
        return render(request, 'data-vendor.html', {'form': form, 'formc2': formc2,

                                                    'datac1': datac1, 'datac2': datac2, 'datac21': datac21})


def dataVendorC1(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormTipePerusahaan(request.POST)
        # check whether it's valid:
        if form.is_valid():
            tipe_perusahaan = form.cleaned_data.get('tipe_perusahaan')
            user_id = request.user.id
            obj, created = VendorGeneral.objects.update_or_create(
                user_id=user_id,
                defaults={
                    'tipe_perusahaan': tipe_perusahaan,
                    'disclaimer': False
                }
            )
            ser_instance = serializers.serialize('json', [obj, ])
            print('ok1')
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            print('notok')
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorC2(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormDisclaimer(request.POST)
        # check whether it's valid:
        if form.is_valid():
            disclaimer = form.cleaned_data.get('disclaimer')
            user_id = request.user.id
            obj, created = VendorGeneral.objects.update_or_create(
                user_id=user_id,
                defaults={
                    'disclaimer': disclaimer
                }
            )
            ser_instance = serializers.serialize('json', [obj, ])
            print('ok1')
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            print('notok')
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorC3(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        loggeduser = request.user
        print(request.POST)
        tipe_perusahaan = get_tipe_perusahaan(loggeduser)
        if tipe_perusahaan == 'PO':
            form = FormDataPerorangan(request.POST)
            # check whether it's valid:
            if form.is_valid():
                nama_perorangan = form.cleaned_data.get('nama_perorangan')
                nama_singkatan = form.cleaned_data.get('nama_singkatan')
                alamat_perorangan = form.cleaned_data.get('alamat_perorangan')
                kota_perorangan = form.cleaned_data.get('kota_perorangan')
                kode_pos_perorangan = form.cleaned_data.get(
                    'kode_pos_perorangan')
                nomor_ktp = form.cleaned_data.get('nomor_ktp')
                tanggal_berakhir = form.cleaned_data.get('tanggal_berakhir')
                npwp_perorangan = form.cleaned_data.get(
                    'npwp_perorangan')
                nomor_telepon = form.cleaned_data.get(
                    'nomor_telepon')
                nomor_fax = form.cleaned_data.get('nomor_fax')
                email = form.cleaned_data.get('email')
                nomor_hp = form.cleaned_data.get('nomor_hp')
                
                user_id = request.user.id
                obj, created = VendorPerorangan.objects.update_or_create(
                    user_id=user_id,
                    defaults={
                        'nama_perorangan': nama_perorangan,
                        'nama_singkatan': nama_singkatan,
                        'alamat_perorangan': alamat_perorangan,
                        'kota_perorangan': kota_perorangan,
                        'kode_pos_perorangan': kode_pos_perorangan,
                        'nomor_ktp': nomor_ktp,
                        'tanggal_berakhir': tanggal_berakhir,
                        'npwp_perorangan': npwp_perorangan,
                        'nomor_telepon': nomor_telepon,
                        'nomor_fax': nomor_fax,
                        'email': email,
                        'nomor_hp': nomor_hp,
                    }
                )
                
                data = VendorPerorangan.objects.filter(
                    user=loggeduser).values('nama_perorangan', 'nama_singkatan', 'alamat_perorangan',
                                            'kota_perorangan__kota', 'kode_pos_perorangan', 'nomor_ktp',
                                            'tanggal_berakhir', 'npwp_perorangan', 'nomor_telepon', 'nomor_fax',
                                            'email', 'nomor_hp')
                ser_instance = list(data)
                return JsonResponse(ser_instance, status=200, safe=False)

            else:
                # some form errors occured.
                return JsonResponse(form.errors, status=400)
        else:
            # create a form instance and populate it with data from the request:
            form = FormDataPerusahaan(request.POST)
            # check whether it's valid:
            if form.is_valid():
                tipe_pkp = form.cleaned_data.get('tipe_pkp')
                no_pkp = form.cleaned_data.get('no_pkp')
                kualifikasi = form.cleaned_data.get('kualifikasi')
                grade = form.cleaned_data.get('grade')
                nama_perusahaan = form.cleaned_data.get('nama_perusahaan')
                bentuk_perusahaan = form.cleaned_data.get('bentuk_perusahaan')
                npwp_perusahaan = form.cleaned_data.get('npwp_perusahaan')
                no_akte_perusahaan = form.cleaned_data.get('no_akte_perusahaan')
                tanggal_berdiri_perusahaan = form.cleaned_data.get(
                    'tanggal_berdiri_perusahaan')
                tanggal_perubahan = form.cleaned_data.get('tanggal_perubahan')
                nama_singkatan = form.cleaned_data.get('nama_singkatan')
                website = form.cleaned_data.get('website')
                user_id = request.user.id
                obj, created = VendorPerusahaan.objects.update_or_create(
                    user_id=user_id,
                    defaults={
                        'tipe_pkp': tipe_pkp,
                        'no_pkp': no_pkp,
                        'kualifikasi': kualifikasi,
                        'grade': grade,
                        'nama_perusahaan': nama_perusahaan,
                        'bentuk_perusahaan': bentuk_perusahaan,
                        'npwp_perusahaan': npwp_perusahaan,
                        'no_akte_perusahaan': no_akte_perusahaan,
                        'tanggal_berdiri_perusahaan': tanggal_berdiri_perusahaan,
                        'tanggal_perubahan': tanggal_perubahan,
                        'nama_singkatan': nama_singkatan,
                        'website': website,
                    }
                )
                data = VendorPerusahaan.objects.filter(
                    user=loggeduser).values('tipe_pkp', 'no_pkp', 'kualifikasi',
                                            'grade', 'nama_perusahaan', 'bentuk_perusahaan',
                                            'npwp_perusahaan', 'no_akte_perusahaan', 'tanggal_berdiri_perusahaan', 'tanggal_perubahan',
                                            'nama_singkatan', 'website')
                ser_instance = list(data)
                return JsonResponse(ser_instance, status=200, safe=False)
            else:
                # some form errors occured.
                return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorC4(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormAlamatPerusahaan(request.POST)
        print(request.POST)
        # check whether it's valid:
        if form.is_valid():
            alamat_kantor = form.cleaned_data.get('alamat_kantor')
            kota_kantor = form.cleaned_data.get('kota_kantor')
            kode_pos_kantor = form.cleaned_data.get('kode_pos_kantor')

            alamat_npwp = form.cleaned_data.get('alamat_npwp')
            kota_npwp = form.cleaned_data.get('kota_npwp')
            kode_pos_npwp = form.cleaned_data.get('kode_pos_npwp')

            alamat_gudang = form.cleaned_data.get('alamat_gudang')
            kota_gudang = form.cleaned_data.get('kota_gudang')
            kode_pos_gudang = form.cleaned_data.get('kode_pos_gudang')

            user_id = request.user.id

            obj, created = AlamatVendorPerusahaan.objects.update_or_create(
                user_id=user_id,
                defaults={
                    'alamat_kantor': alamat_kantor,
                    'kota_kantor': kota_kantor,
                    'kode_pos_kantor': kode_pos_kantor,

                    'alamat_npwp': alamat_npwp,
                    'kota_npwp': kota_npwp,
                    'kode_pos_npwp': kode_pos_npwp,

                    'alamat_gudang': alamat_gudang,
                    'kota_gudang': kota_gudang,
                    'kode_pos_gudang': kode_pos_gudang,
                }
            )
            ser_instance = serializers.serialize('json', [obj, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorC5(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormTeleponPerusahaan(request.POST)
        print(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nomor_telepon = form.cleaned_data.get('nomor_telepon')
            nomor_fax = form.cleaned_data.get('nomor_fax')
            user_id = request.user.id

            obj, created = VendorPerusahaan.objects.update_or_create(
                user_id=user_id,
                defaults={
                    'nomor_telepon': nomor_telepon,
                    'nomor_fax': nomor_fax,
                }
            )
            ser_instance = serializers.serialize('json', [obj, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            # return JsonResponse({"error": dict(form.errors.items())}, status=400)
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorC6(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormPenanggungjawabPerusahaan(request.POST)
        print(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nama_pemilik = form.cleaned_data.get('nama_pemilik')
            email_pemilik = form.cleaned_data.get('email_pemilik')
            hp_pemilik = form.cleaned_data.get('hp_pemilik')

            nama_pimpinan = form.cleaned_data.get('nama_pimpinan')
            email_pimpinan = form.cleaned_data.get('email_pimpinan')
            hp_pimpinan = form.cleaned_data.get('hp_pimpinan')
            ktp_pimpinan = form.cleaned_data.get('ktp_pimpinan')

            nama_marketing = form.cleaned_data.get('nama_marketing')
            email_marketing = form.cleaned_data.get('email_marketing')
            hp_marketing = form.cleaned_data.get('hp_marketing')

            user_id = request.user.id

            obj, created = PenanngungjawabVendorPerusahaan.objects.update_or_create(
                user_id=user_id,
                defaults={
                    'nama_pemilik': nama_pemilik,
                    'email_pemilik': email_pemilik,
                    'hp_pemilik': hp_pemilik,

                    'nama_pimpinan': nama_pimpinan,
                    'email_pimpinan': email_pimpinan,
                    'hp_pimpinan': hp_pimpinan,
                    'ktp_pimpinan': ktp_pimpinan,

                    'nama_marketing': nama_marketing,
                    'email_marketing': email_marketing,
                    'hp_marketing': hp_marketing,
                }
            )
            ser_instance = serializers.serialize('json', [obj, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            # return JsonResponse({"error": dict(form.errors.items())}, status=400)
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorC7(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormSegmentasiPerusahaan(request.POST)
        print(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user_id = request.user.id
            loggeduser = request.user
            obj = form.save(commit=False)
            obj.user_id = user_id
            obj.save()
            data = SegmentasiPerusahaan.objects.filter(
                user=loggeduser).values('kbli__kbli', 'kbli__judul')
            ser_instance = list(data)
            return JsonResponse(ser_instance, status=200, safe=False)
        else:
            # some form errors occured.
            # return JsonResponse({"error": dict(form.errors.items())}, status=400)
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorC8(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormTenagaAhliPerusahaan(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            user_id = request.user.id
            loggeduser = request.user
            obj = form.save(commit=False)
            obj.user_id = user_id
            obj.save()
            data = TenagaAhliPerusahaan.objects.filter(user=loggeduser).values(
                'nama_tenaga_ahli', 'tanggal_lahir', 'pendidikan', 'pengalaman', 'profesi', 'dokumen')
            ser_instance = list(data)
            return JsonResponse(ser_instance, status=200, safe=False)
        else:
            # some form errors occured.
            # return JsonResponse({"error": dict(form.errors.items())}, status=400)
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorC91(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormPengalamanPerusahaan(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            user_id = request.user.id
            loggeduser = request.user
            obj = form.save(commit=False)
            obj.user_id = user_id
            obj.save()
            data = PengalamanPerusahaan.objects.filter(user=loggeduser).values(
                'p_nama', 'p_lokasi', 'p_bidang_usaha', 'p_mulai_kerjasama', 'p_nilai_kontrak', 'p_mata_uang', 'p_dokumen')
            ser_instance = list(data)
            return JsonResponse(ser_instance, status=200, safe=False)
        else:
            # some form errors occured.
            # return JsonResponse({"error": dict(form.errors.items())}, status=400)
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorC92(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormPengalamanMitraKerjaPerusahaan(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            user_id = request.user.id
            loggeduser = request.user
            obj = form.save(commit=False)
            obj.user_id = user_id
            obj.save()
            data = PengalamanMitraKerjaPerusahaan.objects.filter(user=loggeduser).values(
                'm_nama', 'm_lokasi', 'm_bidang_usaha', 'm_mulai_kerjasama', 'm_nilai_kontrak', 'm_mata_uang', 'm_dokumen')
            ser_instance = list(data)
            return JsonResponse(ser_instance, status=200, safe=False)
        else:
            # some form errors occured.
            # return JsonResponse({"error": dict(form.errors.items())}, status=400)
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorC93(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormPekerjaanBerjalanPerusahaan(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            user_id = request.user.id
            loggeduser = request.user
            obj = form.save(commit=False)
            obj.user_id = user_id
            obj.save()
            data = PekerjaanBerjalanPerusahaan.objects.filter(user=loggeduser).values(
                'b_nama', 'b_lokasi', 'b_bidang_usaha', 'b_mulai_kerjasama', 'b_nilai_kontrak', 'b_mata_uang', 'b_dokumen')
            ser_instance = list(data)
            return JsonResponse(ser_instance, status=200, safe=False)
        else:
            # some form errors occured.
            # return JsonResponse({"error": dict(form.errors.items())}, status=400)
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorB(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormBank(request.POST)
        print(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user_id = request.user.id
            loggeduser = request.user
            obj = form.save(commit=False)
            obj.user_id = user_id
            obj.save()
            databank = BankVendorPerusahaan.objects.filter(
                user=loggeduser).values('nama', 'cabang', 'nomor_rekening')
            # ser_instance = serializers.serialize('json', databank)
            ser_instance = list(databank)
            return JsonResponse(ser_instance, status=200, safe=False)
        else:
            # some form errors occured.
            # return JsonResponse({"error": dict(form.errors.items())}, status=400)
            return JsonResponse(form.errors, status=400)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)


def dataVendorD(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormDokumenPerusahaan(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            user_id = request.user.id
            loggeduser = request.user
            nama_file = form.cleaned_data.get('nama_file')
            jenis_file = form.cleaned_data.get('jenis_file')
            # tanggal_berakhir = form.cleaned_data.get('tanggal_berakhir')
            tanggal_berakhir = request.POST.get('tanggal_berakhir')
            user_id = request.user.id

            obj, created = FileVendorPerusahaan.objects.update_or_create(
                user_id=user_id,
                jenis_file=jenis_file,
                defaults={
                    'nama_file': nama_file,
                    'tanggal_berakhir':tanggal_berakhir,
                }
            )
            data = FileVendorPerusahaan.objects.filter(
                user=loggeduser).values('nama_file', 'jenis_file', 'updated_at')
            ser_instance = list(data)
            return JsonResponse(ser_instance, status=200, safe=False)
        else:
            # some form errors occured.
            # return JsonResponse({"error": dict(form.errors.items())}, status=400)
            error = form.errors
            print(error)
            return JsonResponse(error, status=400, safe=False)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse(form.errors, status=400)


def jsonGetKotabyPropinsi(request, id=id):
    data = MasterKota.objects.filter(provinsi=id).values()
    return JsonResponse(list(data), safe=False)


def jsonGetPropinsi(request):
    data = MasterProvinsi.objects.all().values()
    return JsonResponse(list(data), safe=False)


def jsonGetKbli(request):
    data = MasterKbli.objects.filter(kbli__length__gt=3).values()
    return JsonResponse(list(data), safe=False)


def jsonGetDokumen(request):
    loggeduser = request.user
    data = FileVendorPerusahaan.objects.filter(user=loggeduser).values()
    return JsonResponse(list(data), safe=False)

def jsonCekPkp(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        no_pkp = request.POST['no_pkp']
        existance = VendorPerusahaan.objects.filter(
            no_pkp = no_pkp).exists()
        result = ''
        print(existance)
        if existance:
            result = 'exist'
        else:
            result = 'not exist'
        return JsonResponse({'result':result}, status=200, safe=False)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)

def jsonCekNpwp(request):
    # if this is a POST request we need to process the form data
    loggeduser = request.user
    tipe_perusahaan = get_tipe_perusahaan(loggeduser)
    if tipe_perusahaan == 'PO':
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            no_npwp = request.POST['no_npwp']
            print(request.POST)
            existance = VendorPerorangan.objects.exclude(user=loggeduser).filter(
                npwp_perorangan=no_npwp).exists()
            result = ''
            print(existance)
            if existance:
                result = 'exist'
            else:
                result = 'not exist'
            return JsonResponse({'result': result}, status=200, safe=False)
    else:
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            no_npwp = request.POST['no_npwp']
            print(request.POST)
            existance = VendorPerusahaan.objects.filter(
                npwp_perusahaan=no_npwp).exists()
            result = ''
            print(existance)
            if existance:
                result = 'exist'
            else:
                result = 'not exist'
            return JsonResponse({'result':result}, status=200, safe=False)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)

def verifyToAdministrator(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        submit = request.POST['submit']
        if submit == 'true':
            result = False
            loggeduser = request.user
            reason = ""
            data_perorangan = ""
            data_perusahaan = ""
            if get_tipe_perusahaan(loggeduser) == 'PO':
                data_perorangan = VendorPerorangan.objects.filter(user=loggeduser).exists()
                if not data_perusahaan:
                    reason += "Data Perorangan, "
            else:
                data_perusahaan = VendorPerusahaan.objects.filter(user=loggeduser).exists()
                if not data_perusahaan:
                    reason += "Data Perusahaan, "
                alamat = AlamatVendorPerusahaan.objects.filter(
                    user=loggeduser).exists()
                if not alamat:
                    reason += "Alamat Perusahaan, "
                telepon = not VendorPerusahaan.objects.filter(
                    user=loggeduser, nomor_telepon__exact='').exists()
                if not telepon:
                    reason += "Telepon, "
                penanggungjawab = PenanngungjawabVendorPerusahaan.objects.filter(
                    user=loggeduser).exists()
                if not penanggungjawab:
                    reason += "Penanggungjawab, "
            dokumen_administrasi = (
                FileVendorPerusahaan.objects.filter(user=loggeduser).count() >= MasterDokumen.objects.filter(for_perorangan=True, is_required=True).count())
            if not dokumen_administrasi:
                reason += "Dokumen Administrasi, "
            bank = BankVendorPerusahaan.objects.filter(user=loggeduser).exists()
            if not bank:
                reason += "Bank, "
            segmentasi = SegmentasiPerusahaan.objects.filter(user=loggeduser).exists()
            if not segmentasi:
                reason += "Segmentasi, "
            tenaga_ahli = TenagaAhliPerusahaan.objects.filter(
                user=loggeduser).exists()
            if not tenaga_ahli:
                reason += "Tenaga Ahli, "
            pengalaman = PengalamanPerusahaan.objects.filter(
                user=loggeduser).exists()
            if not pengalaman:
                reason += "Pengalaman"
            result = ((data_perusahaan and alamat and telepon and penanggungjawab)
                      or data_perorangan) and dokumen_administrasi and bank and segmentasi and tenaga_ahli and pengalaman
            # print(data_perusahaan , alamat, telepon , penanggungjawab , dokumen_administrasi , bank ,segmentasi , tenaga_ahli , pengalaman)
            if result:
                obj = VendorGeneral.objects.get(user=loggeduser)
                obj.dalam_verifikasi = True
                obj.save()
                return JsonResponse({'result': 'OK'}, status=200, safe=False)
            else:
                return JsonResponse({'result': 'Not OK', 'reason' : 'Mohon periksa bagian '+reason}, status=200, safe=False)

    # if a GET (or any other method) we'll create a blank form
    return JsonResponse({"error": ""}, status=400)

    data = FileVendorPerusahaan.objects.filter(user=loggeduser).values()
    return JsonResponse(list(data), safe=False)


def test(request):
    return render(request, 'testjson.html')

def fakejson(request):
    form = FormDokumenPerusahaan(request.POST, request.FILES)
    if form.is_valid():
        return JsonResponse(ser_instance, status=200, safe=False)
    else:
        error = form.errors
        # return JsonResponse(error, status=400, safe=False)
        return JsonResponse(error, status=400)
