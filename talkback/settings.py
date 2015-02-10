from django.conf import settings as settings

__all__ = ('CONFIG',)

CONFIG_DEFAULTS = {
    'INSERT_BEFORE': '</body>',
    'JQUERY_URL': None,
    'IGNORED_NAMESPACES': ['admin']
}

USER_CONFIG = getattr(settings, 'TALKBACK_CONFIG', {})

CONFIG = CONFIG_DEFAULTS.copy()
CONFIG.update(USER_CONFIG)
