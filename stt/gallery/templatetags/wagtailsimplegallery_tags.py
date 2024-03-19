import os
import re
from typing import Any, Collection

from django import template
from django.conf import settings
from django.core.files import File

from stt.gallery.models import get_gallery_images

register = template.Library()


@register.inclusion_tag("gallery/simple_gallery.html")
def simple_gallery(
    collection: Collection | None = None,
    image_limit: int | None = None,
    use_lightbox: bool = True,
) -> dict[str, Any] | None:
    if not collection:
        return None
    images = get_gallery_images(collection)
    if image_limit:
        images = images[: int(image_limit)]
    return {"gallery_images": images, "use_lightbox": use_lightbox}


@register.filter
def original_url(image: File) -> str:
    return os.path.join(settings.MEDIA_URL, str(image.file))


@register.filter
def hide_num_order(title: str) -> str:
    number_match = re.match(r"^.*?\[[^\d]*(\d+)[^\d]*\].*$", title)
    if number_match:
        number = number_match.group(1)
        return title.replace("[{}]".format(number), "")
    return title
