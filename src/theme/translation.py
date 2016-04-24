from modeltranslation.translator import translator, TranslationOptions
from .models import  HomePage, Portfolio, ENewspaper, Slide, IconBlurb

class TranslatedHomePage(TranslationOptions):
    fields = ()

class TranslatedPortfolio(TranslationOptions):
    fields = ()

class TranslatedENewspaper(TranslationOptions):
    fields = ()

class TranslatedSlide(TranslationOptions):
    fields = ()

class TranslatedIconBlurb(TranslationOptions):
    fields = ()

translator.register(Portfolio, TranslatedPortfolio)
translator.register(ENewspaper, TranslatedENewspaper)
translator.register(Slide, TranslatedSlide)
translator.register(IconBlurb, TranslatedIconBlurb)
translator.register(HomePage, TranslatedHomePage)
