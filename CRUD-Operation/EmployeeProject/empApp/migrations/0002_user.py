# Generated by Django 4.2.7 on 2023-12-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("uname", models.CharField(max_length=32)),
                ("ucity", models.CharField(max_length=32)),
            ],
        ),
    ]
