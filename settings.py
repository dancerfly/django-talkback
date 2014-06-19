from django.conf import settings as settings

__all__ = ('CONFIG',)

CONFIG_DEFAULTS = {
    'INSERT_BEFORE': '</body>',
    'JQUERY_URL': None,
}

USER_CONFIG = getattr(settings, 'DEBUG_TOOLBAR_CONFIG', {})

CONFIG = CONFIG_DEFAULTS.copy()
CONFIG.update(USER_CONFIG)
