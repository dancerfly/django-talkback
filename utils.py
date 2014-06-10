from django.template.loader import render_to_string

from zenaida.contrib.feedback import forms

def render_feedback_widget(request):
	return render_to_string('feedback/feedback_form.html', {
		'form': forms.FeedbackForm
	})
