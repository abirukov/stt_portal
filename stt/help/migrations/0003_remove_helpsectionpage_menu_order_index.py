# Generated by Django 5.0.2 on 2024-03-18 11:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("help", "0002_helpsectionpage_menu_order_index"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="helpsectionpage",
            name="menu_order_index",
        ),
    ]
