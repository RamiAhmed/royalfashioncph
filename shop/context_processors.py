
def shop_collections(request):
    from django.shortcuts import get_list_or_404
    from shop.models import Collection
    collections = get_list_or_404(Collection, active=True)
    return {'collections': collections}
    