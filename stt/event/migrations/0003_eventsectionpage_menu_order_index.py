# Generated by Django 5.0.2 on 2024-03-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0002_eventsectionpage_alter_eventpage_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventsectionpage",
            name="menu_order_index",
            field=models.IntegerField(default=-1, verbose_name="Индекс сортировки"),
        ),
    ]