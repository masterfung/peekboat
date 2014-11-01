# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20141030_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boat',
            old_name='name_of_boat',
            new_name='name',
        ),
    ]
