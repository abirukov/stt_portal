from django.db import models
from django.db.models import QuerySet
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.search import index

from stt.base.models import PaginatedPage, SectionPage, StandardPage


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
    gallery = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Страница галереи",
        help_text="Выберите связанную страницу галереи",
    )

    content_panels = StandardPage.content_panels + [
        FieldPanel("start"),
        FieldPanel("end"),
        PageChooserPanel("gallery", "gallery.GalleryPage"),
    ]

    search_fields = StandardPage.search_fields + [
        index.SearchField("start"),
        index.SearchField("end"),
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
