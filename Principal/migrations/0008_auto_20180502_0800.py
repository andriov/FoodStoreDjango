# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0007_auto_20180502_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(default=False, max_length=200)),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d', blank=True)),
                ('description', models.TextField(help_text='Escriba en menos de 240 car\xe1cteres la descripci\xf3n del producto.', max_length=240, verbose_name='Descripci\xf3n ')),
                ('stock', models.PositiveIntegerField(default=False, verbose_name='Stock ')),
                ('available', models.BooleanField(default=True)),
                ('price', models.DecimalField(default=0.0, verbose_name='Precio ', max_digits=4, decimal_places=2)),
                ('start_publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Inicio de Publicaci\xf3n  ')),
                ('end_publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fin de Publicaci\xf3n')),
                ('category', models.ForeignKey(related_name='products', to='Principal.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
