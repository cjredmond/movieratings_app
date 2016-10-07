# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 20:23
from __future__ import unicode_literals
from django.db.models import F
from django.db import migrations

def add_average(apps, schema_editor):
    Movie = apps.get_model("movieratings", "Movie")
    #F = Movie.average_rating
    print(Movie)
    print("HERE")
    Movie.objects.filter(average_rating = 3.0).update(average_rating=4)

class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0004_auto_20161006_2022'),
    ]

    operations = [
        migrations.RunPython(add_average)
    ]