from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from wagtailmedia.blocks import AudioChooserBlock, VideoChooserBlock

from stt.base.blocks import ImageBlock
from stt.base.rich_text_features import ALL_WITHOUT_FILES


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


class StandardPage(Page):
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
            ),
            ("audio", AudioChooserBlock(label="Аудио")),
            ("video", VideoChooserBlock(label="Видео")),
        ],
        null=True,
        blank=True,
        verbose_name="Контент",
    )
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        abstract = True


class SectionPage(Page):
    max_count = 1
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
        abstract = True
