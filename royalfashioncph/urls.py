from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'royalfashioncph.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^humans\.txt$', 'alphastage.views.humanstxt', name='humanstxt'),
    url(r'^robots\.txt$', include('robots.urls')),
)
