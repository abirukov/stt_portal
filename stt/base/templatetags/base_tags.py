import datetime
from typing import Any

from django import template
from django.template import RequestContext

from stt.base.models import Holiday

register = template.Library()


@register.inclusion_tag("tags/holiday.html", takes_context=True)
def holiday_tag(context: RequestContext) -> dict[str, Any]:
    today = datetime.date.today()
    holiday = Holiday.objects.filter(
        start_date__gte=today,
        end_date__lte=today,
    ).first()

    return {
        "request": context["request"],
        "holiday": holiday,
    }
