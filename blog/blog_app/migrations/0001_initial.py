# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, to='pages.Page', primary_key=True, parent_link=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('home_title', models.CharField(max_length=250, blank=True)),
            ],
            options={
                'verbose_name': 'Home Page',
                'verbose_name_plural': 'Home Pages',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, to='pages.Page', primary_key=True, parent_link=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('cover', models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d/')),
                ('video_url', models.URLField(blank=True, help_text='Provide a u-tube video link here')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(verbose_name='Order', null=True)),
                ('image', mezzanine.core.fields.FileField(verbose_name='Image', max_length=200)),
                ('description', models.CharField(verbose_name='Description', max_length=1000, blank=True)),
                ('home', models.ForeignKey(related_name='images', to='blog_app.HomePage')),
            ],
            options={
                'verbose_name': 'Slider Image',
                'verbose_name_plural': 'Slider Images',
                'ordering': ('_order',),
            },
        ),
    ]
