# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20140611_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackitem',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
