# Generated by Django 4.2 on 2024-04-18 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tadaApp", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="DistanceMatrix",
        ),
        migrations.DeleteModel(
            name="TaDaRateSheet",
        ),
    ]