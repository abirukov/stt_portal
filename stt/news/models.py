from django.db.models import QuerySet

from stt.base.models import PaginatedPage, SectionPage, StandardPage


class NewsPage(StandardPage):
    class Meta:
        verbose_name = "Страница новости"
        verbose_name_plural = "Страницы новостей"


class NewsSectionPage(PaginatedPage, SectionPage):
    subpage_types: list[str] = ["news.NewsPage"]

    content_panels = SectionPage.content_panels + PaginatedPage.content_panels

    @property
    def elements(self) -> QuerySet:
        return NewsPage.objects.all()

    class Meta:
        verbose_name = "Раздела новостей"
        verbose_name_plural = "Разделы новостей"
