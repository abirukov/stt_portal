from typing import Any

from django import template
from django.template import RequestContext
from wagtail.models import Page, Site

register = template.Library()

# https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/


@register.simple_tag(takes_context=True)
def get_site_root(context: RequestContext) -> Any:
    return Site.find_for_request(context["request"]).root_page


@register.inclusion_tag("tags/top_menu.html", takes_context=True)
def top_menu(context: RequestContext, parent: Page) -> dict[str, Any]:
    menuitems = parent.get_children().in_menu()
    return {
        "menuitems": menuitems,
        "request": context["request"],
    }
