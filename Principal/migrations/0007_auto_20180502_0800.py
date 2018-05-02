# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0006_auto_20180502_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cedula', models.CharField(max_length=15, serialize=False, verbose_name='cedulA: ', primary_key=True)),
                ('apellidoPer', models.CharField(max_length=20, verbose_name='apellidO ')),
                ('nombrePer', models.CharField(max_length=20, verbose_name='nombrE ')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
