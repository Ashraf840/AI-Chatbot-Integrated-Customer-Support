# Generated by Django 4.1 on 2023-01-21 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customersupportrequest",
            name="visitor_session_uuid",
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
