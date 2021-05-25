from django.urls import path 
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('lojas/', views.stores, name='stores'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('categoria/<slug:category_slug>/', views.category_list, name='category_list'),
    path('loja/<slug:store_slug>/', views.store_list, name='store_list'),
]