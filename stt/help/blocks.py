from wagtail.blocks import CharBlock, RegexBlock, StreamBlock, StructBlock
from wagtail.documents.blocks import DocumentChooserBlock


class MobilePhoneBlock(StructBlock):
    phone = RegexBlock(
        required=True,
        regex=r"^[0-9]{10}$",
        max_length=10,
        min_length=10,
        error_messages={"invalid": "Не верно введен номер"},
        help_text="Ввод без +7 в формате 9008887766",
        label="Мобильный номер телефона",
    )
    workplace = CharBlock(required=True, label="Рабочее место")
    employee = CharBlock(required=False, label="Работник")

    class Meta:
        icon = "mobile-alt"
        template = "blocks/mobile_phone_block.html"
        label = "Блок мобильного телефона"


class CityPhoneBlock(MobilePhoneBlock):
    phone = RegexBlock(
        required=True,
        regex=r"^[0-9]{6}$",
        max_length=6,
        min_length=6,
        error_messages={"invalid": "Не верно введен номер"},
        help_text="Ввод без +74812 в формате 887766",
        label="Городской номер телефона",
    )

    class Meta:
        icon = "globe"
        template = "blocks/city_phone_block.html"
        label = "Блок городского телефона"


class InternalPhoneBlock(MobilePhoneBlock):
    phone = RegexBlock(
        required=True,
        regex=r"^[0-9]{3}$",
        max_length=3,
        min_length=3,
        error_messages={"invalid": "Не верно введен номер"},
        help_text="Ввод в формате 123",
        label="Внутренний номер телефона",
    )

    class Meta:
        icon = "home"
        template = "blocks/internal_phone_block.html"
        label = "Блок внутреннего телефона"


class PhoneStreamBlock(StreamBlock):
    header = CharBlock(required=True, label="Название группы")
    mobile_phone = MobilePhoneBlock()
    city_phone = CityPhoneBlock()
    internal_phone = InternalPhoneBlock()

    class Meta:
        icon = "mobile-alt"
        template = "blocks/phone_stream_block.html"
        label = "Блок телефонов"
        block_counts = {
            "header": {"min_num": 1, "max_num": 1},
        }


class DocumentBlock(StructBlock):
    header = CharBlock(required=False, label="Название документа")
    document = DocumentChooserBlock(required=True, label="Оригинал документа")
    document_pdf = DocumentChooserBlock(required=False, label="PDF превью (если пусто генерируется автоматически)")
    document_example = DocumentChooserBlock(
        required=False,
        label="Пример заполнения документа",
    )
    document_example_pdf = DocumentChooserBlock(
        required=False,
        label="PDF превью примера (если пусто генерируется автоматически)",
    )

    class Meta:
        icon = "doc-full"
        template = "blocks/document_stream_block.html"
        label = "Блок документа"
