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


from .SemiMonthOffset import SemiMonthOffset

class SemiMonthEnd(SemiMonthOffset):
    """
    Two DateOffset's per month repeating on the last day of the month & day_of_month.
    
        Parameters
        ----------
        n : int
        normalize : bool, default False
        day_of_month : int, {1, 3,...,27}, default 15
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.SemiMonthEnd()
        Timestamp('2022-01-15 00:00:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _min_day_of_month = 1
    _prefix = 'SM'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E5CF243D80>'


