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


from .NativeFile import NativeFile

class BufferedInputStream(NativeFile):
    """
    BufferedInputStream(NativeFile stream, int buffer_size, MemoryPool memory_pool=None)
    
        An input stream that performs buffered reads from
        an unbuffered input stream, which can mitigate the overhead
        of many small reads in some cases.
    
        Parameters
        ----------
        stream : NativeFile
            The input stream to wrap with the buffer
        buffer_size : int
            Size of the temporary read buffer.
        memory_pool : MemoryPool
            The memory pool used to allocate the buffer.
    """
    def detach(self): # real signature unknown; restored from __doc__
        """
        BufferedInputStream.detach(self)
        
                Release the raw InputStream.
                Further operations on this stream are invalid.
        
                Returns
                -------
                raw : NativeFile
                    The underlying raw input stream
        """
        pass

    def __init__(self, NativeFile_stream, int_buffer_size, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ BufferedInputStream.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ BufferedInputStream.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002D88CE8E7B0>'


