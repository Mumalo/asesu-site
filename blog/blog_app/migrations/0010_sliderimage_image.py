# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import mezzanine.core.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_remove_sliderimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='image',
            field=mezzanine.core.fields.FileField(verbose_name='Image', max_length=200, default=datetime.datetime(2016, 10, 8, 7, 13, 37, 156552, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
