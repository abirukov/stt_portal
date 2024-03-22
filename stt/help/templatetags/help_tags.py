from django import template
from django.template import RequestContext

register = template.Library()


@register.inclusion_tag("tags/help_section.html", takes_context=True)
def help_section(context: RequestContext) -> RequestContext:
    return context