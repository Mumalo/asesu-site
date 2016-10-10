# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_sliderimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='image_heading',
            field=models.CharField(max_length=1000, verbose_name='Heading', blank=True),
        ),
    ]
