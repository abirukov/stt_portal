from wagtail.models import Page


class EventPage(Page):
    subpage_types = []

    class Meta:
        verbose_name = "Страница события"
        verbose_name_plural = "Страницы событий"


class EventSectionPage(Page):
    max_count = 1
    subpage_types = ["event.EventPage"]

    class Meta:
        verbose_name = "Раздел событий"
        verbose_name_plural = "Разделы событий"
