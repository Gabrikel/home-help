from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')


    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name='store_product_category', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    cep = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Stores'
    
    def get_absolute_url(self):
        return reverse('store:store_list', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    unity = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
    
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.name