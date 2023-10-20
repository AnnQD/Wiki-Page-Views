# Generated by Django 4.2.6 on 2023-10-20 03:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikipage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wikipage',
            old_name='count',
            new_name='views',
        ),
        migrations.AddField(
            model_name='wikipage',
            name='date',
            field=models.DateField(default=datetime.date(2023, 1, 1)),
        ),
        migrations.AlterField(
            model_name='wikipage',
            name='title',
            field=models.CharField(max_length=32),
        ),
    ]