from django import forms
from django.forms import ModelForm
from kelas.models import Barang, member, pesanan


class FormBarang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'

        widgets = {
            # nama pada widget harus sana dengan pada file models.py
            'kodebrg': forms.TextInput({'class': 'form-control'}),
            'nama': forms.TextInput({'class': 'form-control'}),
            'stok': forms.NumberInput({'class': 'form-control'}),
            'harga': forms.NumberInput({'class': 'form-control'}),
            'link_brg': forms.TextInput({'class': 'form-control'}),
            'jenis_id': forms.Select({'class': 'form-control'}),
        }

class FormMember(ModelForm):
    class Meta:
        model = member
        fields = '__all__'

        widgets = {
            # nama pada widget harus sana dengan pada file models.py
            'kode_member' : forms.TextInput({'class': 'from-control'}),
            'nama' : forms.TextInput({'class': 'from-control'}),
            'alamat' : forms.TextInput({'class': 'from-control'}),
            'tahun_gabung' : forms.NumberInput({'class': 'form-control'}),
            'poin' : forms.NumberInput({'class': 'form-control'}),
        }

class FormPesanan(ModelForm):
    class Meta:
        model = pesanan
        fields = '__all__'

        widgets = {
            # nama pada widget harus sana dengan pada file models.py           
            'id_member' : forms.TextInput({'class': 'from-control'}),
            'nama_barang' : forms.TextInput({'class': 'from-control'}),
            'pembeli' : forms.TextInput({'class': 'from-control'}),
            'tgl_pesan' : forms.NumberInput({'class': 'form-control'}),
        }