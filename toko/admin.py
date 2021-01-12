from django.contrib import admin
from .models import Produk
from .models import Customer
from .models import Pesan
from .models import Itempesan
from .models import IDpesan

admin.site.register(Customer)
admin.site.register(Produk)
admin.site.register(Pesan)
admin.site.register(Itempesan)
admin.site.register(IDpesan)