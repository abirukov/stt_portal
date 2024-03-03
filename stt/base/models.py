from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
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
