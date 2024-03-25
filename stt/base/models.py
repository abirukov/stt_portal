from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.db.models import QuerySet
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtailmedia.blocks import AudioChooserBlock

from stt.base.blocks import ImageBlock, SttVideoChooserBlock
from stt.base.rich_text_features import ALL_WITHOUT_FILES


@register_snippet
class Holiday(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        help_text="Введите название праздника",
    )
    congratulatory_text = RichTextField(
        verbose_name="Текст поздравления",
        help_text="Введите текст поздравления",
    )
    start_date = models.DateField(
        null=False,
        verbose_name="Дата начала поздравления",
        help_text="Выберите дату начала поздравления",
    )
    end_date = models.DateField(
        verbose_name="Дата окончания поздравления",
        help_text="Выберите дату окончания поздравления(если праздник однодневный необязательно)",
    )
    panels = [
        FieldPanel("title"),
        FieldPanel("congratulatory_text"),
        FieldPanel("start_date"),
        FieldPanel("end_date"),
    ]

    class Meta:
        verbose_name = "Праздник"
        verbose_name_plural = "Праздники"

    def __str__(self) -> str:
        return "Праздник"


class PaginatedPage(RoutablePageMixin, Page):
    elements_per_page = models.IntegerField(
        default=12,
        verbose_name="Количество элементов на странице",
        help_text="Сколько элементов будет отображаться на странице",
    )

    content_panels = [FieldPanel("elements_per_page")]

    def get_context(
        self,
        request: WSGIRequest,
        *args: Any,
        **kwargs: Any,
    ) -> dict[str, Page]:
        elements = self.elements
        context = super(PaginatedPage, self).get_context(request)
        page = request.GET.get("page")
        paginator = Paginator(elements, self.elements_per_page)
        try:
            elements = paginator.page(page)
        except PageNotAnInteger:
            elements = paginator.page(1)
        except EmptyPage:
            elements = paginator.page(paginator.num_pages)
        context["elements"] = elements
        context["elements_per_page"] = self.elements_per_page
        return context

    @property
    def elements(self) -> QuerySet:
        return QuerySet()

    class Meta:
        abstract = True


class StandardPage(Page):
    subpage_types: list[str] = []
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Изображение",
        verbose_name="Изображение",
    )
    body = StreamField(
        [
            (
                "description",
                RichTextBlock(
                    features=ALL_WITHOUT_FILES,
                    label="Текст",
                ),
            ),
            ("image_block", ImageBlock()),
            (
                "embed_block",
                EmbedBlock(
                    help_text="Вставьте ссылку на контент, пример https://www.youtube.com/watch?v=SGJFWirQ3ks",
                    icon="media",
                    template="base/blocks/embed_block.html",
                    label="Встраиваемый контент",
                ),
            ),
            ("audio", AudioChooserBlock(label="Аудио")),
            ("video", SttVideoChooserBlock(label="Видео")),
        ],
        null=True,
        blank=True,
        verbose_name="Контент",
    )
    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("body"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]

    class Meta:
        abstract = True


class SectionPage(Page):
    max_count = 1
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Фоновое изображение раздела",
        verbose_name="Изображение",
    )
    body = StreamField(
        [
            (
                "description",
                RichTextBlock(
                    features=ALL_WITHOUT_FILES,
                    label="Описание",
                ),
            ),
        ],
        null=True,
        blank=True,
        verbose_name="О разделе",
    )
    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("body"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]

    class Meta:
        abstract = True
