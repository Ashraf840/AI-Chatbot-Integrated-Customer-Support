# Generated by Django 4.2 on 2023-07-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_customersupportrequest_registered_user_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='csovisitormessage',
            options={'verbose_name_plural': 'HDO Visitor Messages'},
        ),
        migrations.AlterModelOptions(
            name='customersupportrequest',
            options={'verbose_name_plural': 'HDO Support Request'},
        ),
        migrations.AlterField(
            model_name='customersupportrequest',
            name='assigned_cso',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Assigned HDO'),
        ),
        migrations.AlterField(
            model_name='customersupportrequest',
            name='is_detached',
            field=models.BooleanField(default=False, help_text="Mark as detached if the HDO mark the 'CustomerSupportRequest' as resolved or dismissed", verbose_name='Detached'),
        ),
        migrations.AlterField(
            model_name='customersupportrequest',
            name='is_dismissed',
            field=models.BooleanField(default=False, help_text='Mark as dismissed if the HDO marked the coordinating convoInfo as dismissed', verbose_name='Dismissed'),
        ),
        migrations.AlterField(
            model_name='customersupportrequest',
            name='is_resolved',
            field=models.BooleanField(default=False, help_text='Mark as resolved if the HSO marked the coordinating convoInfo as resolved', verbose_name='Resolved'),
        ),
    ]
