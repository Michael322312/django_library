# Generated by Django 5.0.2 on 2024-02-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="librarybook",
            name="isbn",
            field=models.CharField(max_length=63, unique=True),
        ),
        migrations.AlterModelTable(
            name="librarybook",
            table="library_books",
        ),
    ]
