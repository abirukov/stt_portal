from django import template
from django.template import RequestContext
from wagtail.images import get_image_model

register = template.Library()


@register.inclusion_tag("tags/gallery_section.html", takes_context=True)
def gallery_section(context: RequestContext) -> RequestContext:
    for element in context["elements"]:
        if element.skin is None:
            new_skin = get_image_model().objects.filter(collection__name=element.collection).first()
            if new_skin is not None:
                element.skin = new_skin
                element.save()

    return context
