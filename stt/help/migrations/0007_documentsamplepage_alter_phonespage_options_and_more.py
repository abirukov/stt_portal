# Generated by Django 5.0.2 on 2024-03-19 09:47

import django.db.models.deletion
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("help", "0006_alter_phonespage_phones"),
        ("wagtailcore", "0091_remove_revision_submitted_for_moderation"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocumentSamplePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "description",
                                wagtail.blocks.RichTextBlock(
                                    features=[
                                        "h2",
                                        "h3",
                                        "h4",
                                        "h5",
                                        "h6",
                                        "bold",
                                        "italic",
                                        "link",
                                        "code",
                                        "blockquote",
                                        "document-link",
                                    ],
                                    label="Текст",
                                ),
                            ),
                            (
                                "image_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                label="Изображение", required=True
                                            ),
                                        ),
                                        (
                                            "caption",
                                            wagtail.blocks.CharBlock(
                                                label="Подпись", required=False
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ],
                        blank=True,
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "phones",
                    wagtail.fields.StreamField(
                        [
                            (
                                "phone_block",
                                wagtail.blocks.StreamBlock(
                                    [
                                        (
                                            "header",
                                            wagtail.blocks.CharBlock(
                                                label="Название группы", required=False
                                            ),
                                        ),
                                        (
                                            "mobile_phone",
                                            wagtail.blocks.StructBlock(
                                                [
                                                    (
                                                        "phone",
                                                        wagtail.blocks.RegexBlock(
                                                            error_messages={
                                                                "invalid": "Не верно введен номер"
                                                            },
                                                            help_text="Ввод без +7 в формате 9008887766",
                                                            label="Мобильный номер телефона",
                                                            max_length=10,
                                                            min_length=10,
                                                            regex="^[0-9]{10}$",
                                                            required=True,
                                                        ),
                                                    ),
                                                    (
                                                        "workplace",
                                                        wagtail.blocks.CharBlock(
                                                            label="Рабочее место",
                                                            required=True,
                                                        ),
                                                    ),
                                                    (
                                                        "employee",
                                                        wagtail.blocks.CharBlock(
                                                            label="Работник",
                                                            required=False,
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ),
                                        (
                                            "city_phone",
                                            wagtail.blocks.StructBlock(
                                                [
                                                    (
                                                        "phone",
                                                        wagtail.blocks.RegexBlock(
                                                            error_messages={
                                                                "invalid": "Не верно введен номер"
                                                            },
                                                            help_text="Ввод без +74812 в формате 887766",
                                                            label="Городской номер телефона",
                                                            max_length=6,
                                                            min_length=6,
                                                            regex="^[0-9]{6}$",
                                                            required=True,
                                                        ),
                                                    ),
                                                    (
                                                        "workplace",
                                                        wagtail.blocks.CharBlock(
                                                            label="Рабочее место",
                                                            required=True,
                                                        ),
                                                    ),
                                                    (
                                                        "employee",
                                                        wagtail.blocks.CharBlock(
                                                            label="Работник",
                                                            required=False,
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ),
                                        (
                                            "internal_phone",
                                            wagtail.blocks.StructBlock(
                                                [
                                                    (
                                                        "phone",
                                                        wagtail.blocks.RegexBlock(
                                                            error_messages={
                                                                "invalid": "Не верно введен номер"
                                                            },
                                                            help_text="Ввод в формате 123",
                                                            label="Внутренний номер телефона",
                                                            max_length=3,
                                                            min_length=3,
                                                            regex="^[0-9]{3}$",
                                                            required=True,
                                                        ),
                                                    ),
                                                    (
                                                        "workplace",
                                                        wagtail.blocks.CharBlock(
                                                            label="Рабочее место",
                                                            required=True,
                                                        ),
                                                    ),
                                                    (
                                                        "employee",
                                                        wagtail.blocks.CharBlock(
                                                            label="Работник",
                                                            required=False,
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        verbose_name="Телефоны",
                    ),
                ),
            ],
            options={
                "verbose_name": "Страница шаблона документа",
                "verbose_name_plural": "Страницы шаблона документа",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.AlterModelOptions(
            name="phonespage",
            options={
                "verbose_name": "Страница с документами",
                "verbose_name_plural": "Страницы с документами",
            },
        ),
        migrations.RemoveField(
            model_name="phonespage",
            name="phones",
        ),
        migrations.AddField(
            model_name="phonespage",
            name="documents",
            field=wagtail.fields.StreamField(
                [
                    (
                        "phone_block",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "header",
                                    wagtail.blocks.CharBlock(
                                        label="Название документа", required=False
                                    ),
                                ),
                                (
                                    "document",
                                    wagtail.documents.blocks.DocumentChooserBlock(
                                        required=True
                                    ),
                                ),
                                (
                                    "document_example",
                                    wagtail.documents.blocks.DocumentChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "document_preview",
                                    wagtail.documents.blocks.DocumentChooserBlock(
                                        accept="pdf", required=False
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                verbose_name="Документы",
            ),
        ),
    ]
