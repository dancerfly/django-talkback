from setuptools import setup, find_packages

__version__ = __import__('talkback').__version__


description = "A pluggable app for adding an AJAX feedback form to Django-powered websites."


setup(
    name="django-talkback",
    version='.'.join([str(v) for v in __version__]),
    url="http://github.com/littleweaver/django-talkback",
    description=description,
    long_description=description,
    author='Little Weaver Web Collective, LLC',
    author_email='hello@littleweaverweb.com',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    platforms=['OS Independent'],
    install_requires=[
        'django>=1.7',
    ]
)
