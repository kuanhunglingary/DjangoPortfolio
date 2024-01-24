# Generated by Django 5.0.1 on 2024-01-24 03:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="link",
            field=models.URLField(
                blank=True,
                help_text="Link to RST. For example 'https://github.com/kuanhunglingary/DjangoPortfolio/blob/main/README.md'",
                null=True,
            ),
        ),
    ]
