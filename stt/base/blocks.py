from typing import Any

from wagtail.blocks import CharBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import VideoChooserBlock
from wagtailmedia.models import Media

from stt.base.utils import format_video_html


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True, label="Изображение")
    caption = CharBlock(required=False, label="Подпись")

    class Meta:
        icon = "image"
        template = "base/blocks/image_block.html"
        label = "Блок изображения"


class SttVideoChooserBlock(VideoChooserBlock):
    def render_basic(self, value: Media, context: Any = None) -> str:
        if not value:
            return ""

        if value.type != self.media_type:
            return ""

        return format_video_html(value)
