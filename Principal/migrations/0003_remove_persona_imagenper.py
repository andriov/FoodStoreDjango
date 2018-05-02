# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0002_auto_20180331_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='imagenPer',
        ),
    ]
