from stt.base.models import SectionPage, StandardPage


class TechnologyPage(StandardPage):
    class Meta:
        verbose_name = "Стандартная страница технологий"
        verbose_name_plural = "Стандартные страницы технологий"


class TechnologySectionPage(SectionPage):
    subpage_types = ["technology.TechnologyPage"]

    class Meta:
        abstract = False
        verbose_name = "Раздел технологий"
        verbose_name_plural = "Разделы технологий"
