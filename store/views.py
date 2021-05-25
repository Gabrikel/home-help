from django.shortcuts import get_object_or_404, render
from .models import Category, Store, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def home(request):
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'categories': categories})
    
def stores(request):
    stores = Store.objects.all()
    return render(request, 'store/stores.html', {'stores': stores})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})

def store_list(request, store_slug):
    store = get_object_or_404(Store, slug=store_slug)
    products = Product.objects.filter(store=store)
    return render(request, 'store/products/store.html', {'store': store, 'products': products})