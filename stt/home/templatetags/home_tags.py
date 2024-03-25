
from django import template
from django.template import RequestContext
from django.db.models import Q
from django.utils import timezone

from stt.event.models import EventPage

register = template.Library()


@register.inclusion_tag("home/tags/event_section.html", takes_context=True)
def event_section(context: RequestContext) -> RequestContext:
    now = timezone.now()
    context["events"] = EventPage.objects.filter(
        Q(start__gte=now)
        | Q(start__lt=now, end__isnull=False, end__gte=now)
    )
    return context
