# Generated by Django 2.2 on 2019-12-26 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addduration',
            name='duration',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 12, 27, 1, 9, 27, 248947)),
        ),
        migrations.AlterField(
            model_name='guest',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 12, 27, 1, 9, 27, 246949)),
        ),
    ]
