# Generated by Django 2.2 on 2019-12-17 13:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_guest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 12, 17, 18, 54, 28, 81864)),
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('time_in', models.TimeField(blank=True, null=True)),
                ('time_out', models.TimeField(blank=True, null=True)),
                ('remarks', models.CharField(default='present', max_length=250)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Addstaff')),
            ],
        ),
    ]