# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_of_boat', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
