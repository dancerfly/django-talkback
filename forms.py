from django import forms

from zenaida.contrib.feedback.models import FeedbackItem

class FeedbackForm(forms.ModelForm):
    class Meta:
        fields = ('content', 'screenshot',)
        model = FeedbackItem
