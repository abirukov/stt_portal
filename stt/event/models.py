from stt.base.models import SectionPage, StandardPage


class EventPage(StandardPage):
    class Meta:
        verbose_name = "Страница события"
        verbose_name_plural = "Страницы событий"


class EventSectionPage(SectionPage):
    subpage_types = ["event.EventPage"]

    class Meta:
        verbose_name = "Раздел событий"
        verbose_name_plural = "Разделы событий"
