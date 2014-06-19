Zenaida Contrib Feedback
========================

Zenaida contrib feedback is a pluggable Django app which adds a feedback form to
every page on your site.

Installation
------------

You can install the latest version of Zenaida using ``pip``::

    $ pip install https://github.com/littleweaver/django-zenaida/tarball/master

You can clone the repository yourself at https://github.com/littleweaver/django-zenaida.

.. highlight:: python

Setup
-----

Ensure that ``'zenaida.contrib.feedback'`` is in your project's ``INSTALLED_APPS``::

   INSTALLED_APPS = (
       'zenaida.contrib.feedback',
       ...
   )

Add the following or similar anywhere in your URLconf::

   urlpatterns = patterns('',
       url(r'^feedback/', include('zenaida.contrib.feedback.urls')),
       ...
   )

Add the following to your ``settings.py`` file::

   MIDDLEWARE_CLASSES += (
      'zenaida.contrib.feedback.middleware.FeedbackMiddleware',
      ...
   )

Zenaida Contrib Feedback relies on jQuery. If you do not already have jQuery in
your templates, add this to you ``settings.py`` file::

   FEEDBACK_CONFIG = {
      'JQUERY_URL': '//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js',
   }
