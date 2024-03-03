from wagtail.models import Page


class GalleryPage(Page):
    pass


class GallerySectionPage(Page):
    max_count = 1
    subpage_types = ["gallery.GalleryPage"]
    restriction_type = 'login'

