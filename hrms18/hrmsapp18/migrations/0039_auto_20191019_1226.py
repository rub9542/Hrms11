# Generated by Django 2.2.6 on 2019-10-19 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp18', '0038_auto_20191019_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 19, 12, 26, 54, 674453)),
        ),
    ]
