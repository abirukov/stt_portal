from django.forms.utils import flatatt
from django.utils.html import format_html, format_html_join
from django.utils.translation import gettext_lazy as _
from wagtailmedia.models import AbstractMedia


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
