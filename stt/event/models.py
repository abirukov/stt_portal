from django.db import models
from wagtail.models import Page

from stt.base.models import SectionPage


class EventPage(Page):
    subpage_types = []

    class Meta:
        verbose_name = "Страница события"
        verbose_name_plural = "Страницы событий"


class EventSectionPage(SectionPage):
    max_count = 1
    subpage_types = ["event.EventPage"]

    class Meta:
        verbose_name = "Раздел событий"
        verbose_name_plural = "Разделы событий"
