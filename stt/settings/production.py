from .base import *

try:
    from .local import *
except ImportError:
    pass

DEBUG = False
CSRF_COOKIE_SECURE = True
