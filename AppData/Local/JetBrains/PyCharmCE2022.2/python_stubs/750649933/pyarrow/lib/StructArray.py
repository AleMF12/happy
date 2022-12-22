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


from .Array import Array

class StructArray(Array):
    """ Concrete class for Arrow arrays of a struct data type. """
    def field(self, index): # real signature unknown; restored from __doc__
        """
        StructArray.field(self, index)
        
                Retrieves the child array belonging to field.
        
                Parameters
                ----------
                index : Union[int, str]
                    Index / position or name of the field.
        
                Returns
                -------
                result : Array
        """
        pass

    def flatten(self, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        StructArray.flatten(self, MemoryPool memory_pool=None)
        
                Return one individual array for each field in the struct.
        
                Parameters
                ----------
                memory_pool : MemoryPool, default None
                    For memory allocations, if required, otherwise use default pool.
        
                Returns
                -------
                result : List[Array]
        """
        pass

    def from_arrays(self, arrays, names=None, fields=None, mask=None, memory_pool=None): # real signature unknown; restored from __doc__
        """
        StructArray.from_arrays(arrays, names=None, fields=None, mask=None, memory_pool=None)
        
                Construct StructArray from collection of arrays representing
                each field in the struct.
        
                Either field names or field instances must be passed.
        
                Parameters
                ----------
                arrays : sequence of Array
                names : List[str] (optional)
                    Field names for each struct child.
                fields : List[Field] (optional)
                    Field instances for each struct child.
                mask : pyarrow.Array[bool] (optional)
                    Indicate which values are null (True) or not null (False).
                memory_pool : MemoryPool (optional)
                    For memory allocations, if required, otherwise uses default pool.
        
                Returns
                -------
                result : StructArray
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002D88CE8E450>'


