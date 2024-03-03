from wagtail.models import Page


class HomePage(Page):
    max_count = 1
    subpage_types = [
        "gallery.GallerySectionPage",
        "news.NewsSectionPage",
        "knowledge.KnowledgeSectionPage",
    ]
