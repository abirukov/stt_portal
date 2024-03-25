from wagtail.blocks import CharBlock, PageChooserBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock

from stt.base.blocks import SttVideoChooserBlock


class HeroSlide(StructBlock):
    image = ImageChooserBlock(required=True, label="Изображение")
    heading = CharBlock(required=True, label="Заголовок")
    text = CharBlock(required=False, label="Текст")
    page_more = PageChooserBlock(required=False, label="Страница подробнее")
    video = SttVideoChooserBlock(required=False, label="Видео")

    class Meta:
        icon = "resubmit"
        template = "home/blocks/hero_slide.html"
        label = "Слайд для главной страницы"
