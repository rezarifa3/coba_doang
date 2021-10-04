from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from sacrificing.models import *
from sacrificing.form import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from sacrificing.resource import BukuResource

def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="laporan buku.xls"'
    return response

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil Dibuat")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form,
        }
    return render(request, 'signup.html', konteks)

def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request, "Data Berhasil Dihapus!")

    return redirect('buku')

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    books = Buku.objects.all();

    konteks = {
        'Books':books,
    }
    return render(request, 'buku.html', konteks)

def penulis(request):
    return HttpResponse("Halaman Penulis")

def penerbit(request):
    return render(request, "penerbit.html")

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-buku.html', konteks)
    else:
        form = FormBuku

        konteks = {
            'form': form
        }

    return render(request, "tambah-buku.html", konteks)

