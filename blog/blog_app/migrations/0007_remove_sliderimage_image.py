# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_sliderimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliderimage',
            name='image',
        ),
    ]
