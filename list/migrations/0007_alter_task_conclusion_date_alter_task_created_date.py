# Generated by Django 4.2.11 on 2025-03-19 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0006_alter_task_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='conclusion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Criado em'),
        ),
    ]
