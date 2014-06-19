from django.http import HttpResponseNotAllowed

def feedback_ajax_submit(request):
	if not request.POST:
		return HttpResponseNotAllowed(['POST'])
