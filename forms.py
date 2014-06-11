from django import forms
from django.core import serializers

from zenaida.contrib.feedback.models import FeedbackItem

class FeedbackForm(forms.ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput)
    request = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        fields = ('user', 'request', 'content', 'screenshot',)
        model = FeedbackItem
