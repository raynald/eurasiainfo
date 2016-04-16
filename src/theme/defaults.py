from mezzanine.conf import register_setting
from django.utils.translation import gettext as _

register_setting(
        name="SOCIAL_LINK_FACEBOOK",
        label=_("Facebook link"),
        description=_("If present a Facebook icon linking here will be in the "
                      "header."),
        editable=True,
        default="https://facebook.com/mezzatheme",
)