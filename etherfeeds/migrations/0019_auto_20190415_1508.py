# Generated by Django 2.1.3 on 2019-04-15 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etherfeeds', '0018_auto_20190415_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerentries',
            name='question',
        ),
        migrations.AddField(
            model_name='answerentries',
            name='question_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hashlist',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 15, 8, 14, 585488), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='memberproposal',
            name='exp_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 25, 15, 8, 14, 586998), verbose_name='date expiring'),
        ),
        migrations.AlterField(
            model_name='memberproposal',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 15, 8, 14, 586951), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='exp_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 25, 15, 8, 14, 585785), verbose_name='date expiring'),
        ),
    ]
