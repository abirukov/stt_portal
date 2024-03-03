from wagtail.models import Page


class NewsSectionPage(Page):
    max_count = 1
    subpage_types = ["news.NewsPage"]


class NewsPage(Page):
    pass
