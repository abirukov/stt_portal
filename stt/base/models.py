from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from wagtailmedia.blocks import AudioChooserBlock

from stt.base.blocks import ImageBlock, SttVideoChooserBlock
from stt.base.rich_text_features import ALL_WITHOUT_FILES


@register_snippet
class Holiday(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        help_text="Введите название праздника",
    )
    congratulatory_text = RichTextField(
        verbose_name="Текст поздравления",
        help_text="Введите текст поздравления",
    )
    start_date = models.DateField(
        null=False,
        verbose_name="Дата начала поздравления",
        help_text="Выберите дату начала поздравления",
    )
    end_date = models.DateField(
        verbose_name="Дата окончания поздравления",
        help_text="Выберите дату окончания поздравления(если праздник однодневный необязательно)",
    )
    panels = [
        FieldPanel("title"),
        FieldPanel("congratulatory_text"),
        FieldPanel("start_date"),
        FieldPanel("end_date"),
    ]

    class Meta:
        verbose_name = "Праздник"
        verbose_name_plural = "Праздники"

    def __str__(self) -> str:
        return "Праздник"


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
            ("video", SttVideoChooserBlock(label="Видео")),
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
