from django import template
from django.template import RequestContext

register = template.Library()


@register.inclusion_tag("tags/news_section.html", takes_context=True)
def news_section(context: RequestContext) -> RequestContext:
    return context
