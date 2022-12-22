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

class DataType(_Weakrefable):
    """
    DataType()
    
        Base class of all Arrow data types.
    
        Each data type is an *instance* of this class.
    """
    def equals(self, other): # real signature unknown; restored from __doc__
        """
        DataType.equals(self, other)
        
                Return true if type is equivalent to passed value.
        
                Parameters
                ----------
                other : DataType or string convertible to DataType
        
                Returns
                -------
                is_equal : bool
        """
        pass

    def field(self, i): # real signature unknown; restored from __doc__
        """ DataType.field(self, i) -> Field """
        return Field

    def to_pandas_dtype(self): # real signature unknown; restored from __doc__
        """
        DataType.to_pandas_dtype(self)
        
                Return the equivalent NumPy / Pandas dtype.
        """
        pass

    def _export_to_c(self, out_ptr): # real signature unknown; restored from __doc__
        """
        DataType._export_to_c(self, out_ptr)
        
                Export to a C ArrowSchema struct, given its pointer.
        
                Be careful: if you don't pass the ArrowSchema struct to a consumer,
                its memory will leak.  This is a low-level function intended for
                expert users.
        """
        pass

    def _import_from_c(self, in_ptr): # real signature unknown; restored from __doc__
        """
        DataType._import_from_c(in_ptr)
        
                Import DataType from a C ArrowSchema struct, given its pointer.
        
                This is a low-level function intended for expert users.
        """
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
        """ DataType.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    bit_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_buffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of data buffers required to construct Array type
        excluding children.
        """

    num_fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The number of child fields.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002D88CEC2660>'


