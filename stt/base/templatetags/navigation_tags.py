from typing import Any

from django import template
from django.template import RequestContext
from wagtail.models import Page, Site

from stt.base.utils import get_real_page_model

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context: RequestContext) -> Any:
    return Site.find_for_request(context["request"]).root_page


@register.inclusion_tag("base/tags/top_menu.html", takes_context=True)
def top_menu(
    context: RequestContext,
    parent: Page,
    calling_page: Page | None = None,
) -> dict[str, Any]:
    menuitems = parent.get_children().live().in_menu()
    self = context.get("self")
    if self is None or self.depth <= 2:
        calling_section = self
    else:
        calling_section = Page.objects.ancestor_of(self, inclusive=True).filter(depth__gt=1)[1]

    for menuitem in menuitems:
        menuitem.active = (
            calling_page.url_path.startswith(menuitem.url_path)
            if calling_page
            else False
        )
    return {
        "calling_page": calling_page,
        "calling_section": calling_section,
        "menuitems": menuitems,
        "request": context["request"],
    }


@register.inclusion_tag("base/tags/mobile_menu.html", takes_context=True)
def mobile_menu(
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


@register.inclusion_tag("base/tags/breadcrumbs.html", takes_context=True)
def breadcrumbs(context: RequestContext) -> dict[str, Any]:
    self = context.get("self")
    if self is None or self.depth <= 2:
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(self, inclusive=True).filter(depth__gt=1)
    breadcrumbs_image = None
    if len(ancestors) > 1:
        section_page = ancestors[1]
        section_model = get_real_page_model(section_page)
        section = section_model.objects.filter(id=section_page.id).first()
        if section:
            breadcrumbs_image = section.image
    return {
        "page": self,
        "ancestors": ancestors,
        "breadcrumbs_image": breadcrumbs_image,
        "request": context["request"],
    }


@register.inclusion_tag("base/tags/pagination.html", takes_context=True)
def pagination(context: RequestContext) -> RequestContext:
    return context
