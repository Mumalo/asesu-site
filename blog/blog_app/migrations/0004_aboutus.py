# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('blog_app', '0003_sliderimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='pages.Page', serialize=False)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('cover', models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
    ]
