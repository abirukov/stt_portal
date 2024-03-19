from wagtail.models import Page


class HelpPage(Page):
    subpage_types: list[str] = []

    class Meta:
        verbose_name = "Стандартная справочная страница"
        verbose_name_plural = "Стандартные справочные страницы"


class HelpSectionPage(Page):
    max_count = 1
    subpage_types: list[str] = ["help.HelpPage"]

    class Meta:
        verbose_name = "Раздел справки"
        verbose_name_plural = "Разделы справки"
