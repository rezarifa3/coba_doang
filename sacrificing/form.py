from django.forms import ModelForm
from sacrificing.models import Buku
from django import forms

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

        widgets = {
            'judul': forms.TextInput({'class':'form-control'}),
            'penulis': forms.TextInput({'class': 'form-control'}),
            'penerbit': forms.TextInput({'class': 'form-control'}),
            'jumlah': forms.NumberInput({'class': 'form-control'}),
            'kelompok_id': forms.Select({'class': 'form-control'}),
        }