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


from .FragmentScanOptions import FragmentScanOptions

class CsvFragmentScanOptions(FragmentScanOptions):
    """
    CsvFragmentScanOptions(ConvertOptions convert_options=None, ReadOptions read_options=None)
    
        Scan-specific options for CSV fragments.
    
        Parameters
        ----------
        convert_options : pyarrow.csv.ConvertOptions
            Options regarding value conversion.
        read_options : pyarrow.csv.ReadOptions
            General read options.
    """
    def equals(self, CsvFragmentScanOptions_other): # real signature unknown; restored from __doc__
        """ CsvFragmentScanOptions.equals(self, CsvFragmentScanOptions other) """
        pass

    def __init__(self, ConvertOptions_convert_options=None, ReadOptions_read_options=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ CsvFragmentScanOptions.__reduce__(self) """
        pass

    convert_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001F348705330>'
    __slots__ = ()


