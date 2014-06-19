from django import forms
from django.core import serializers

from zenaida.contrib.feedback.models import FeedbackItem

class FeedbackForm(forms.ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput)
    view = forms.CharField(widget=forms.HiddenInput)
    content = forms.CharField(label="Your Message", widget=forms.Textarea)
    request_path = forms.CharField(widget=forms.HiddenInput)
    request_method = forms.CharField(widget=forms.HiddenInput)
    request_encoding = forms.CharField(widget=forms.HiddenInput)
    request_meta = forms.CharField(widget=forms.HiddenInput)
    request_get = forms.CharField(widget=forms.HiddenInput)
    request_post = forms.CharField(widget=forms.HiddenInput)
    request_files = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, request=None, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.initial.update({
            'user': request.user if request.user.is_authenticated() else None,
            'view': request.resolver_match.view_name,
            'request_path': request.path,
            'request_method': request.method,
            'request_encoding': request.encoding,
            'request_meta': dict(request.META),
            'request_get': dict(request.GET),
            'request_post': dict(request.POST),
            'request_files': dict(request.FILES),
        })

    class Meta:
        fields = (
            'user',
            'content',
            'screenshot',
            'view',
            'request_path',
            'request_method',
            'request_encoding',
            'request_meta',
            'request_get',
            'request_post',
            'request_files',
        )
        model = FeedbackItem
