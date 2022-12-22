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


from .WeekOfMonthMixin import WeekOfMonthMixin

class WeekOfMonth(WeekOfMonthMixin):
    """
    Describes monthly dates like "the Tuesday of the 2nd week of each month".
    
        Parameters
        ----------
        n : int
        week : int {0, 1, 2, 3, ...}, default 0
            A specific integer for the week of the month.
            e.g. 0 is 1st week of month, 1 is the 2nd week, etc.
        weekday : int {0, 1, ..., 6}, default 0
            A specific integer for the day of the week.
    
            - 0 is Monday
            - 1 is Tuesday
            - 2 is Wednesday
            - 3 is Thursday
            - 4 is Friday
            - 5 is Saturday
            - 6 is Sunday.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.WeekOfMonth()
        Timestamp('2022-01-03 00:00:00')
    """
    @classmethod
    def _from_name(cls, *args, **kwargs): # real signature unknown
        pass

    def _get_offset_day(self, *args, **kwargs): # real signature unknown
        """
        Find the day in the same month as other that has the same
                weekday as self.weekday and is the self.week'th such day in the month.
        
                Parameters
                ----------
                other : datetime
        
                Returns
                -------
                day : int
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _attributes = (
        'n',
        'normalize',
        'week',
        'weekday',
    )
    _prefix = 'WOM'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E5CF243C60>'


