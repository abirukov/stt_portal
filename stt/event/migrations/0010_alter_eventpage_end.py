# Generated by Django 5.0.2 on 2024-03-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0009_alter_eventpage_start"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventpage",
            name="end",
            field=models.DateTimeField(
                blank=True,
                help_text="Выберите дату и время окончания события (необязательно)",
                null=True,
                verbose_name="Окончание события",
            ),
        ),
    ]
