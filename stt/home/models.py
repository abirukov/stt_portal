from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


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

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("hero_text"),
    ]

    def __str__(self) -> str:
        return self.title
