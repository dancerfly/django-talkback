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
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('resolved', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('screenshot', models.FileField(null=True, upload_to=b'feedback/screenshots', blank=True)),
                ('view', models.CharField(max_length=255)),
                ('request_path', models.CharField(max_length=255)),
                ('request_method', models.CharField(max_length=20, null=True, blank=True)),
                ('request_encoding', models.CharField(max_length=20, null=True, blank=True)),
                ('request_meta', models.TextField(null=True, blank=True)),
                ('request_get', models.TextField(null=True, blank=True)),
                ('request_post', models.TextField(null=True, blank=True)),
                ('request_files', models.TextField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
            bases=(models.Model,),
        ),
    ]
