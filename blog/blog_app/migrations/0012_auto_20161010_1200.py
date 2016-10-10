# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_sliderimage_image_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='address',
            field=models.CharField(max_length=125, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='phone',
            field=models.CharField(max_length=25, blank=True),
        ),
    ]
