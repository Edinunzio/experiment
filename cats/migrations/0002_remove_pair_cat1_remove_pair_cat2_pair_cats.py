# Generated by Django 4.2.9 on 2024-01-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cats", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pair",
            name="cat1",
        ),
        migrations.RemoveField(
            model_name="pair",
            name="cat2",
        ),
        migrations.AddField(
            model_name="pair",
            name="cats",
            field=models.ManyToManyField(to="cats.cat"),
        ),
    ]
