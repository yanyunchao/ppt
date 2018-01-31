# -*- coding: utf-8 -*-

import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    base_string = basestring
else:
    base_string = str
