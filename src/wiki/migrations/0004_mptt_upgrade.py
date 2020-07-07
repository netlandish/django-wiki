# Upgrades fields changed in django-mptt
# See: https://github.com/django-mptt/django-mptt/pull/578
# Generated by Django 2.2.7 on 2020-02-06 20:36
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("wiki", "0003_article_organization"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urlpath",
            name="level",
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="urlpath",
            name="lft",
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="urlpath",
            name="rght",
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
