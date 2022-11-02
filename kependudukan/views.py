from dataclasses import field
from django.shortcuts import render
from django.http import JsonResponse
from kependudukan.models import Kelurahan, RequestKTP
from kependudukan.forms import RequestKTPForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
from .models import KELURAHAN_BY_KECAMATAN_CHOICES


# Create your views here.
def show_kependudukan(request):
    context = {
        'beji' : Kelurahan.objects.filter(kecamatan="Beji"),
        'pancoran_mas' : Kelurahan.objects.filter(kecamatan="Pancoran Mas"),
        'cipayung' : Kelurahan.objects.filter(kecamatan="Cipayung"),
        'sukmajaya' : Kelurahan.objects.filter(kecamatan="Sukmajaya"),
        'cilodong' : Kelurahan.objects.filter(kecamatan="Cilodong"),
        'limo' : Kelurahan.objects.filter(kecamatan="Limo"),
        'cinere' : Kelurahan.objects.filter(kecamatan="Cinere"),
        'cimanggis' : Kelurahan.objects.filter(kecamatan="Cimanggis"),
        'tapos' : Kelurahan.objects.filter(kecamatan="Tapos"),
        'sawangan' : Kelurahan.objects.filter(kecamatan="Sawangan"),
        'bojong_sari' : Kelurahan.objects.filter(kecamatan="Bojong Sari"),
    }
    return render(request, "kependudukan.html", context)

def add_request(request):
    form = RequestKTPForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        ktp = form.save()
        ktp.user=request.user
        ktp.save()
        # kecamatan = request.POST.get('kecamatan')
        # kelurahan = request.POST.get('kelurahan')
        # permohonan = request.POST.get('permohonan')

        # nama_lengkap = request.POST.get('nama_lengkap')
        # nomor_kk = request.POST.get('nomor_kk')
        # nik = request.POST.get('nik')
        # alamat = request.POST.get('alamat')

        # rt = request.POST.get('rt')
        # rw = request.POST.get('rw')
        # kode_pos = request.POST.get('kode_pos')

        # nomor_hp = request.POST.get('nomor_hp')

        # schedule_date = request.POST.get('schedule_date')
        # schedule_time = request.POST.get('schedule_time')

        # ktp = RequestKTP.objects.create(
        #     kecamatan=kecamatan, 
        #     kelurahan=kelurahan,
        #     permohonan=permohonan,
        #     nama_lengkap=nama_lengkap,
        #     nomor_kk=nomor_kk,
        #     nik=nik,
        #     alamat=alamat,
        #     rt=rt,
        #     rw=rw,
        #     kode_pos=kode_pos,
        #     nomor_hp=nomor_hp,
        #     schedule_date=schedule_date,
        #     schedule_time=schedule_time
        #     )
        return serialize_ktp([ktp])
        

@login_required(login_url='/login/')
def show_request_ktp(request):
    form = RequestKTPForm()
    form_fields = list(field_name for field_name in form.fields)

    context = {
        'form' : RequestKTPForm(),
        'form_fields' : form_fields,
        'requests' : RequestKTP.objects.filter(user=request.user),
    }
    return render(request, "request_ktp.html", context)

def show_json(request):
    data = Kelurahan.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
def show_request_ktp_json(request):
    data = RequestKTP.objects.filter(user=request.user)
    return serialize_ktp(data)

def serialize_ktp(ktps):
    data = []
    for ktp in ktps:
        data.append(
            {
                "pk": ktp.pk,
                "fields": {
                    "requested_at" : datetime.datetime.strftime(timezone.localtime(ktp.requested_at), "%d-%m-%Y %H:%M:%S"),
                    "provinsi" : ktp.provinsi,
                    "kota" : ktp.kota,
                    "kecamatan" : ktp.kecamatan,
                    "kelurahan" : ktp.kelurahan,
                    "permohonan" : ktp.permohonan,

                    "nama_lengkap" : ktp.nama_lengkap,
                    "nomor_kk" : ktp.nomor_kk,
                    "nik" : ktp.nik,
                    "alamat" : ktp.alamat,

                    "rt" : ktp.rt,
                    "rw" : ktp.rw,
                    "kode_pos" : ktp.kode_pos,

                    "nomor_hp" : ktp.nomor_hp,

                    "schedule_date" : ktp.schedule_date,
                    "schedule_time" : ktp.schedule_time,
                },
            }
        )
    return JsonResponse(data, safe=False)

def get_kelurahan(request):
    kecamatan = request.GET.get("kecamatan")
    kelurahan_list = KELURAHAN_BY_KECAMATAN_CHOICES[kecamatan]
    res = []
    for kelurahan in kelurahan_list:
        res.append(kelurahan[0])
    return JsonResponse(res, safe=False)
    