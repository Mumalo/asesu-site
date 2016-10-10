from django.db import models
from mezzanine.pages.models import Page, RichText, Orderable
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from mezzanine.core.fields import FileField
from mezzanine.utils.models import upload_to
from django.utils.encoding import force_text
from string import punctuation


class AboutUs(Page,RichText ):
    cover = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = _("About Us")
        verbose_name_plural = _("About Us")

class Programs(Page, RichText):
    cover = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)
    video_url = models.URLField(blank=True, help_text="Provide a u-tube video link here")

    class Meta:
        verbose_name = _("Program")
        verbose_name_plural = _("Programs")

class HomePage(Page,RichText):
    home_title = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=25, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=125, blank=True)
    class Meta:
        verbose_name = _("Home Page")
        verbose_name_plural = _("Home Pages")

@python_2_unicode_compatible
class SliderImage(Orderable):
    home = models.ForeignKey("HomePage", related_name="images")
    image = FileField(verbose_name=_("Image"),max_length=200,format="Image",
                      upload_to=upload_to("galleries.GalleryImage.image", "galleries"))
    image_heading = models.CharField(_("Heading"), max_length=1000, blank=True)
    description = models.CharField(_("Description"), max_length=1000, blank=True)

    class Meta:
        verbose_name = _("Slider Image")
        verbose_name_plural = _("Slider Images")

    def __str__(self):
        return self.description
    def save(self, *args, **kwargs):
        """
        If no description is given when created, create one from the
        file name.
        """
        if not self.id and not self.description:
            name = force_text(self.image)
            name = name.rsplit("/", 1)[-1].rsplit(".", 1)[0]
            name = name.replace("'", "")
            name = "".join([c if c not in punctuation else " " for c in name])
            # str.title() doesn't deal with unicode very well.
            # http://bugs.python.org/issue6412
            name = "".join([s.upper() if i == 0 or name[i - 1] == " " else s
                            for i, s in enumerate(name)])
            self.description = name
        super(SliderImage, self).save(*args, **kwargs)








# Register your models here.

