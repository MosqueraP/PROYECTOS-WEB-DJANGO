# Generated by Django 5.0.1 on 2024-01-24 05:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="page",
            options={
                "ordering": ["order", "title"],
                "verbose_name": "pagina",
                "verbose_name_plural": "paginas",
            },
        ),
    ]
