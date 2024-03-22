# Generated by Django 5.0.2 on 2024-03-22 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0011_eventsectionpage_elements_per_page"),
        ("wagtailcore", "0091_remove_revision_submitted_for_moderation"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventpage",
            name="gallery",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
            ),
        ),
    ]
