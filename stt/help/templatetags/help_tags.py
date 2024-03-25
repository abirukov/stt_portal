from django import template
from django.template import RequestContext

register = template.Library()


@register.inclusion_tag("help/tags/help_section.html", takes_context=True)
def help_section(context: RequestContext) -> RequestContext:
    return context


def mobile_phone_number(value: str) -> str:
    return "+7 (%s) %s-%s-%s" % (value[0:3], value[3:6], value[6:8], value[8:10])


def city_phone_number(value: str) -> str:
    return "+7 (4812) %s-%s-%s" % (value[0:2], value[2:4], value[4:6])


def internal_phone_number(value: str) -> str:
    return f"Вн. {value}"


register.filter("mobile_phone_number", mobile_phone_number)
register.filter("city_phone_number", city_phone_number)
register.filter("internal_phone_number", internal_phone_number)
