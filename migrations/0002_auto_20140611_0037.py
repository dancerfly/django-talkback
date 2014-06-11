# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackitem',
            name='request_post',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedbackitem',
            name='request_encoding',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedbackitem',
            name='request_method',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedbackitem',
            name='request_path',
            field=models.CharField(default='NOT AVAILABLE', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedbackitem',
            name='request_get',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedbackitem',
            name='request_files',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedbackitem',
            name='request_meta',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='feedbackitem',
            name='request',
        ),
    ]
