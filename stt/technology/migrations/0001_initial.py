# Generated by Django 5.0.2 on 2024-03-18 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0091_remove_revision_submitted_for_moderation"),
    ]

    operations = [
        migrations.CreateModel(
            name="TechnologyPage",
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
            ],
            options={
                "verbose_name": "Стандартная страница технологий",
                "verbose_name_plural": "Стандартные страницы технологий",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="TechnologySectionPage",
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
            ],
            options={
                "verbose_name": "Раздел технологий",
                "verbose_name_plural": "Разделы технологий",
            },
            bases=("wagtailcore.page",),
        ),
    ]
