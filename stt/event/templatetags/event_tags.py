from django import template
from django.template import RequestContext

register = template.Library()


@register.inclusion_tag("event/tags/event_section.html", takes_context=True)
def event_section(context: RequestContext) -> RequestContext:
    return context
