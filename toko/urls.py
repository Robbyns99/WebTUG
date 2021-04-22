from django.urls import path
from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('about/', views.about, name="about"),
	path('help/', views.help, name="help"),

	path('update_item/', views.updateItem, name="update_item"),
	path('proses_pesan/', views.prosesPesan, name="proses_pesan"),
	# path('success/', views.success, name="success"),
]