import json

from django.http import (HttpResponse, HttpResponseNotAllowed,
                         HttpResponseBadRequest)

from talkback.forms import FeedbackForm

def feedback_ajax_submit(request):
    if not request.POST:
        return HttpResponseNotAllowed(['POST'])
    else:
        form = FeedbackForm(request, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'message': 'Thank you for your feedback!'}), content_type="application/json")
        else:
            return HttpResponseBadRequest(form.errors.as_json(), content_type="application/json")
