from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField
from wagtail.models import Page


class NewsPage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="News image",
    )
    body = StreamField(
        [
            ("text", RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("body"),
    ]
    subpage_types: list[str] = []

    class Meta:
        verbose_name = "Страница новости"
        verbose_name_plural = "Страницы новостей"


class NewsSectionPage(Page):
    max_count = 1
    subpage_types: list[str] = ["news.NewsPage"]

    class Meta:
        verbose_name = "Раздела новостей"
        verbose_name_plural = "Разделы новостей"
