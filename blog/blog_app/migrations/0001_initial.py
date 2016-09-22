# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, to='pages.Page', auto_created=True)),
                ('dob', models.DateField(verbose_name='Date of birth')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cover', models.ImageField(upload_to='authors')),
                ('author', models.ForeignKey(to='blog_app.Author')),
            ],
        ),
    ]
