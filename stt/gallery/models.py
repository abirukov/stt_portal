from typing import Any, Collection

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model
from wagtail.models import Page
from wagtail.search import index

from stt.base.models import PaginatedPage


class GalleryPage(PaginatedPage):
    subpage_types: list[str] = []
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
    content_panels = Page.content_panels + [
        FieldPanel("collection"),
        FieldPanel("intro_title"),
        FieldPanel("intro_text"),
    ]
    search_fields = Page.search_fields + [
        index.SearchField("intro_title"),
        index.SearchField("intro_text"),
    ]

    def get_context(
        self,
        request: WSGIRequest,
        *args: Any,
        **kwargs: Any,
    ) -> dict[str, Page]:
        elements = get_gallery_images(self.collection.name)
        context = super(GalleryPage, self).get_context(request)
        page = request.GET.get("page")
        paginator = Paginator(elements, self.elements_per_page)
        try:
            elements = paginator.page(page)
        except PageNotAnInteger:
            elements = paginator.page(1)
        except EmptyPage:
            elements = paginator.page(paginator.num_pages)
        context["elements"] = elements
        return context

    class Meta:
        verbose_name = "Страница галереи"
        verbose_name_plural = "Страницы галереи"


class GallerySectionPage(Page):
    max_count = 1
    subpage_types = ["gallery.GalleryPage"]

    class Meta:
        verbose_name = "Раздел галереи"
        verbose_name_plural = "Разделы галереи"


def get_gallery_images(collection: Collection) -> QuerySet:
    return get_image_model().objects.filter(collection__name=collection)
