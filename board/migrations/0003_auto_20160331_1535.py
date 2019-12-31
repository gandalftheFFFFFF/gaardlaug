# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20150801_2153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boardmember',
            options={'ordering': ['first_name', 'last_name']},
        ),
    ]
