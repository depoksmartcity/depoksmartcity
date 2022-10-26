from django import forms

# iterables
KECAMATAN_CHOICES = (
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

# creating a form 
class RequestKTPForm(forms.Form):
    provinsi = "Jawa Barat"
    kota = "Depok"
    kecamatan = forms.ChoiceField(choices=KECAMATAN_CHOICES, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'kecamatan'}))
    kelurahan = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'kelurahan'}))

    permohonan = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'permohonan'}))

    nama_lengkap = forms.CharField(max_length = 250, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'nama_lengkap'}))
    nomor_kk = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'nomor_kk'}))
    nik = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'nik'}))
    alamat = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'alamat'}))

    rt = forms.IntegerField()
    rw = forms.IntegerField()
    kode_pos = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'kode_pos'}))

    nomor_hp = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'nomor_hp'})) # untuk dihubungi dalam melakukan konfirmasi

    jadwal = forms.CharField(max_length = 250, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'jadwal'}))
