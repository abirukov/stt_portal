from typing import Any

from django import template
from django.template import RequestContext

from stt.gallery.models import GalleryPage

register = template.Library()


@register.inclusion_tag("tags/gallery_section.html", takes_context=True)
def gallery_section(context: RequestContext) -> dict[str, Any]:
    galleries = GalleryPage.objects.all()
    return {
        "galleries": galleries,
        "request": context["request"],
    }
