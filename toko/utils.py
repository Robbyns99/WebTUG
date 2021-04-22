import json
from .models import Produk
from .models import Customer
from .models import Itempesan
from .models import IDpesan
from .models import Pesan

from django.contrib.auth.models import User

def cookieCart(request):
  try:
    cart = json.loads(request.COOKIES['cart'])
  except:
    cart ={}
    print('Cart:', cart)
    
  items =[]
  pesan ={'get_cart_total':0, 'get_cart_items':0, 'pengiriman':False}
  cartItems = pesan ['get_cart_items']

  for i in cart:
		#Menggunakan blok percobaan untuk mencegah barang-barang dicart yang mungkin telah dihapus dari produk
    try:
      cartItems += cart[i]['jumlah']
      
      produk = Produk.objects.get(id=i)
      total = (produk.harga * cart[i]['jumlah'])

      pesan['get_cart_total'] += total
      pesan['get_cart_items'] += cart[i]['jumlah']

      item = {
				'produk':{
					"id":produk.id,
					"nama":produk.nama,
					"harga":produk.harga,
					"imageURL":produk.imageURL
				},
				'jumlah':cart[i]['jumlah'],
				'get_total':total,
			}
      items.append(item)

      pesan['pengiriman'] = True
    except:
      pass
  return{'cartItems':cartItems, 'pesan':pesan, 'items':items}

def cartData(request):
  if request.user.is_authenticated:
    customer = request.user.customer
    pesan, created = Pesan.objects.get_or_create(customer=customer, complete=False)
    items=pesan.itempesan_set.all()
    cartItems = pesan.get_cart_items 
  else:
    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']
    pesan = cookieData['pesan']
    items = cookieData['items']
  return{'cartItems':cartItems, 'pesan':pesan, 'items':items}

def guestOrder(request, data):
  # print("User is'n logged in..")
  
    
  # print('COOKIES:', request.COOKIES)
  nama = data['form']['nama']
  email = data['form']['email']
  # input user
  user = User.objects.get_or_create(
    username=nama,
    )
  
  print(user[1])

  cookieData = cookieCart(request)
  items = cookieData['items']

  customer, created = Customer.objects.get_or_create(
    email= email,
    nama = nama,
    user = User.objects.get(username=user[0]))
  

  pesan = Pesan.objects.create(customer=customer, complete=False)

  for item in items:
    produk = Produk.objects.get(id=item['produk']['id'])
    itemPesan = Itempesan.objects.create(produk=produk, pesan=pesan, jumlah=item['jumlah'])

  return customer, pesan