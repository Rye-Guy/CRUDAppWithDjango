# Generated by Django 2.1.3 on 2018-11-23 19:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181114_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 19, 15, 19, 609062, tzinfo=utc), verbose_name='date published'),
        ),
    ]
