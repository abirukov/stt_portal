from django.forms.utils import flatatt
from django.utils.html import format_html, format_html_join
from django.utils.translation import gettext_lazy as _
from wagtail.models import Page
from wagtailmedia.models import AbstractMedia
from django.apps import apps


def format_video_html(item: AbstractMedia) -> str:
    return format_html(
        "<video width='80%' controls>\n{sources}\n<p>{fallback}</p>\n</video>",
        sources=format_html_join(
            "\n",
            "<source{0}>",
            [[flatatt(s)] for s in item.sources],
        ),
        fallback=_("Your browser does not support the video element."),
    )


def get_real_page_model(page: Page) -> Page | None:
    content_type = page.content_type
    return apps.get_model(
        app_label=content_type.app_label,
        model_name=content_type.model,
    )
