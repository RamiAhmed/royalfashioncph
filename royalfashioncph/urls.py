from django.conf.urls import patterns, include, url
from django.contrib import sitemaps
from django.contrib.sitemaps import GenericSitemap

from django.core.urlresolvers import reverse

from django.contrib import admin
admin.autodiscover()

from royalfashioncph import views
from shop.models import Collection,Product

class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'om-os']

    def location(self, item):
        return reverse(item)

collection_info_dict = {
    'queryset': Collection.objects.all().filter(active=True),
    'date_field': 'added',
}

product_info_dict = {
    'queryset': Product.objects.all().filter(for_sale=True),
    'date_field': 'added',                         
}                     
    
sitemaps = {
    'static': StaticViewsSitemap,
    'collections': GenericSitemap(collection_info_dict, priority=0.7),
    'products': GenericSitemap(product_info_dict, priority=0.6),
}

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^om-os/', include('contact.urls')),
    
    url(r'^shop/(?P<collection_slug>[\w\-]+)/(?P<product_slug>[\w\-]+)/$', 'shop.views.details', name='shop-details'),    
    url(r'^shop/(?P<slug>[\w\-]+)/$', 'shop.views.index', name='shop'),
    url(r'^search/', include('haystack.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^humans\.txt$', views.humanstxt, name='humanstxt'),
    url(r'^robots\.txt$', include('robots.urls')),
)
