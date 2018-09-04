# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from dpay import *  # noqa
from dpaybase import *  # noqa


# pylint: disable=unused-import,unused-variable
def test_import():
    _ = DPay()
    _ = account.PasswordKey
