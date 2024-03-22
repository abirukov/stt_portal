from django.db.models import QuerySet

from stt.base.models import SectionPage, StandardPage, PaginatedPage


class TechnologyPage(StandardPage):
    class Meta:
        verbose_name = "Стандартная страница технологий"
        verbose_name_plural = "Стандартные страницы технологий"


class TechnologySectionPage(PaginatedPage, SectionPage):
    subpage_types = ["technology.TechnologyPage"]

    content_panels = SectionPage.content_panels + PaginatedPage.content_panels

    @property
    def elements(self) -> QuerySet:
        return TechnologyPage.objects.all()

    class Meta:
        abstract = False
        verbose_name = "Раздел технологий"
        verbose_name_plural = "Разделы технологий"
