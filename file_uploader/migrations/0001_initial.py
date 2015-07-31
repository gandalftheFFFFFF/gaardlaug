# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import file_uploader.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150731_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200, choices=[('regnskab', 'Regnskab'), ('referat', 'Referat'), ('andet', 'Andet')])),
                ('date', models.DateField()),
                ('doc', models.FileField(upload_to=file_uploader.models.get_upload_path)),
                ('post', models.ForeignKey(to='news.Post', blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
