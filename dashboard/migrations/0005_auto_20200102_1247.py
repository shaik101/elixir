# Generated by Django 2.2.7 on 2020-01-02 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200101_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 1, 2, 12, 47, 4, 35100)),
        ),
        migrations.AlterField(
            model_name='guest',
            name='comments',
            field=models.CharField(blank=True, default='NA', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 1, 2, 12, 47, 4, 32611)),
        ),
    ]