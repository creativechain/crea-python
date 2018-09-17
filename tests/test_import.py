# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from crea import *  # noqa
from creabase import *  # noqa


# pylint: disable=unused-import,unused-variable
def test_import():
    _ = Crea()
    _ = account.PasswordKey
