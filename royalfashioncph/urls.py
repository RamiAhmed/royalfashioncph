from django.conf.urls import patterns, include, url
from django.contrib import sitemaps
from django.core.urlresolvers import reverse

from django.contrib import admin
admin.autodiscover()

from royalfashioncph import views

class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.6
    changefreq = 'daily'

    def items(self):
        return ['home', 'om-os']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'static': StaticViewsSitemap,
}

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^om-os/', include('contact.urls')),
    
    url(r'^shop/(?P<collection_slug>[\w\-]+)/(?P<product_slug>[\w\-]+)/$', 'shop.views.details', name='shop-details'),    
    url(r'^shop/(?P<slug>[\w\-]+)/$', 'shop.views.index', name='shop'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^humans\.txt$', views.humanstxt, name='humanstxt'),
    url(r'^robots\.txt$', include('robots.urls')),
)
