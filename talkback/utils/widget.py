from django.template.loader import render_to_string
from django.template import RequestContext

from talkback import forms
from talkback.settings import CONFIG

def render_feedback_widget(request):
    return render_to_string('talkback/feedback_form.html', {
        'form': forms.FeedbackForm(request=request),
        'config': CONFIG,
    }, context_instance=RequestContext(request))
