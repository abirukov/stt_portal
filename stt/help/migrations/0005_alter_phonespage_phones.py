# Generated by Django 5.0.2 on 2024-03-19 09:14

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("help", "0004_phonespage_helppage_body_helpsectionpage_body_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phonespage",
            name="phones",
            field=wagtail.fields.StreamField(
                [
                    (
                        "header",
                        wagtail.blocks.RichTextBlock(
                            features=["h2", "h3", "h4", "h5", "h6"], label="Заголовок"
                        ),
                    ),
                    (
                        "phone_block",
                        wagtail.blocks.StreamBlock(
                            [
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
                                                    form_classname="Мобильный номер телефона",
                                                    help_text="Ввод без +7 в формате 9008887766",
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
                                                    form_classname="Городской номер телефона",
                                                    help_text="Ввод без +74812 в формате 887766",
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
                                                    form_classname="Внутренний номер телефона",
                                                    help_text="Ввод в формате 123",
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
                    ),
                ],
                blank=True,
                null=True,
                verbose_name="Телефоны",
            ),
        ),
    ]