from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis, member, pesanan

class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg', 'nama', 'stok', 'harga', 'link_brg', 'jenis_id']
    search_fields = ['kodebrg', 'nama']
    list_filter = ('jenis_id')
    list_per_page = 3

class kolomMember(admin.ModelAdmin):
    list_display = ['kode_member', 'nama', 'alamat', 'tahun_gabung', 'poin']
    search_fields = ['kode_member', 'nama']
    list_filter = ('poin')
    list_per_page = 3

class kolomPesanan(admin.ModelAdmin):
    list_display = ['id_member', 'nama_barang', 'pembeli', 'tgl_pesan']
    search_fields = ['id_member', 'nama']
    list_filter = ('nama_barang',)
    list_per_page = 3

admin.site.register(Barang)
admin.site.register(Jenis)
admin.site.register(member)
admin.site.register(pesanan, kolomPesanan)
