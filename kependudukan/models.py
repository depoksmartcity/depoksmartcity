from random import choices
from django.db import models
from django.contrib.auth.models import User

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

KELURAHAN_BY_KECAMATAN_CHOICES = {
    "Beji" : [
    ("Beji", "Beji"),("Beji Timur", "Beji Timur"), ("Kemiri Muka", "Kemiri Muka"), 
    ("Pondok Cina", "Pondok Cina"), ("Kukusan", "Kukusan"), ("Tanah Baru", "Tanah Baru")],
    "Pancoran Mas" : [
    ("Pancoran Mas", "Pancoran Mas"), ("Depok", "Depok"), ("Depok Jaya", "Depok Jaya"), 
    ("Rangkapan Jaya", "Rangkapan Jaya"), ("Rangkapan Jaya Baru", "Rangkapan Jaya Baru"), ("Mampang", "Mampang")], 
    "Cipayung" :
    [("Cipayung", "Cipayung"), ("Cipayung Jaya", "Cipayung Jaya"), ("Ratu Jaya", "Ratu Jaya"), 
    ("Bojong Pondok Terong", "Bojong Pondok Terong"), ("Pondok Jaya", "Pondok Jaya")], 
    "Sukamajaya" :
    [("Sukmajaya", "Sukmajaya"), ("Mekar Jaya", "Mekar Jaya"), ("Bakti Jaya", "Bakti Jaya"), 
    ("Abadi Jaya", "Abadi Jaya"), ("Tirta Jaya", "Tirta Jaya"), ("Cisalak", "Cisalak")], 
    "Cilodong" :
    [("Sukamaju", "Sukamaju"), ("Cilodong", "Cilodong"), ("Kalibaru", "Kalibaru"), 
    ("Kalimulya", "Kalimulya"), ("Jatimulya", "Jatimulya")], 
    "Limo":
    [("Limo", "Limo"), ("Meruyung", "Meruyung"), ("Grogol", "Grogol"), ("Krukut", "Krukut")], 
    "Cinere" :
    [("Cinere", "Cinere"), ("Gandul", "Gandul"), ("Pengkalan Jati", "Pengkalan Jati"), 
    ("Pangkalan Jati Baru", "Pangkalan Jati Baru")], 
    "Cimanggis":
    [("Cisalak Pasar", "Cisalak Pasar"), ("Mekarsari", "Mekarsari"), ("Tugu", "Tugu"), 
    ("Pasir Gunung Selatan", "Pasir Gunung Selatan"), ("Harjamukti", "Harjamukti"), 
    ("Curug", "Curug")], 
    "Tapos" :
    [("Tapos", "Tapos"), ("Leuwinanggung", "Leuwinanggung"), ("Sukatani", "Sukatani"), 
    ("Sukamaju Baru", "Sukamaju Baru"), ("Jatijajar", "Jatijajar"), ("Cilangkap", "Cilangkap"), 
    ("Cimpaeun", "Cimpaeun")], 
    "Sawangan":
    [("Sawangan", "Sawangan"), ("Kedaung", "Kedaung"), ("Cinangka", "Cinangka"), 
    ("Sawangan Baru", "Sawangan Baru"), ("Bedahan", "Bedahan"), ("Pengasinan", "Pengasinan"), 
    ("Pasir Putih", "Pasir Putih")], 
    "Bojong Sari":
    [("Bojong Sari", "Bojong Sari"), ("Bojongsari Baru", "Bojongsari Baru"), ("Serua", "Serua"), 
    ("Pondok Petir", "Pondok Petir"), ("Curug", "Curug"), ("Duren Mekar", "Duren Mekar"), ("Duren Seribu", "Duren Seribu")]
}

PERMOHONAN_CHOICES = (
    ("Baru", "Baru"),
    ("Penggantian", "Penggantian")
)

TIMESLOT_LIST = (
        ('08:00 - 08:15', '08:00 - 08:15'),
        ('08:15 - 08:30', '08:15 - 08:30'),
        ('08:30 - 08:45', '08:30 - 08:45'),
        ('08:45 - 09.00', '08:45 - 09.00'),
        ('09:00 - 09:15', '09:00 - 09:15'),
        ('09:15 - 09:30', '09:15 - 09:30'),
        ('09:30 - 09:45', '09:30 - 09:45'),
        ('09:45 - 10.00', '09:45 - 10.00'),
        ('10:00 - 10:15', '10:00 - 10:15'),
        ('10:15 - 10:30', '10:15 - 10:30'),
        ('10:30 - 10:45', '10:30 - 10:45'),
        ('10:45 - 11.00', '10:45 - 11.00'),
        ('11:00 - 11:15', '11:00 - 11:15'),
        ('11:15 - 11:30', '11:15 - 11:30'),
        ('11:30 - 11:45', '11:30 - 11:45'),
        ('11:45 - 12.00', '11:45 - 12.00'),

        ('13:00 - 13:15', '13:00 - 13:15'),
        ('13:15 - 13:30', '13:15 - 13:30'),
        ('13:30 - 13:45', '13:30 - 13:45'),
        ('13:45 - 14.00', '13:45 - 14.00'),
        ('14:00 - 14:15', '14:00 - 14:15'),
        ('14:15 - 14:30', '14:15 - 14:30'),
        ('14:30 - 14:45', '14:30 - 14:45'),
        ('14:45 - 15.00', '14:45 - 15.00'),
    )

# Create your models here.
class Kelurahan(models.Model): # TODO: belum makemigrations and migrate
    name = models.CharField(max_length=255)
    kecamatan = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

class RequestKTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    requested_at = models.DateTimeField(auto_now_add=True)

    provinsi = models.CharField(max_length=255, default="Jawa Barat")
    kota = models.CharField(max_length=255, default="Depok")
    kecamatan = models.CharField(max_length=255, choices=KECAMATAN_CHOICES)
    kelurahan = models.CharField(max_length=255, choices=KELURAHAN_CHOICES)
    permohonan = models.CharField(max_length=255, choices=PERMOHONAN_CHOICES) 

    nama_lengkap = models.CharField(max_length=255)
    nomor_kk = models.CharField(max_length=255)
    nik = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)

    rt = models.CharField(max_length=255)
    rw = models.CharField(max_length=255)
    kode_pos = models.CharField(max_length=255)

    nomor_hp = models.CharField(max_length=15)

    schedule_date = models.DateField()
    schedule_time = models.CharField(max_length=255, choices=TIMESLOT_LIST)

    def __str__(self):
        return str(self.schedule_date) + ' at ' + self.schedule_time
