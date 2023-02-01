from django.db import models

# Create your models here.

class Jenis(models.Model):
    name = models.CharField(max_length=50)
    ket = models.TextField()

    def __str__(self):
        return self.name

class Barang(models.Model):
    kodebrg = models.CharField(max_length=8)
    nama = models.CharField(max_length=100)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_brg = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama

class member(models.Model):
    kode_member = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=120)
    tahun_gabung = models.CharField(max_length=20)
    poin = models.IntegerField()

    def __str__(self):
        return self.nama

class pesanan(models.Model):
    id_member = models.CharField(max_length=10)
    nama_barang = models.CharField(max_length=100)
    pembeli = models.CharField(max_length=150)
    tgl_pesan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_barang