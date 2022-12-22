# encoding: utf-8
# module pyarrow.lib
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import datetime as datetime # C:\Users\#Ale\.conda\envs\GCS10004\lib\datetime.py
import decimal as _pydecimal # C:\Users\#Ale\.conda\envs\GCS10004\lib\decimal.py
import numpy as np # C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\numpy\__init__.py
import os as os # C:\Users\#Ale\.conda\envs\GCS10004\lib\os.py
import sys as sys # <module 'sys' (built-in)>
import pickle as builtin_pickle # C:\Users\#Ale\.conda\envs\GCS10004\lib\pickle.py
import pickle as pickle # C:\Users\#Ale\.conda\envs\GCS10004\lib\pickle.py
import signal as signal # C:\Users\#Ale\.conda\envs\GCS10004\lib\signal.py
import threading as threading # C:\Users\#Ale\.conda\envs\GCS10004\lib\threading.py
import warnings as warnings # C:\Users\#Ale\.conda\envs\GCS10004\lib\warnings.py
import atexit as atexit # <module 'atexit' (built-in)>
import re as re # C:\Users\#Ale\.conda\envs\GCS10004\lib\re.py
import collections as collections # C:\Users\#Ale\.conda\envs\GCS10004\lib\collections\__init__.py
import codecs as codecs # C:\Users\#Ale\.conda\envs\GCS10004\lib\codecs.py
import time as time # <module 'time' (built-in)>
from _queue import QueueEmpty

import collections.abc as __collections_abc
import enum as __enum
import importlib._bootstrap as __importlib__bootstrap
import io as __io
import _io as ___io


from ._Weakrefable import _Weakrefable

class Scalar(_Weakrefable):
    """
    Scalar()
    
        The base class for scalars.
    """
    def as_py(self): # real signature unknown; restored from __doc__
        """ Scalar.as_py(self) """
        pass

    def cast(self, target_type): # real signature unknown; restored from __doc__
        """
        Scalar.cast(self, target_type)
        
                Attempt a safe cast to target data type.
        
                Parameters
                ----------
                target_type : DataType or string coercible to DataType
                    The type to cast the scalar to.
        
                Returns
                -------
                scalar : A Scalar of the given target data type.
        """
        pass

    def equals(self, Scalar_other): # real signature unknown; restored from __doc__
        """ Scalar.equals(self, Scalar other) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ Scalar.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    is_valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Holds a valid (non-null) value.
        """

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Data type of the Scalar object.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002D88CEBF720>'


