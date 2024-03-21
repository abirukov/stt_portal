from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model
from wagtail.models import Page, Collection
from wagtail.search import index

from stt.base.models import PaginatedPage, SectionPage


class GalleryPage(PaginatedPage):
    subpage_types: list[str] = []
    skin = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Обложка",
        verbose_name="Обложка (необязательно)",
    )

    intro_title = models.CharField(
        verbose_name=_("Intro title"),
        max_length=250,
        blank=True,
        help_text=_("Optional H1 title for the gallery page."),
    )
    intro_text = RichTextField(
        blank=True,
        verbose_name=_("Intro text"),
        help_text=_("Optional text to go with the intro text."),
    )
    collection = models.ForeignKey(
        "wagtailcore.Collection",
        verbose_name=_("Collection"),
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Show images in this collection in the gallery view."),
    )
    content_panels = PaginatedPage.content_panels + [
        FieldPanel("skin"),
        FieldPanel("collection"),
        FieldPanel("intro_title"),
        FieldPanel("intro_text"),
    ]
    search_fields = Page.search_fields + [
        index.SearchField("intro_title"),
        index.SearchField("intro_text"),
    ]

    @property
    def elements(self) -> QuerySet:
        return get_gallery_images(self.collection.name)

    class Meta:
        verbose_name = "Страница галереи"
        verbose_name_plural = "Страницы галереи"


class GallerySectionPage(PaginatedPage, SectionPage):
    subpage_types = ["gallery.GalleryPage"]

    content_panels = SectionPage.content_panels + PaginatedPage.content_panels

    @property
    def elements(self) -> QuerySet:
        return GalleryPage.objects.all()

    class Meta:
        verbose_name = "Раздел галереи"
        verbose_name_plural = "Разделы галереи"


def get_gallery_images(collection: Collection) -> QuerySet:
    return get_image_model().objects.filter(collection__name=collection)
