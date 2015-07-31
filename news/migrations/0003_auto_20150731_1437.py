# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150731_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(blank=True, to='news.Post', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
