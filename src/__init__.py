import os
import sys

__version__ = '0.0.1'
__license__ = 'MIT'

EZEOSDIR = os.path.dirname(__file__)
USAGE = '%prog [options] [path]'
VERSION = 'EZEOS version %s\n\nPython %s' % (__version__, sys.version)

from src.util.util import run