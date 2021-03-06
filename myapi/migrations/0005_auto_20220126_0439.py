# Generated by Django 3.2.11 on 2022-01-26 04:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_auto_20220126_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
    ]
