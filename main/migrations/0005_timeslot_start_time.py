# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_timeslot_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 28, 22, 1, 0, 419022, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
