# Generated by Django 4.0.2 on 2022-03-04 06:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='last_modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
