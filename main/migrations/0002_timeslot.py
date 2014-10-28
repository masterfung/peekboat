# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('duration', models.IntegerField(max_length=3)),
                ('availability', models.IntegerField(default=0)),
                ('boat', models.ForeignKey(related_name='boat', default=None, to='main.Boat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
