# Generated by Django 3.1.6 on 2021-03-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Students",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("e_no", models.IntegerField()),
                ("name", models.CharField(max_length=30)),
                ("city", models.CharField(max_length=20)),
                ("branch", models.CharField(max_length=15)),
            ],
        )
    ]
