# Generated by Django 4.2 on 2023-10-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_chatsupportuseronline_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersupportrequest',
            name='chatbot_socket_id',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
