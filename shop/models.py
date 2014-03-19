# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField
from tinymce.models import HTMLField
import datetime

# Create your models here.
class ProductImage(models.Model):
    image_title = models.CharField(max_length=200, verbose_name="Billed titel eller beskrivelse", blank=True)
    image = ImageField(upload_to="/media/products/")
    product = models.ForeignKey('Product', related_name="images", verbose_name="Tilhører produkt")
    photographer_name = models.CharField(max_length=255, verbose_name="Fotografs Navn", blank=True)
    photographer_url = models.URLField(verbose_name="Fotografs Hjemmeside (URL)", blank=True)
    
    def get_absolute_url(self):
        return u'%s' % self.image.url
    
    def __unicode__(self):
        return u'%s' % self.image_title
    
class ProductSize(models.Model):
    SIZE_CHOICES = (
        ('ClothSizes', (
                ('XS', 'Extra Small'),
                ('S', 'Small'),
                ('M', 'Medium'),
                ('L', 'Large'),
                ('XL', 'Extra Large'),
            )
        ),
        ('ShoeSizes', (
                ('36', '36'),
                ('37', '37'),
                ('38', '38'),
                ('39', '39'),
                ('40', '40'),
                ('41', '41'),
                ('42', '42'),
                ('43', '43'),
                ('44', '44'),
                ('45', '45'),
            )
        )
                       
                       
    )
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M', verbose_name="Tilgængelige Størrelser")
    product = models.ForeignKey('Product', related_name="sizes", verbose_name="Tilhører produkt", blank=True)
    
    def __unicode__(self):
        return u'%s' % self.size

    
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Produkt Navn", default="Produkt")
    description = models.CharField(max_length=255, verbose_name="Produkt beskrivelse eller historie", blank=True)
    price = models.PositiveSmallIntegerField(verbose_name="Produkt Pris")
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Dato og tidspunkt tilføjet")
    for_sale = models.BooleanField(verbose_name="Er produktet klar til salg?", default=True)
    slug = models.SlugField(unique=True, max_length=255, verbose_name="URL; denne værdi bør aldrig ændres!")
    collection = models.ForeignKey('Collection', related_name="products", verbose_name="Tilhører kollektion")
    
    def get_absolute_url(self):
        return reverse('shop.views.details', args=[self.collection.slug, self.slug])
    
    def get_first_image(self):
        return self.images.get(id=1)
    
    class Meta:
        ordering = ['-added']    
    
    def __unicode__(self):
        return u'%s' % self.name
    
    def get_sizes_string(self):
        return ''.join([s.size for s in self.sizes.all()])       
        
    
class Collection(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kollektion", default="Kollektion")
    description = models.CharField(max_length=255, verbose_name="Kollektion beskrivelse", blank=True)
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Dato og tidspunkt tilføjet")
    active = models.BooleanField(default=True, verbose_name="Er denne kollektion klar til salg?")
    slug = models.SlugField(unique=True, max_length=255, verbose_name="URL; denne værdi bør aldrig ændres!")
    
    def get_absolute_url(self):
        return reverse('shop.views.index', args=[self.slug])   
    
    class Meta:
        ordering = ['-added']    
    
    def __unicode__(self):
        return u'%s' % self.name  
    
