from typing import Any, Collection

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail.fields import RichTextField
from wagtail.images import get_image_model
from wagtail.images.models import Image
from wagtail.models import Page

IMAGE_ORDER_TYPES = (
    (1, "Image title"),
    (2, "Newest image first"),
)


class GalleryPage(RoutablePageMixin, Page):
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
    images_per_page = models.IntegerField(
        default=8,
        verbose_name=_("Images per page"),
        help_text=_("How many images there should be on one page."),
    )
    use_lightbox = models.BooleanField(
        verbose_name=_("Use lightbox"),
        default=True,
        help_text=_("Use lightbox to view larger images when clicking the thumbnail."),
    )
    order_images_by = models.IntegerField(choices=IMAGE_ORDER_TYPES, default=1)

    content_panels = Page.content_panels + [
        FieldPanel("intro_title", classname="full title"),
        FieldPanel("intro_text", classname="full title"),
        FieldPanel("collection"),
        FieldPanel("images_per_page", classname="full title"),
        FieldPanel("use_lightbox"),
        FieldPanel("order_images_by"),
    ]

    @property
    def images(self) -> Collection:
        return get_gallery_images(self.collection.name, self)

    def get_context(
        self,
        request: WSGIRequest,
        *args: Any,
        **kwargs: Any,
    ) -> dict[str, Page]:
        images = self.images
        context = super(GalleryPage, self).get_context(request)
        page = request.GET.get("page")
        paginator = Paginator(images, self.images_per_page)
        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            images = paginator.page(paginator.num_pages)
        context["gallery_images"] = images
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


def get_gallery_images(
    collection: Collection,
    page: GalleryPage | None = None,
):
    images = get_image_model().objects.filter(collection__name=collection)
    if page:
        if page.order_images_by == 1:
            images = images.order_by("title")
        elif page.order_images_by == 2:
            images = images.order_by("-created_at")
    return images
