from django import template
from django.db.models import Q
from django.template import RequestContext
from django.utils import timezone

from stt.event.models import EventPage
from stt.news.models import NewsPage

register = template.Library()


@register.inclusion_tag("home/tags/event_section.html", takes_context=True)
def home_event_section(context: RequestContext) -> RequestContext:
    now = timezone.now()
    context["events"] = EventPage.objects.filter(
        Q(start__gte=now) | Q(start__lt=now, end__isnull=False, end__gte=now),
    )
    return context


@register.inclusion_tag("home/tags/news_section.html", takes_context=True)
def home_news_section(context: RequestContext) -> RequestContext:
    context["news"] = NewsPage.objects.all()[:10]
    return context
