# Generated by Django 5.0.2 on 2024-03-28 10:40

import stt.base.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmedia.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0011_alter_newspage_body_alter_newssectionpage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newspage",
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
                                "superscript",
                                "subscript",
                                "strikethrough",
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
                            ],
                            label="Блок изображения",
                        ),
                    ),
                    ("audio", wagtailmedia.blocks.AudioChooserBlock(label="Аудио")),
                    ("video", stt.base.blocks.SttVideoChooserBlock(label="Видео")),
                ],
                blank=True,
                null=True,
                verbose_name="Контент",
            ),
        ),
    ]
