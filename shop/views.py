from django.shortcuts import render, get_object_or_404, get_list_or_404

from shop.models import Product, Collection

# Create your views here.
def index(request, slug):
    collection = get_object_or_404(Collection, slug=slug)
    products = collection.products.all().filter(for_sale=True)
    
    return render(request, 'shop/index.html', {'collection':collection, 'products':products})

def details(request, collection_slug, product_slug):
    collection = get_object_or_404(Collection, slug=collection_slug)
    product = get_object_or_404(Product, slug=product_slug)
    images = product.images.all()
    
    sizes_set = product.sizes.all()
    sizes = "".join([str(i) for i in sizes_set.values_list()])
    
    return render(request, 'shop/details.html', {'collection':collection, 'product':product, 'images':images, 'sizes':sizes})