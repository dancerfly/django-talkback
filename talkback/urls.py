from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^submit/$', 'talkback.views.feedback_ajax_submit'),
)
