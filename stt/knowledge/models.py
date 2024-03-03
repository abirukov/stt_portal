from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField
from wagtail.models import Page


class KnowledgeSectionPage(Page):
    max_count = 1
    subpage_types = ["knowledge.KnowledgePage"]


class KnowledgePage(Page):
    body = StreamField([
            ('text', RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    subpage_types = []
