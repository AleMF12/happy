# encoding: utf-8
# module pandas._libs.tslibs.offsets
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\pandas\_libs\tslibs\offsets.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import operator as operator # C:\Users\#Ale\.conda\envs\GCS10004\lib\operator.py
import re as re # C:\Users\#Ale\.conda\envs\GCS10004\lib\re.py
import time as time # <module 'time' (built-in)>
import warnings as warnings # C:\Users\#Ale\.conda\envs\GCS10004\lib\warnings.py
import numpy as np # C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\numpy\__init__.py
from pandas._libs.properties import cache_readonly

from pandas._libs.tslibs.timedeltas import Timedelta

from pandas._libs.tslibs.timestamps import Timestamp


from .Tick import Tick

class Nano(Tick):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _nanos_inc = 1
    _period_dtype_code = 12000
    _prefix = 'N'
    _reso = 10
    _td64_unit = 'ns'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E5CF268A50>'


