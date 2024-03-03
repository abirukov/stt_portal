from typing import Any

from django import template
from django.template import RequestContext
from wagtail.models import Collection

register = template.Library()


@register.inclusion_tag("tags/home_hero.html", takes_context=True)
def home_hero_tag(context: RequestContext, collection_name: str) -> dict[str, Any]:
    images = Collection.objects.filter(name=collection_name)
    return {
        "request": context["request"],
        "images": images,
    }
