from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
  # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  user = models.OneToOneField(User, verbose_name=('user'), on_delete=models.CASCADE)
  nama = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)

  def __str__(self):
    return str(self.nama)

class Produk(models.Model):
  nama = models.CharField(max_length=200, null=True)
  harga = models.FloatField()
  image = models.ImageField(null=True, blank=True)

  def __str__(self):
    return self.nama

  @property
  def imageURL(self):
    try:
      url = self.image.url
    except:
      url = ''
    return url

class Pesan(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
  waktu_pesanan = models.DateTimeField(auto_now_add=True)
  complete = models.BooleanField(default=False, null=True, blank=False)
  transaksi_id = models.CharField(max_length=200, null=True)

  def __str__(self):
    return str(self.id)

  @property
  def pengiriman(self):
    pengiriman = True
    itempesan = self.itempesan_set.all()
    return pengiriman

  @property
  def get_cart_total(self):
    itempesan = self.itempesan_set.all()
    total = sum([item.get_total for item in itempesan])
    return total

  @property
  def get_cart_items(self):
    itempesan = self.itempesan_set.all()
    total = sum([item.jumlah for item in itempesan])
    return total

class Itempesan(models.Model):
  produk = models.ForeignKey(Produk, on_delete=models.SET_NULL, null=True, blank=True)
  pesan = models.ForeignKey(Pesan, on_delete=models.SET_NULL, null=True, blank=True)
  jumlah = models.IntegerField(default=0, null=True, blank=True)
  waktu_penambah = models.DateTimeField(auto_now_add=True)

  @property
  def get_total(self):
    total = self.produk.harga * self.jumlah
    return total

class IDpesan(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
  pesan = models.ForeignKey(Pesan, on_delete=models.SET_NULL, null=True, blank=True)
  idgame = models.CharField(max_length=200, null=True)
  servergame = models.CharField(max_length=200, null=True)
  waktu_penambah = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.idgame)
