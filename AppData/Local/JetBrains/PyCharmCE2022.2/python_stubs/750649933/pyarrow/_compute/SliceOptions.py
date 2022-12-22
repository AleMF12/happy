# encoding: utf-8
# module pyarrow._compute
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\pyarrow\_compute.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import pyarrow.lib as lib # C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
import inspect as inspect # C:\Users\#Ale\.conda\envs\GCS10004\lib\inspect.py
import numpy as np # C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\numpy\__init__.py
from pyarrow.lib import ArrowInvalid, frombytes, tobytes

import pyarrow.lib as __pyarrow_lib


from ._SliceOptions import _SliceOptions

class SliceOptions(_SliceOptions):
    """
    Options for slicing.
    
        Parameters
        ----------
        start : int
            Index to start slicing at (inclusive).
        stop : int or None, default None
            If given, index to stop slicing at (exclusive).
            If not given, slicing will stop at the end.
        step : int, default 1
            Slice step.
    """
    def __init__(self, start, stop=None, step=1): # real signature unknown; restored from __doc__
        """ SliceOptions.__init__(self, start, stop=None, step=1) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for slicing.\\n\\n    Parameters\\n    ----------\\n    start : int\\n        Index to start slicing at (inclusive).\\n    stop : int or None, default None\\n        If given, index to stop slicing at (exclusive).\\n        If not given, slicing will stop at the end.\\n    step : int, default 1\\n        Slice step.\\n    ', '__init__': <cyfunction SliceOptions.__init__ at 0x000002BD21D3B380>, '__dict__': <attribute '__dict__' of 'SliceOptions' objects>})"


