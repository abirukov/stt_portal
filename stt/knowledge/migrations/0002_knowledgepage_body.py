# Generated by Django 5.0.2 on 2024-03-03 16:15

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("knowledge", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="knowledgepage",
            name="body",
            field=wagtail.fields.StreamField(
                [("text", wagtail.blocks.RichTextBlock())], blank=True, null=True
            ),
        ),
    ]