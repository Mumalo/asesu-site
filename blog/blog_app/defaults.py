
from mezzanine.conf import register_setting

register_setting(
   name="SITE_TITLE",
   label= ("Site Title"),
   description= ("Title that will display at the top of the site, and be "
        "appended to the content of the HTML title tags on every page."),
   editable=True,
   default="ASESU",
   translatable=True,
)


