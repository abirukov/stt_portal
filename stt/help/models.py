from wagtail.models import Page

from stt.base.models import SectionPage


class HelpPage(Page):
    subpage_types = []

    class Meta:
        verbose_name = "Стандартная справочная страница"
        verbose_name_plural = "Стандартные справочные страницы"


class HelpSectionPage(SectionPage):
    max_count = 1
    subpage_types = ["help.HelpPage"]

    class Meta:
        verbose_name = "Раздел справки"
        verbose_name_plural = "Разделы справки"
