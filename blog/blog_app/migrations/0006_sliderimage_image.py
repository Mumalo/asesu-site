# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_remove_sliderimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='image',
            field=mezzanine.core.fields.FileField(default=datetime.datetime(2016, 10, 8, 6, 31, 42, 432350, tzinfo=utc), verbose_name='Image', max_length=200),
            preserve_default=False,
        ),
    ]
