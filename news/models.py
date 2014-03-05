# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from tinymce.models import HTMLField
from sorl.thumbnail import ImageField
import datetime

# Create your models here.
class NewsImage(models.Model):
    image_title = models.CharField(max_length=200, verbose_name="Billed titel eller beskrivelse", blank=True)
    image = ImageField(upload_to="/media/news/")
    news_post = models.ForeignKey('NewsPost', related_name="images", verbose_name="Tilhører nyhed")
    
    def get_absolute_url(self):
        return u'%s' % self.image.url
    
    def __unicode__(self):
        return u'%s' % self.image_title

class NewsPost(models.Model):
    title = models.CharField(max_length=254, verbose_name="Nyheds titel")
    #body = models.TextField(verbose_name="Nyheds tekst")
    body = HTMLField(verbose_name="Nyheds tekst")
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Dato og tidspunkt tilføjet")
    active = models.BooleanField(default=True, verbose_name="Er denne nyhed aktiv?")
    slug = models.SlugField(unique=True, max_length=254, verbose_name="URL; denne værdi bør aldrig ændres!")
    
    def get_absolute_url(self):
        date = self.added
        return reverse('news.views.post', args=[date.strftime("%Y"), date.strftime("%m"), date.strftime("%d"), self.slug])

    class Meta:
        ordering = ['-added'] 
    
    def __unicode__(self):
        return u'%s' % self.title
    
    