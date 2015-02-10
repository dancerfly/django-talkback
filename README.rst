Django Feedback
===============

Django-Feedback is a pluggable Django app which adds a feedback form to
every page on your site.

Installation
------------

You can install the latest version of Django Feedback using ``pip``::

    $ pip install https://github.com/littleweaver/django-feedback/tarball/master

You can clone the repository yourself at https://github.com/littleweaver/django-feedack.

.. highlight:: python

Setup
-----

Ensure that ``'feedback'`` is in your project's ``INSTALLED_APPS``::

   INSTALLED_APPS = (
       'feedback',
       ...
   )

Add the following or similar anywhere in your URLconf::

   urlpatterns = patterns('',
       url(r'^feedback/', include('feedback.urls')),
       ...
   )

Add the following to your ``settings.py`` file::

   MIDDLEWARE_CLASSES += (
      'feedback.middleware.FeedbackMiddleware',
      ...
   )

Django Feedback relies on jQuery. If you do not already have jQuery in
your templates, add this to you ``settings.py`` file::

   FEEDBACK_CONFIG = {
      'JQUERY_URL': '//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js',
   }
