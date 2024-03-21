from typing import Any

from django import template
from django.template import RequestContext

from stt.event.models import EventPage

register = template.Library()


@register.inclusion_tag("tags/event_section.html", takes_context=True)
def event_section(context: RequestContext) -> RequestContext:
    return context