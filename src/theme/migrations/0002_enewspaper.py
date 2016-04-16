# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150527_1555'),
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ENewspaper',
            fields=[
                ('blogpost_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='blog.BlogPost')),
            ],
            options={
                'verbose_name': 'ENewspaper',
                'verbose_name_plural': 'Enewspapers',
            },
            bases=('blog.blogpost',),
        ),
    ]
