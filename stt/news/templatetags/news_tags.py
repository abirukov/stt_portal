from typing import Any

from django import template
from django.template import RequestContext

from stt.news.models import NewsPage

register = template.Library()


# Retrieves a single gallery item and returns a gallery of images


@register.inclusion_tag("tags/news_section.html", takes_context=True)
def news_section(context: RequestContext) -> dict[str, Any]:
    news = NewsPage.objects.all()
    return {
        "news": news,
        "request": context["request"],
    }
