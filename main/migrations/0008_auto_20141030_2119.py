# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20141030_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='boat',
            field=models.ForeignKey(related_name='boat', default=None, blank=True, to='main.Boat', null=True),
            preserve_default=True,
        ),
    ]
