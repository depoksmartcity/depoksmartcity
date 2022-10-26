from django import forms

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
    (0, "Beji"),
    (1, "Pancoran Mas"),
    (2, "Cipayung"),
    (3, "Sukmajaya"),
    (4, "Cilodong"),
    (5, "Limo"),
    (6, "Cinere"),
    (7, "Cimanggis"),
    (8, "Tapos"),
    (9, "Sawangan"),
    (10, "Bojong Sari")
)

PERMOHONAN_CHOICES = (
    ("Baru", "Baru"),
    ("Penggantian", "Penggantian")
)

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

    jadwal = forms.CharField(max_length = 250, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'jadwal'}))
