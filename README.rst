Django Talkback
===============

Django-Talkback is a pluggable Django app which adds a feedback form to
every page on your site.

Installation
------------

You can install the latest version of Django Talkback using ``pip``::

    $ pip install https://github.com/littleweaver/django-talkback/tarball/master

You can clone the repository yourself at https://github.com/littleweaver/django-talkback.

.. highlight:: python

Setup
-----

Ensure that ``'talkback'`` is in your project's ``INSTALLED_APPS``::

   INSTALLED_APPS = (
       'talkback',
       ...
   )

Add the following or similar anywhere in your URLconf::

   urlpatterns = patterns('',
       url(r'^talkback/', include('talkback.urls')),
       ...
   )

Add the following to your ``settings.py`` file::

   MIDDLEWARE_CLASSES += (
      'talkback.middleware.TalkbackMiddleware',
      ...
   )

Django Talkback relies on jQuery. If you do not already have jQuery in
your templates, add this to you ``settings.py`` file::

   TALKBACK_CONFIG = {
      'JQUERY_URL': '//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js',
   }
