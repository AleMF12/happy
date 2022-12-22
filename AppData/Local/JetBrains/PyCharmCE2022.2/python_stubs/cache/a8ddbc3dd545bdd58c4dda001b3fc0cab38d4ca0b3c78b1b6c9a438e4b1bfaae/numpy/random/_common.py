# encoding: utf-8
# module numpy.random._common
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\numpy\random\_common.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import numpy as np # C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\numpy\__init__.py

# functions

def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None): # reliably restored by inspect
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    pass

# classes

class interface(tuple):
    """ interface(state_address, state, next_uint64, next_uint32, next_double, bit_generator) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new interface object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new interface object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, state_address, state, next_uint64, next_uint32, next_double, bit_generator): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, state_address, state, next_uint64, next_uint32, next_double, bit_generator): # reliably restored by inspect
        """ Create new instance of interface(state_address, state, next_uint64, next_uint32, next_double, bit_generator) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    bit_generator = _tuplegetter(5, 'Alias for field number 5')
    next_double = _tuplegetter(4, 'Alias for field number 4')
    next_uint32 = _tuplegetter(3, 'Alias for field number 3')
    next_uint64 = _tuplegetter(2, 'Alias for field number 2')
    state = _tuplegetter(1, 'Alias for field number 1')
    state_address = _tuplegetter(0, 'Alias for field number 0')
    _fields = (
        'state_address',
        'state',
        'next_uint64',
        'next_uint32',
        'next_double',
        'bit_generator',
    )
    _field_defaults = {}
    __slots__ = ()


# variables with complex values

__all__ = [
    'interface',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000013F2F33D4C0>'

__pyx_capi__ = {
    'LEGACY_POISSON_LAM_MAX': None, # (!) real value is '<capsule object "double" at 0x0000013F2F33D5D0>'
    'MAXSIZE': None, # (!) real value is '<capsule object "uint64_t" at 0x0000013F2F33D600>'
    'POISSON_LAM_MAX': None, # (!) real value is '<capsule object "double" at 0x0000013F2F33D5A0>'
    'benchmark': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *, PyObject *, Py_ssize_t, PyObject *)" at 0x0000013F2F33D630>'
    'check_array_constraint': None, # (!) real value is '<capsule object "int (PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x0000013F2F33D720>'
    'check_constraint': None, # (!) real value is '<capsule object "int (double, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x0000013F2F33D6F0>'
    'cont': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, int, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *)" at 0x0000013F2F33D8A0>'
    'cont_broadcast_3': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x0000013F2F33D930>'
    'cont_f': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *)" at 0x0000013F2F33D900>'
    'disc': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, int, int, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x0000013F2F33D8D0>'
    'discrete_broadcast_iii': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x0000013F2F33D960>'
    'double_fill': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x0000013F2F33D780>'
    'float_fill': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x0000013F2F33D7B0>'
    'float_fill_from_double': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x0000013F2F33D7E0>'
    'int_to_array': None, # (!) real value is '<capsule object "PyArrayObject *(PyObject *, PyObject *, PyObject *, PyObject *)" at 0x0000013F2F33D840>'
    'kahan_sum': None, # (!) real value is '<capsule object "double (double *, npy_intp)" at 0x0000013F2F33D750>'
    'prepare_cffi': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *)" at 0x0000013F2F33D690>'
    'prepare_ctypes': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *)" at 0x0000013F2F33D6C0>'
    'random_raw': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x0000013F2F33D660>'
    'validate_output_shape': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyArrayObject *)" at 0x0000013F2F33D870>'
    'wrap_int': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x0000013F2F33D810>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='numpy.random._common', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000013F2F33D4C0>, origin='C:\\\\Users\\\\#Ale\\\\.conda\\\\envs\\\\GCS10004\\\\lib\\\\site-packages\\\\numpy\\\\random\\\\_common.cp39-win_amd64.pyd')"

__test__ = {}

