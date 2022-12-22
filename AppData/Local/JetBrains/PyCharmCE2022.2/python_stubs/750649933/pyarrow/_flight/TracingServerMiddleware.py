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

class TracingServerMiddleware(ServerMiddleware):
    # no doc
    def __init__(self, trace_context): # real signature unknown; restored from __doc__
        """ TracingServerMiddleware.__init__(self, trace_context) """
        pass

    trace_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = [
        'trace_context',
    ]


