# Generated by Django 5.0.2 on 2024-03-18 11:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0003_eventsectionpage_menu_order_index"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eventsectionpage",
            name="menu_order_index",
        ),
    ]