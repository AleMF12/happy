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


from ._StructFieldOptions import _StructFieldOptions

class StructFieldOptions(_StructFieldOptions):
    """
    Options for the `struct_field` function.
    
        Parameters
        ----------
        indices : sequence of int
            List of indices for chained field lookup, for example `[4, 1]`
            will look up the second nested field in the fifth outer field.
    """
    def __init__(self, indices): # real signature unknown; restored from __doc__
        """ StructFieldOptions.__init__(self, indices) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for the `struct_field` function.\\n\\n    Parameters\\n    ----------\\n    indices : sequence of int\\n        List of indices for chained field lookup, for example `[4, 1]`\\n        will look up the second nested field in the fifth outer field.\\n    ', '__init__': <cyfunction StructFieldOptions.__init__ at 0x000002BD21D3B860>, '__dict__': <attribute '__dict__' of 'StructFieldOptions' objects>})"


