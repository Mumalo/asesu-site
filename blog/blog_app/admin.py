from __future__ import unicode_literals

from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import Programs, HomePage, SliderImage, AboutUs
from mezzanine.utils.static import static_lazy as static

admin.site.register(AboutUs, PageAdmin)
admin.site.register(Programs, PageAdmin)


class HomeImageInline(TabularDynamicInlineAdmin):
    model = SliderImage

class HomeAdmin(PageAdmin):

    class Media:
        css = {"all": (static("mezzanine/css/admin/gallery.css"))}
    inlines = (HomeImageInline, )
admin.site.register(HomePage, HomeAdmin)

