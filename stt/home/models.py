from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from stt.home.blocks import HeroSlide


class HomePage(Page):
    max_count = 1
    subpage_types = [
        "event.EventSectionPage",
        "gallery.GallerySectionPage",
        "help.HelpSectionPage",
        "news.NewsSectionPage",
        "technology.TechnologySectionPage",
    ]

    hero_slider = StreamField(
        [("slide", HeroSlide(label="Слайд"))],
        null=True,
        blank=True,
        verbose_name="Слайдер",
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_slider"),
    ]

    def __str__(self) -> str:
        return self.title
