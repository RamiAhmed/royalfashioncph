from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'royalfashioncph.views.home', name='home'),
    url(r'^home/', 'royalfashioncph.views.home'),
    url(r'^om-os/', 'royalfashioncph.views.omos', name='om-os'),
    url(r'^spring-collection/', 'royalfashioncph.views.springcollection', name='spring-collection'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^humans\.txt$', 'royalfashioncph.views.humanstxt', name='humanstxt'),
    url(r'^robots\.txt$', include('robots.urls')),
)
