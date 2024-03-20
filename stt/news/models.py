from stt.base.models import SectionPage, StandardPage


class NewsPage(StandardPage):
    class Meta:
        verbose_name = "Страница новости"
        verbose_name_plural = "Страницы новостей"


class NewsSectionPage(SectionPage):
    subpage_types: list[str] = ["news.NewsPage"]

    class Meta:
        verbose_name = "Раздела новостей"
        verbose_name_plural = "Разделы новостей"
