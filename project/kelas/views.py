from django.shortcuts import render,redirect
from kelas.forms import FormBarang, FormMember, FormPesanan
from kelas.models import Barang, member, pesanan
from django.contrib import messages

def home(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request, 'home.html',konteks)

def Barang_View(request):
    Barangs=Barang.objects.all()
    konteks={
        'Barangs':Barangs,
    }
    return render(request, 'tampil_brg.html',konteks)

def Member(request):
    Members=member.objects.all()
    konteks={
        'Members':Members,
    }
    return render(request, 'member.html',konteks)

def Pesanan(request):
    Pesanans=pesanan.objects.all()
    konteks={
        'Pesanans':Pesanans,
    }
    return render(request, 'pesanan.html',konteks)

def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request, 'produk.html',konteks)

# Create your views here.

def tambah_barang(request):
    if request.POST:
        form= FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = FormBarang()
            konteks = {
                'form':form,
            }
            return render(request, 'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        konteks={
            'form':form,
        }
    return render(request, 'tambah_barang.html',konteks)

def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('ubah_brg', id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs':barangs,
        }
    return render(request, 'ubah_brg.html',konteks)

def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request, "Data Terhapus")
    return redirect('vbrg')

def tambah_member(request):
    if request.POST:
        form= FormMember(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = FormMember()
            konteks = {
                'form':form,
            }
            return render(request, 'tambah_member.html',konteks)
    else:
        form=FormMember()
        konteks={
            'form':form,
        }
    return render(request, 'tambah_member.html',konteks)

def ubah_member(request,id_member):
    Members=member.objects.get(id=id_member)
    if request.POST:
        form=FormMember(request.POST,instance=Members)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('ubah_member', id_member=id_member)
    else:
        form=FormMember(instance=Members)
        konteks = {
            'form':form,
            'Members':Members,
        }
    return render(request, 'ubah_member.html',konteks)

def hapus_member(request,id_member):
    Members=member.objects.filter(id=id_member)
    Members.delete()
    messages.success(request, "Data Terhapus")
    return redirect('member')

def tambah_pesanan(request):
    if request.POST:
        form= FormPesanan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = FormPesanan()
            konteks = {
                'form':form,
            }
            return render(request, 'tambah_pesanan.html',konteks)
    else:
        form=FormPesanan()
        konteks={
            'form':form,
        }
    return render(request, 'tambah_pesanan.html',konteks)

def ubah_pesanan(request,id_pesanan):
    pesanans=pesanan.objects.get(id=id_pesanan)
    if request.POST:
        form=FormPesanan(request.POST,instance=pesanans)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('ubah_pesanan', id_pesanan=id_pesanan)
    else:
        form=FormPesanan(instance=pesanans)
        konteks = {
            'form':form,
            'pesanans':pesanans,
        }
    return render(request, 'ubah_pesanan.html',konteks)

def hapus_pesanan(request,id_pesanan):
    pesanans=pesanan.objects.filter(id=id_pesanan)
    pesanans.delete()
    messages.success(request, "Data Terhapus")
    return redirect('pesanan')
