from wagtail.blocks import CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True, label="Изображение")
    caption = CharBlock(required=False, label="Подпись")

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"
        label = "Блок изображения"
