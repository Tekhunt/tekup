# Generated by Django 4.2 on 2023-04-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="SkillCovered",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
    ]
