# Generated by Django 4.1.7 on 2023-03-20 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchatbotsocket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Chatbot Socket Record Created At'),
        ),
    ]
