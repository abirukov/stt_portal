# Generated by Django 5.0.2 on 2024-03-25 08:44

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("help", "0014_alter_documentsamplepage_documents_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="documentsamplepage",
            name="documents",
            field=wagtail.fields.StreamField(
                [
                    (
                        "documents_block",
                        wagtail.blocks.StructBlock(
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
                                        label="Оригинал документа", required=True
                                    ),
                                ),
                                (
                                    "document_pdf",
                                    wagtail.documents.blocks.DocumentChooserBlock(
                                        label="Оригинал документа в pdf для превью"
                                    ),
                                ),
                                (
                                    "document_example",
                                    wagtail.documents.blocks.DocumentChooserBlock(
                                        label="Пример заполнения документа",
                                        required=False,
                                    ),
                                ),
                                (
                                    "document_example_pdf",
                                    wagtail.documents.blocks.DocumentChooserBlock(
                                        label="Пример заполнения документа в pdf для превью"
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
        migrations.AlterField(
            model_name="phonespage",
            name="phones",
            field=wagtail.fields.StreamField(
                [
                    (
                        "phones_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "header",
                                    wagtail.blocks.CharBlock(
                                        label="Название группы", required=True
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
                                                    label="Рабочее место", required=True
                                                ),
                                            ),
                                            (
                                                "employee",
                                                wagtail.blocks.CharBlock(
                                                    label="Работник", required=False
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
                                                    label="Рабочее место", required=True
                                                ),
                                            ),
                                            (
                                                "employee",
                                                wagtail.blocks.CharBlock(
                                                    label="Работник", required=False
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
                                                    label="Рабочее место", required=True
                                                ),
                                            ),
                                            (
                                                "employee",
                                                wagtail.blocks.CharBlock(
                                                    label="Работник", required=False
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
    ]
