# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('view', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('request', models.TextField()),
                ('resolved', models.BooleanField(default=True)),
                ('content', models.TextField()),
                ('screenshot', models.FileField(null=True, upload_to=b'feedback/screenshots', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
