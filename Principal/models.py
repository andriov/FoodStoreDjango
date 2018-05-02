# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=False)
    def get_absolute_url(self):
        return reverse('products:product_list_by_category',
                        args=[self.slug])

class Meta:
    ordering = ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'

def __str__(self):
    return self.name

class Product(models.Model):
    #STATUS_CHOICES=(
    #    ('Desayuno','desayuno'),
    #    ('Almuerzo','almuerzo'),
    #    ('Merienda','merienda'),
    #    ('Otro', 'otro'),
    #)
    category = models.ForeignKey(Category,related_name = 'products')# ForeignKey key relation one to many
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, default=False)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #Aditional image to the product, install pip install Pillow

    description = models.TextField(max_length=240, help_text=('Escriba en menos de 240 carácteres la descripción del producto.'), verbose_name='Descripción ')
    stock = models.PositiveIntegerField(default=False, verbose_name='Stock ')
    available = models.BooleanField(default=True) #campo para quitar el producto del catalogo
    price = models.DecimalField(default= 00.00, max_digits=4, decimal_places=2, verbose_name = 'Precio ')
    start_publish = models.DateTimeField(default=timezone.now, blank=False,verbose_name = 'Inicio de Publicación  ')#install pytz
    end_publish = models.DateTimeField(default=timezone.now, blank=False, verbose_name='Fin de Publicación')
    def get_absolute_url(self):
        return reverse('products:product_detail',
                        args=[self.id, self.slug])
    #available_time = models.DurationField( help_text=('Tiempo en el que se pueden realizar las compras de este producto'), verbose_name='Tiempo Disponible: ')
    #tipo = models.CharField(max_length=40,
    #                              choices=STATUS_CHOICES,
    #                              verbose_name='Tipo')

    #id_Product = models.PositiveIntegerField(primary_key=True, null=False, blank=False, default=False)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
