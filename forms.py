from django import forms
from django.contrib.auth import get_user_model
from django.core import serializers

from zenaida.contrib.feedback.models import FeedbackItem

class FeedbackForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all(), widget=forms.HiddenInput, required=True)
    view = forms.CharField(widget=forms.HiddenInput, required=True)
    content = forms.CharField(label="Your Message", widget=forms.Textarea, required=True)
    request_path = forms.CharField(widget=forms.HiddenInput, required=True)
    request_method = forms.CharField(widget=forms.HiddenInput, required=True)
    request_encoding = forms.CharField(widget=forms.HiddenInput, required=False)
    request_meta = forms.CharField(widget=forms.HiddenInput, required=False)
    request_get = forms.CharField(widget=forms.HiddenInput, required=False)
    request_post = forms.CharField(widget=forms.HiddenInput, required=False)
    request_files = forms.CharField(widget=forms.HiddenInput, required=False)

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

    # TODO: Implement tampering validation on the user, view, and request_* fields

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
