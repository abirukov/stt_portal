from typing import Any

from django import template
from django.template import RequestContext
from wagtail.models import Page, Site

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context: RequestContext) -> Any:
    return Site.find_for_request(context["request"]).root_page


@register.inclusion_tag("tags/top_menu.html", takes_context=True)
def top_menu(
    context: RequestContext,
    parent: Page,
    calling_page: Page | None = None,
) -> dict[str, Any]:
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.active = (
            calling_page.url_path.startswith(menuitem.url_path)
            if calling_page
            else False
        )
    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        "request": context["request"],
    }


@register.inclusion_tag("tags/breadcrumbs.html", takes_context=True)
def breadcrumbs(context: RequestContext) -> dict[str, Any]:
    self = context.get("self")
    if self is None or self.depth <= 2:
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(self, inclusive=True).filter(depth__gt=1)
    return {
        "page": self,
        "ancestors": ancestors,
        "request": context["request"],
    }
