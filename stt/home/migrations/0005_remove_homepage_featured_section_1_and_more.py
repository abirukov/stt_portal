# Generated by Django 5.0.2 on 2024-03-04 05:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_alter_homepage_body"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="homepage",
            name="featured_section_1",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="featured_section_1_title",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="promo_image",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="promo_text",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="promo_title",
        ),
    ]