# Generated by Django 5.0.2 on 2024-03-19 09:14

import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "technology",
            "0005_technologypage_body_alter_technologysectionpage_body_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="technologypage",
            name="body",
            field=wagtail.fields.StreamField(
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
                    (
                        "embed_block",
                        wagtail.embeds.blocks.EmbedBlock(
                            help_text="Вставьте ссылку на контент, пример https://www.youtube.com/watch?v=SGJFWirQ3ks",
                            icon="media",
                            label="Встраиваемый контент",
                            template="blocks/embed_block.html",
                        ),
                    ),
                ],
                blank=True,
                null=True,
                verbose_name="Контент",
            ),
        ),
    ]
