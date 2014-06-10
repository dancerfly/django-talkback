from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class FeedbackItem(models.Model):
    view = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    request = models.TextField()
    resolved = models.BooleanField(default=True)
    content = models.TextField()
    screenshot = models.FileField(blank=True, null=True, upload_to="feedback/screenshots")
