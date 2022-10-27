import datetime
from django import forms
from kependudukan.models import TIMESLOT_LIST

# iterables
KECAMATAN_CHOICES = (
    ("Beji", "Beji"),
    ("Pancoran Mas", "Pancoran Mas"),
    ("Cipayung", "Cipayung"),
    ("Sukmajaya", "Sukmajaya"),
    ("Cilodong", "Cilodong"),
    ("Limo", "Limo"),
    ("Cinere", "Cinere"),
    ("Cimanggis", "Cimanggis"),
    ("Tapos", "Tapos"),
    ("Sawangan", "Sawangan"),
    ("Bojong Sari", "Bojong Sari")
)

KELURAHAN_CHOICES = (
    # Beji
    ("Beji", "Beji"),("Beji Timur", "Beji Timur"), ("Kemiri Muka", "Kemiri Muka"), 
    ("Pondok Cina", "Pondok Cina"), ("Kukusan", "Kukusan"), ("Tanah Baru", "Tanah Baru"),
    # Pancoran Mas
    ("Pancoran Mas", "Pancoran Mas"), ("Depok", "Depok"), ("Depok Jaya", "Depok Jaya"), 
    ("Rangkapan Jaya", "Rangkapan Jaya"), ("Rangkapan Jaya Baru", "Rangkapan Jaya Baru"), ("Mampang", "Mampang"), 
    # Cipayung
    ("Cipayung", "Cipayung"), ("Cipayung Jaya", "Cipayung Jaya"), ("Ratu Jaya", "Ratu Jaya"), 
    ("Bojong Pondok Terong", "Bojong Pondok Terong"), ("Pondok Jaya", "Pondok Jaya"), 
    # Sukamajaya
    ("Sukmajaya", "Sukmajaya"), ("Mekar Jaya", "Mekar Jaya"), ("Bakti Jaya", "Bakti Jaya"), 
    ("Abadi Jaya", "Abadi Jaya"), ("Tirta Jaya", "Tirta Jaya"), ("Cisalak", "Cisalak"), 
    # Cilodong
    ("Sukamaju", "Sukamaju"), ("Cilodong", "Cilodong"), ("Kalibaru", "Kalibaru"), 
    ("Kalimulya", "Kalimulya"), ("Jatimulya", "Jatimulya"), 
    # Limo
    ("Limo", "Limo"), ("Meruyung", "Meruyung"), ("Grogol", "Grogol"), ("Krukut", "Krukut"), 
    # Cinere
    ("Cinere", "Cinere"), ("Gandul", "Gandul"), ("Pengkalan Jati", "Pengkalan Jati"), 
    ("Pangkalan Jati Baru", "Pangkalan Jati Baru"), 
    # Cimanggis
    ("Cisalak Pasar", "Cisalak Pasar"), ("Mekarsari", "Mekarsari"), ("Tugu", "Tugu"), 
    ("Pasir Gunung Selatan", "Pasir Gunung Selatan"), ("Harjamukti", "Harjamukti"), 
    ("Curug", "Curug"), 
    # Tapos
    ("Tapos", "Tapos"), ("Leuwinanggung", "Leuwinanggung"), ("Sukatani", "Sukatani"), 
    ("Sukamaju Baru", "Sukamaju Baru"), ("Jatijajar", "Jatijajar"), ("Cilangkap", "Cilangkap"), 
    ("Cimpaeun", "Cimpaeun"), 
    # Sawangan
    ("Sawangan", "Sawangan"), ("Kedaung", "Kedaung"), ("Cinangka", "Cinangka"), 
    ("Sawangan Baru", "Sawangan Baru"), ("Bedahan", "Bedahan"), ("Pengasinan", "Pengasinan"), 
    ("Pasir Putih", "Pasir Putih"), 
    # Bojong Sari
    ("Bojong Sari", "Bojong Sari"), ("Bojongsari Baru", "Bojongsari Baru"), ("Serua", "Serua"), 
    ("Pondok Petir", "Pondok Petir"), ("Curug", "Curug"), ("Duren Mekar", "Duren Mekar"), ("Duren Seribu", "Duren Seribu"),
)

PERMOHONAN_CHOICES = (
    ("Baru", "Baru"),
    ("Penggantian", "Penggantian")
)

class DateInput(forms.DateInput):
    input_type = 'date'

# creating a form 
class RequestKTPForm(forms.Form):
    provinsi = "Jawa Barat"
    kota = "Depok"
    kecamatan = forms.ChoiceField(choices=KECAMATAN_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'name': 'kecamatan'}))
    kelurahan = forms.ChoiceField(choices=KELURAHAN_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'name': 'kelurahan'}))

    permohonan = forms.ChoiceField(choices=PERMOHONAN_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'name': 'permohonan'}))

    nama_lengkap = forms.CharField(max_length = 250, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'nama_lengkap'}))
    nomor_kk = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'nomor_kk'}))
    nik = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'nik'}))
    alamat = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'class': 'form-control', 'name': 'alamat'}))

    rt = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'rt'}))
    rw = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'rw'}))
    kode_pos = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'kode_pos'}))

    nomor_hp = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'nomor_hp'})) # untuk dihubungi dalam melakukan konfirmasi

    # jadwal = forms.CharField(max_length = 250, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'jadwal'}))
    # schedule
    schedule_date = forms.DateField(widget=DateInput, initial=datetime.date.today)
    schedule_time = forms.ChoiceField(choices=TIMESLOT_LIST, widget=forms.Select(attrs={'class': 'form-control', 'name': 'schedule_time'}))
    # schedule_date = request.POST.get('schedule_date')
    # schedule_time = request.POST.get('schedule_time')