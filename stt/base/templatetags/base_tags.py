from typing import Any

from django import template
from django.template import RequestContext

from stt.base.models import Footer

register = template.Library()


@register.inclusion_tag("tags/footer.html", takes_context=True)
def footer_tag(context: RequestContext) -> dict[str, Any]:
    return {
        "request": context["request"],
        "footer": Footer.objects.first(),
    }
