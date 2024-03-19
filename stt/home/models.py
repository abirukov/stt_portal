from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from stt.base.blocks import BaseStreamBlock


class HomePage(Page):
    max_count = 1
    subpage_types = [
        "event.EventSectionPage",
        "gallery.GallerySectionPage",
        "help.HelpSectionPage",
        "news.NewsSectionPage",
        "technology.TechnologySectionPage",
    ]

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        max_length=255,
        help_text="Write an introduction for the bakery",
        null=True,
    )

    # Body section of the HomePage
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Home content block",
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("hero_text"),
        FieldPanel("body"),
    ]

    def __str__(self) -> str:
        return self.title
