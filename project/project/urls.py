"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse
from django.shortcuts import render
from kelas.views import produk, home
from kelas.views import tambah_barang, ubah_brg, hapus_brg
from kelas.views import tambah_member, ubah_member, hapus_member
from kelas.views import tambah_pesanan, ubah_pesanan, hapus_pesanan
from kelas.views import Barang_View, Member, Pesanan

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', coba),
    path('',home, name='home'),
    path('produk/',produk, name='produk'),
    path('addbrg/',tambah_barang),
    path('vbrg/',Barang_View, name='vbrg'),
    path('member/', Member, name='member'),
    path('pesanan/', Pesanan, name='pesanan'),
    path('ubahBrg/<int:id_barang>',ubah_brg, name='ubah_brg'),
    path('hapus/<int:id_barang>',hapus_brg, name='hapus_brg'),
    path('addmember/',tambah_member, name="add_member"),
    path('ubahMember/<int:id_member>',ubah_member, name='ubah_member'),
    path('delete/<int:id_member>',hapus_member, name='hapus_member'),
    path('addpesanan/',tambah_pesanan, name="add_pesanan"),
    path('ubahpesanan/<int:id_pesanan>',ubah_pesanan, name='ubah_pesanan'),
    path('buang/<int:id_pesanan>',hapus_pesanan, name='hapus_pesanan'),
    
]
