from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^submit/$', 'zenaida.contrib.feedback.views.feedback_ajax_submit'),
)
