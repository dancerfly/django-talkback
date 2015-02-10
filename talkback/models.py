from django.conf import settings
from django.db import models


class FeedbackItem(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    resolved = models.BooleanField(default=False)
    content = models.TextField()
    screenshot = models.FileField(blank=True, null=True, upload_to="feedback/screenshots")

    # Request Data
    view = models.CharField(max_length=255)
    request_path = models.CharField(max_length=255)

    # The longest methods should be 7 chars, but we'll allow custom methods up
    # to 20 chars just in case.
    request_method = models.CharField(max_length=20, blank=True, null=True)

    # How long is the longest encoding name?
    request_encoding = models.CharField(max_length=20, blank=True, null=True)

    request_meta = models.TextField(blank=True, null=True)
    request_get = models.TextField(blank=True, null=True)
    request_post = models.TextField(blank=True, null=True)
    request_files = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "{username} at {path}".format(
            username=self.user.get_full_name(),
            path = self.request_path
        )

    class Meta:
        ordering = ["-timestamp"]
