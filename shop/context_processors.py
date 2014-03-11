
def shop_collections(request):
    from shop.models import Collection

    collections = Collection.objects.all().filter(active=True)
    return {'collections': collections}
    