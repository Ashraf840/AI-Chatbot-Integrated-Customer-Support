# Generated by Django 4.2.1 on 2023-07-13 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authenticationApp", "0009_alter_user_signin_token_tms_user_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_signin_token_tms",
            name="token_type",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Token Type"
            ),
        ),
    ]
