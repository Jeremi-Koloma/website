# Generated by Django 5.1.6 on 2025-02-27 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
