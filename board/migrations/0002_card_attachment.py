# Generated by Django 5.1.7 on 2025-03-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="attachment",
            field=models.ImageField(blank=True, null=True, upload_to="cards/"),
        ),
    ]
