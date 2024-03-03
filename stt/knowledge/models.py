from wagtail.models import Page


class KnowledgeSectionPage(Page):
    max_count = 1
    subpage_types = ["knowledge.KnowledgePage"]


class KnowledgePage(Page):
    pass
