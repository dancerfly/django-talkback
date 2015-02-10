# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20140619_0349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedbackitem',
            options={'ordering': [b'-timestamp']},
        ),
    ]
