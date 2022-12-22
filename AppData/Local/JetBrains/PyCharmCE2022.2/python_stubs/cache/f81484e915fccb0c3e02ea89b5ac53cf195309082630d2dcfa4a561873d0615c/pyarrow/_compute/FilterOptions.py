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


from ._FilterOptions import _FilterOptions

class FilterOptions(_FilterOptions):
    """
    Options for selecting with a boolean filter.
    
        Parameters
        ----------
        null_selection_behavior : str, default "drop"
            How to handle nulls in the selection filter.
            Accepted values are "drop", "emit_null".
    """
    def __init__(self, null_selection_behavior=None): # real signature unknown; restored from __doc__
        """ FilterOptions.__init__(self, null_selection_behavior=u'drop') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for selecting with a boolean filter.\\n\\n    Parameters\\n    ----------\\n    null_selection_behavior : str, default "drop"\\n        How to handle nulls in the selection filter.\\n        Accepted values are "drop", "emit_null".\\n    \', \'__init__\': <cyfunction FilterOptions.__init__ at 0x000002BD21D3B520>, \'__dict__\': <attribute \'__dict__\' of \'FilterOptions\' objects>})'


