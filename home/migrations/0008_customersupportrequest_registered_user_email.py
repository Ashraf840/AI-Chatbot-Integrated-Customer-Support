# Generated by Django 4.2.1 on 2023-07-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_csovisitorconvoinfo_is_dismissed_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customersupportrequest",
            name="registered_user_email",
            field=models.CharField(
                blank=True, max_length=60, null=True, verbose_name="User Email"
            ),
        ),
    ]
