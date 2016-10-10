# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_remove_sliderimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='image',
            field=mezzanine.core.fields.FileField(default=datetime.datetime(2016, 10, 8, 6, 37, 52, 776590, tzinfo=utc), max_length=200, verbose_name='Image'),
            preserve_default=False,
        ),
    ]
