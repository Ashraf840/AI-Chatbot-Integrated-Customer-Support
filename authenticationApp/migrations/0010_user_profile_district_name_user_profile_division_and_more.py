# Generated by Django 4.2 on 2023-07-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationApp', '0009_alter_user_signin_token_tms_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='district_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='District Name'),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='division',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Division '),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='user_organization_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Organization Name'),
        ),
    ]