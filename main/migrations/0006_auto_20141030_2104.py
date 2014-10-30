# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_timeslot_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='start_time',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
