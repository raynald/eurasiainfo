# -*- coding: utf-8 -*-

from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
# from mezzanine.core.admin import SingletonAdmin
from mezzanine.pages.admin import PageAdmin
from mezzanine.blog.admin import BlogPostAdmin

from .models import HomePage, Slide, IconBlurb, Portfolio, ENewspaper


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class IconBlurbInline(TabularDynamicInlineAdmin):
    model = IconBlurb

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, IconBlurbInline)

class ENewspaperAdmin(BlogPostAdmin):
    model = ENewspaper

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Portfolio, PageAdmin)
admin.site.register(ENewspaper, ENewspaperAdmin)

# admin.site.register(SitewideContent, SingletonAdmin)