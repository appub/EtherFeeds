# Generated by Django 2.1.3 on 2019-04-12 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etherfeeds', '0006_auto_20190412_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='exp_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 22, 13, 24, 26, 84266), verbose_name='date expiring'),
        ),
    ]
