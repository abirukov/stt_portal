from typing import Any

from django.db.models import QuerySet, signals
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.documents.models import Document
from wagtail.fields import StreamField
from wagtail.models import Page, PageBase

from stt.base.blocks import ImageBlock
from stt.base.models import PaginatedPage, SectionPage, StandardPage
from stt.base.rich_text_features import ALL_WITHOUT_FILES
from stt.base.utils import convert_to_pdf, create_document
from stt.help.blocks import DocumentStreamBlock, PhoneStreamBlock


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


def pre_save_document_sample_page(
    sender: PageBase,
    instance: DocumentSamplePage,
    **kwargs: Any,
) -> None:
    documents = instance.documents
    raw_data = documents.get_prep_value()
    is_changed = False
    for index, document_block in enumerate(documents):
        for block in document_block.value:
            if block.block_type == "document" or block.block_type == "document_example":
                pdf_value = get_block_value(document_block, f"{block.block_type}_pdf")
                if block.value.file_extension in ["doc", "docx"] and pdf_value is None:
                    sample_pdf = create_sample_pdf(block.value)
                    assert sample_pdf
                    raw_data[index]["value"].append(
                        {"type": f"{block.block_type}_pdf", "value": sample_pdf.id},
                    )
                    is_changed = True
                elif block.value.file_extension == "pdf" and pdf_value is None:
                    raw_data[index]["value"].append(
                        {"type": f"{block.block_type}_pdf", "value": block.value.id},
                    )
                    is_changed = True

    if is_changed:
        instance.documents = raw_data


def create_sample_pdf(block_value: Document) -> Document | None:
    pdf_file_path = convert_to_pdf(block_value.file.path)
    if pdf_file_path is None:
        return None

    return create_document(
        pdf_file_path,
        f" PDF {block_value.title}",
    )


def get_block_value(document_block: Any, document_type: str) -> Any:
    result = None
    for block in document_block.value:
        if block.block_type == document_type:
            result = block.value

    return result


signals.pre_save.connect(
    receiver=pre_save_document_sample_page,
    sender=DocumentSamplePage,
)
