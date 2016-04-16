# -*- coding: utf-8 -*-

from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
# from mezzanine.core.admin import SingletonAdmin
from mezzanine.pages.admin import PageAdmin

from .models import HomePage, Slide, IconBlurb, Portfolio


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class IconBlurbInline(TabularDynamicInlineAdmin):
    model = IconBlurb

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, IconBlurbInline)


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Portfolio, PageAdmin)
# admin.site.register(SitewideContent, SingletonAdmin)