from typing import Any

from django import template
from django.template import RequestContext
from wagtail.images.models import Image
from wagtail.models import Collection

from stt.gallery.models import GalleryPage

register = template.Library()


# Retrieves a single gallery item and returns a gallery of images
@register.inclusion_tag("tags/gallery.html", takes_context=True)
def gallery(context: RequestContext, gallery: Collection) -> dict[str, Any]:
    images = Image.objects.filter(collection=gallery)

    return {
        "images": images,
        "request": context["request"],
    }


@register.inclusion_tag("tags/gallery_section.html", takes_context=True)
def gallery_section(context: RequestContext) -> dict[str, Any]:
    galleries = GalleryPage.objects.all()
    return {
        "galleries": galleries,
        "request": context["request"],
    }
