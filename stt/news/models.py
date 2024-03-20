from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField
from wagtail.models import Page

from stt.base.models import StandardPage, SectionPage


class NewsPage(StandardPage):

    class Meta:
        verbose_name = "Страница новости"
        verbose_name_plural = "Страницы новостей"


class NewsSectionPage(SectionPage):
    subpage_types: list[str] = ["news.NewsPage"]

    class Meta:
        verbose_name = "Раздела новостей"
        verbose_name_plural = "Разделы новостей"
