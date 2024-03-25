# Generated by Django 5.0.2 on 2024-03-25 08:50

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("help", "0015_alter_documentsamplepage_documents_and_more"),
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
                                        label="PDF превью (если пусто генерируется автоматически)",
                                        required=False,
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
                                        label="PDF превью примера (если пусто генерируется автоматически)",
                                        required=False,
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
