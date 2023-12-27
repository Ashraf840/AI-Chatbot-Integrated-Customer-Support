# Generated by Django 4.1.7 on 2023-03-22 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_csovisitorconvoinfo_is_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='csovisitorconvoinfo',
            name='is_cleared',
            field=models.BooleanField(default=False, help_text='The CSO removed/cleared the associate msg-req from the CSR List, thus the conversation will be marked as cleared', verbose_name='Associate msg-req is removed'),
        ),
        migrations.AlterField(
            model_name='csovisitorconvoinfo',
            name='is_cancelled',
            field=models.BooleanField(default=False, help_text='The user cancelled the chat-conversation, thus the associate msg-req will be removed form the CSR list', verbose_name='Chat cancelled'),
        ),
    ]
