# encoding: utf-8
# module pyarrow._flight
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\pyarrow\_flight.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import collections as collections # C:\Users\#Ale\.conda\envs\GCS10004\lib\collections\__init__.py
import contextlib as contextlib # C:\Users\#Ale\.conda\envs\GCS10004\lib\contextlib.py
import enum as enum # C:\Users\#Ale\.conda\envs\GCS10004\lib\enum.py
import re as re # C:\Users\#Ale\.conda\envs\GCS10004\lib\re.py
import socket as socket # C:\Users\#Ale\.conda\envs\GCS10004\lib\socket.py
import time as time # <module 'time' (built-in)>
import threading as threading # C:\Users\#Ale\.conda\envs\GCS10004\lib\threading.py
import warnings as warnings # C:\Users\#Ale\.conda\envs\GCS10004\lib\warnings.py
import weakref as weakref # C:\Users\#Ale\.conda\envs\GCS10004\lib\weakref.py
import pyarrow.lib as lib # C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
from pyarrow.lib import (ArrowCancelled, ArrowException, ArrowInvalid, 
    SignalStopHandler, _ReadPandasMixin, as_buffer, frombytes, tobytes)

import enum as __enum
import importlib._bootstrap as __importlib__bootstrap
import pyarrow.lib as __pyarrow_lib


from .ServerMiddleware import ServerMiddleware

class _ServerMiddlewareWrapper(ServerMiddleware):
    """ _ServerMiddlewareWrapper(dict middleware) """
    def call_completed(self, exception): # real signature unknown; restored from __doc__
        """ _ServerMiddlewareWrapper.call_completed(self, exception) """
        pass

    def sending_headers(self): # real signature unknown; restored from __doc__
        """ _ServerMiddlewareWrapper.sending_headers(self) """
        pass

    def __init__(self, dict_middleware): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _ServerMiddlewareWrapper.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _ServerMiddlewareWrapper.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002D412573A20>'


