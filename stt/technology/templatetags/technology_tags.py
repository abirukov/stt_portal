from django import template
from django.template import RequestContext

register = template.Library()


@register.inclusion_tag("technology/tags/technology_section.html", takes_context=True)
def technology_section(context: RequestContext) -> RequestContext:
    return context
