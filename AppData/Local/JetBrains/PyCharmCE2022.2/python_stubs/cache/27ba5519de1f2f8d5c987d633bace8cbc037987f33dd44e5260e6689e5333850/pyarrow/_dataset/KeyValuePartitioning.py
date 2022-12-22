# encoding: utf-8
# module pyarrow._dataset
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\pyarrow\_dataset.cp39-win_amd64.pyd
# by generator 1.147
""" Dataset is currently unstable. APIs subject to change without notice. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import codecs as codecs # C:\Users\#Ale\.conda\envs\GCS10004\lib\codecs.py
import collections as collections # C:\Users\#Ale\.conda\envs\GCS10004\lib\collections\__init__.py
import os as os # C:\Users\#Ale\.conda\envs\GCS10004\lib\os.py
import warnings as warnings # C:\Users\#Ale\.conda\envs\GCS10004\lib\warnings.py
import pyarrow as pa # C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\pyarrow\__init__.py
from pyarrow.lib import ArrowTypeError, _pc, frombytes, tobytes

import importlib._bootstrap as __importlib__bootstrap
import pyarrow.lib as __pyarrow_lib


from .Partitioning import Partitioning

class KeyValuePartitioning(Partitioning):
    """ KeyValuePartitioning() """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ KeyValuePartitioning.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ KeyValuePartitioning.__setstate_cython__(self, __pyx_state) """
        pass

    dictionaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The unique values for each partition field, if available.

        Those values are only available if the Partitioning object was
        created through dataset discovery from a PartitioningFactory, or
        if the dictionaries were manually specified in the constructor.
        If no dictionary field is available, this returns an empty list.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001F3487053F0>'


