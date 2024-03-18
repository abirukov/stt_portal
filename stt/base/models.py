from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


@register_snippet
class Footer(models.Model):
    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футеры"

    body = RichTextField()

    panels = [
        FieldPanel("body"),
    ]

    def __str__(self) -> str:
        return "Футер"


class SectionPage(Page):
    menu_order_index = models.IntegerField(verbose_name="Индекс сортировки", default=-1)

    class Meta:
        abstract = True

