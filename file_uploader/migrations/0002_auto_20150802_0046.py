# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_uploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='post',
            field=models.ForeignKey(null=True, to='news.Post', blank=True),
        ),
    ]
