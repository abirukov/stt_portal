from typing import Any

from django.db.models import QuerySet, signals
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock, StructValue
from wagtail.documents.models import Document
from wagtail.fields import StreamField
from wagtail.models import Page, PageBase
from wagtail.search import index

from stt.base.blocks import ImageBlock
from stt.base.models import PaginatedPage, SectionPage, StandardPage
from stt.base.rich_text_features import ALL_WITHOUT_FILES
from stt.base.utils import convert_to_pdf, create_document
from stt.help.blocks import DocumentBlock, PhoneStreamBlock


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

    search_fields = Page.search_fields + [  # Inherit search_fields from Page
        index.SearchField('body'),
        index.SearchField('phones'),
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
        [("documents_block", DocumentBlock())],
        null=True,
        blank=True,
        verbose_name="Документы",
    )
    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("documents"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('documents'),
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


def pre_save_document_sample_page(
    sender: PageBase,
    instance: DocumentSamplePage,
    **kwargs: Any,
) -> None:
    documents = instance.documents
    for document in documents:
        handle_document(document.value)


def handle_document(document: StructValue) -> None:
    document_fields = ["document", "document_example"]
    for document_field in document_fields:
        value = document[document_field]
        pdf_value = document[f"{document_field}_pdf"]
        if value is None:
            continue
        if value.file_extension in ["doc", "docx"] and pdf_value is None:
            sample_pdf = create_sample_pdf(value)
            assert sample_pdf
            document[f"{document_field}_pdf"] = sample_pdf
        elif value.file_extension == "pdf" and pdf_value is None:
            document[f"{document_field}_pdf"] = value


def create_sample_pdf(block_value: Document) -> Document | None:
    pdf_file_path = convert_to_pdf(block_value.file.path)
    if pdf_file_path is None:
        return None

    return create_document(
        pdf_file_path,
        f" PDF {block_value.title}",
    )


signals.pre_save.connect(
    receiver=pre_save_document_sample_page,
    sender=DocumentSamplePage,
)
