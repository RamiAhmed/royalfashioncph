from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

from contact import views


urlpatterns = patterns('',
    url(r'^$', views.contact, name='om-os'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),

)
