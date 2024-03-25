# Generated by Django 5.0.2 on 2024-03-25 08:32

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations

import stt.base.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0008_alter_homepage_hero_slider"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="hero_slider",
            field=wagtail.fields.StreamField(
                [
                    (
                        "slide",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Изображение", required=True
                                    ),
                                ),
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(
                                        label="Заголовок", required=True
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        label="Текст", required=False
                                    ),
                                ),
                                (
                                    "page_more",
                                    wagtail.blocks.PageChooserBlock(
                                        label="Страница подробнее", required=False
                                    ),
                                ),
                                (
                                    "video",
                                    stt.base.blocks.SttVideoChooserBlock(
                                        label="Видео", required=False
                                    ),
                                ),
                            ],
                            label="Слайд",
                        ),
                    )
                ],
                blank=True,
                null=True,
                verbose_name="Слайдер",
            ),
        ),
    ]
