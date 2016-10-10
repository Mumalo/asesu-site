
from mezzanine.conf import register_setting
from django.utils.translation import ugettext_lazy as _

register_setting(
   name="SITE_TITLE",
   label= _("Site Title"),
   description= ("Title that will display at the top of the site, and be "
        "appended to the content of the HTML title tags on every page."),
   editable=True,
   default="ASESU",
   translatable=True,
)

register_setting(
    name="BLOG_USE_FEATURED_IMAGE",
    description= _("Enable featured images in blog posts"),
    editable=False,
    default=True,
)

register_setting(
    name="PAGES_MENU_SHOW_ALL",
    description=_("If True, the left-hand tree template for the pages menu will show all levels of navigation, otherwise child pages are only shown when viewing the parent page."),
    editable=True,
    default=True,
)

