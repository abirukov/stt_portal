from django.db import models
from django.db.models import QuerySet
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from stt.base.models import SectionPage, StandardPage, PaginatedPage


class EventPage(StandardPage):
    start = models.DateTimeField(
        verbose_name="Начало события",
        help_text="Выберите дату и время начала события",
    )
    end = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Окончание события",
        help_text="Выберите дату и время окончания события (необязательно)",
    )

    content_panels = StandardPage.content_panels + [
        FieldPanel("start"),
        FieldPanel("end"),
    ]

    class Meta:
        verbose_name = "Страница события"
        verbose_name_plural = "Страницы событий"


class EventSectionPage(PaginatedPage, SectionPage):
    subpage_types = ["event.EventPage"]

    content_panels = SectionPage.content_panels + PaginatedPage.content_panels

    @property
    def elements(self) -> QuerySet:
        return EventPage.objects.all()

    class Meta:
        verbose_name = "Раздел событий"
        verbose_name_plural = "Разделы событий"
