from .base import *

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEBUG = True

try:
    from .local import *
except ImportError:
    pass
