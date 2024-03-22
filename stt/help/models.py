from django.db.models import QuerySet
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField
from wagtail.models import Page

from stt.base.blocks import DocumentStreamBlock, ImageBlock, PhoneStreamBlock
from stt.base.models import SectionPage, StandardPage, PaginatedPage
from stt.base.rich_text_features import ALL_WITHOUT_FILES


class HelpPage(StandardPage):
    subpage_types: list[str] = []

    class Meta:
        verbose_name = "Стандартная справочная страница"
        verbose_name_plural = "Стандартные справочные страницы"


class PhonesPage(Page):
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
        ],
        null=True,
        blank=True,
        verbose_name="Описание",
        block_counts={
            "description": {"max_num": 1},
            "image_block": {"max_num": 1},
        },
    )
    phones = StreamField(
        [("phones_block", PhoneStreamBlock())],
        null=True,
        blank=True,
        verbose_name="Телефоны",
    )
    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("phones"),
    ]

    class Meta:
        verbose_name = "Страница с телефонами"
        verbose_name_plural = "Страницы с телефонами"


class DocumentSamplePage(Page):
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
        ],
        null=True,
        blank=True,
        verbose_name="Описание",
        block_counts={
            "description": {"max_num": 1},
            "image_block": {"max_num": 1},
        },
    )
    documents = StreamField(
        [("documents_block", DocumentStreamBlock())],
        null=True,
        blank=True,
        verbose_name="Документы",
    )
    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("documents"),
    ]

    class Meta:
        verbose_name = "Страница шаблона документа"
        verbose_name_plural = "Страницы шаблона документа"


class HelpSectionPage(PaginatedPage, SectionPage):
    subpage_types: list[str] = [
        "help.HelpPage",
        "help.PhonesPage",
        "help.DocumentSamplePage",
    ]

    content_panels = SectionPage.content_panels + PaginatedPage.content_panels

    @property
    def elements(self) -> QuerySet:
        return self.get_children().order_by("last_published_at")

    class Meta:
        verbose_name = "Раздел справки"
        verbose_name_plural = "Разделы справки"
