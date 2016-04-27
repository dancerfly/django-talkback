import json

from django.http import (HttpResponse, HttpResponseNotAllowed,
                         HttpResponseBadRequest)
from django.contrib.sites.shortcuts import get_current_site

from talkback.forms import FeedbackForm
from talkback.utils.emails import send_notification_email


def feedback_ajax_submit(request):
    if not request.POST:
        return HttpResponseNotAllowed(['POST'])
    else:
        form = FeedbackForm(request, request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            send_notification_email(instance, get_current_site(request))
            return HttpResponse(json.dumps({'message': 'Thank you for your feedback!'}), content_type="application/json")
        else:
            return HttpResponseBadRequest(form.errors.as_json(), content_type="application/json")
