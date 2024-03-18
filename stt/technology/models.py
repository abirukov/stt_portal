from wagtail.models import Page


class TechnologyPage(Page):
    subpage_types = []

    class Meta:
        verbose_name = "Стандартная страница технологий"
        verbose_name_plural = "Стандартные страницы технологий"


class TechnologySectionPage(Page):
    max_count = 1
    subpage_types = ["technology.TechnologyPage"]

    class Meta:
        verbose_name = "Раздел технологий"
        verbose_name_plural = "Разделы технологий"
