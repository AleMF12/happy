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


from .MonthOffset import MonthOffset

class BusinessMonthEnd(MonthOffset):
    """
    DateOffset increments between the last business day of the month.
    
        Examples
        --------
        >>> from pandas.tseries.offsets import BMonthEnd
        >>> ts = pd.Timestamp('2020-05-24 05:01:15')
        >>> ts + BMonthEnd()
        Timestamp('2020-05-29 05:01:15')
        >>> ts + BMonthEnd(2)
        Timestamp('2020-06-30 05:01:15')
        >>> ts + BMonthEnd(-2)
        Timestamp('2020-03-31 05:01:15')
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'business_end'
    _prefix = 'BM'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E5CF243EA0>'


