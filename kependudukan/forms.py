from django import forms
   
# creating a form 
class RequestKTPForm(forms.Form):
    provinsi = "Jawa Barat"
    kota = "Depok"
    kecamatan = forms.ChoiceField()
    kelurahan = forms.ChoiceField()

    permohonan = forms.CharField(max_length=250)

    nama_lengkap = forms.CharField(max_length = 250)
    nomor_kk = forms.CharField(max_length=16)
    nik = forms.CharField(max_length=16)
    alamat = forms.Textarea()

    rt = forms.IntegerField()
    rw = forms.IntegerField()
    kode_pos = forms.CharField(max_length=5)

    nomor_hp = forms.CharField(max_length=15) # untuk dihubungi dalam melakukan konfirmasi

    schedule_date = forms.DateField()
    schedule_time = forms.TimeField()
