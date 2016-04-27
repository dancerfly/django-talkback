from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^submit/$', 'talkback.views.feedback_ajax_submit'),  # noqa
)
