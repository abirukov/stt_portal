from django import template
from django.template import RequestContext
from wagtail.images import get_image_model

register = template.Library()


@register.inclusion_tag("tags/gallery_section.html", takes_context=True)
def gallery_section(context: RequestContext) -> RequestContext:
    for element in context["elements"]:
        if element.skin is not None:
            element.real_image = element.skin
        else:
            element.real_image = get_image_model().objects.filter(collection__name=element.collection).first()

    return context
