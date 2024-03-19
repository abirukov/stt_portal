from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import CharBlock, RichTextBlock, StructBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page

from stt.base.blocks import ImageBlock
from stt.base.rich_text_features import ALL_WITHOUT_FILES


class TechnologyPage(Page):
    subpage_types: list[str] = []
    body = StreamField(
        [
            (
                "description",
                RichTextBlock(
                    features=ALL_WITHOUT_FILES,
                    label="Текст",
                ),
            ),
            ("image_block", ImageBlock()),
            (
                "embed_block",
                EmbedBlock(
                    help_text="Вставьте ссылку на контент, пример https://www.youtube.com/watch?v=SGJFWirQ3ks",
                    icon="media",
                    template="blocks/embed_block.html",
                    label="Встраиваемый контент",
                ),
            )
        ],
        null=True,
        blank=True,
        verbose_name="О технологии",
    )
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Стандартная страница технологий"
        verbose_name_plural = "Стандартные страницы технологий"


class TechnologySectionPage(Page):
    max_count = 1
    subpage_types = ["technology.TechnologyPage"]
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Фоновое изображение раздела",
        verbose_name="Изображение",
    )
    body = StreamField(
        [
            (
                "description",
                RichTextBlock(
                    features=ALL_WITHOUT_FILES,
                    label="Описание",
                ),
            ),
        ],
        null=True,
        blank=True,
        verbose_name="О разделе",
    )
    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Раздел технологий"
        verbose_name_plural = "Разделы технологий"
