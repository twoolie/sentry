"""
sentry.filters
~~~~~~~~~~~~~~

:copyright: (c) 2010 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from .base import *
from .builtins import *
from .widgets import *

# Backwards compatibility
SentryFilter = Filter
