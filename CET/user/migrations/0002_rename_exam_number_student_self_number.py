# Generated by Django 4.1 on 2023-05-22 13:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="exam_number",
            new_name="self_number",
        ),
    ]