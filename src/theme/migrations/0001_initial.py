# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('heading', models.CharField(help_text=b'The heading under the icon blurbs', max_length=200)),
                ('subheading', models.CharField(help_text=b'The subheading just below the heading', max_length=200)),
                ('featured_works_heading', models.CharField(default=b'Featured Works', max_length=200)),
                ('content_heading', models.CharField(default=b'About us!', max_length=200)),
                ('latest_posts_heading', models.CharField(default=b'Latest Posts', max_length=200)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='IconBlurb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('icon', mezzanine.core.fields.FileField(max_length=255, verbose_name='Image')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('link', models.CharField(help_text=b'Optional, if provided clicking the blurb will go here.', max_length=2000, blank=True)),
                ('homepage', models.ForeignKey(related_name='blurbs', to='theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('homepage', models.ForeignKey(related_name='slides', to='theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_portfolio',
            field=models.ForeignKey(blank=True, to='theme.Portfolio', help_text=b'If selected items from this portfolio will be featured on the home page.', null=True),
        ),
    ]
