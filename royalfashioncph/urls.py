from django.conf.urls import patterns, include, url
from django.contrib import sitemaps
from django.core.urlresolvers import reverse

from django.contrib import admin
admin.autodiscover()

class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.6
    changefreq = 'daily'

    def items(self):
        return ['home', 'om-os', 'spring-collection']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'static': StaticViewsSitemap,
}

urlpatterns = patterns('',
    url(r'^$', 'royalfashioncph.views.home', name='home'),
    url(r'^home/', 'royalfashioncph.views.home'),
    url(r'^om-os/', 'royalfashioncph.views.omos', name='om-os'),
    url(r'^spring-collection/', 'royalfashioncph.views.springcollection', name='spring-collection'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^humans\.txt$', 'royalfashioncph.views.humanstxt', name='humanstxt'),
    url(r'^robots\.txt$', include('robots.urls')),
)
