from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

from news import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='news'),
    #url(r'^(?P<year>\d{4})/$', views.year, name='news-year'),
    #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', views.month, name='news-month'),
    #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$', views.day, name='news-day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/(?P<news_slug>[\w\-]+)/$', views.post, name='news-post'),
    

)
