# encoding: utf-8
# module zmq.backend.cython._poll
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\zmq\backend\cython\_poll.cp39-win_amd64.pyd
# by generator 1.147
""" 0MQ polling related functions and classes. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import warnings as warnings # C:\Users\#Ale\.conda\envs\GCS10004\lib\warnings.py
from time import monotonic

import zmq.error as __zmq_error


# functions

def zmq_poll(sockets, timeout=-1): # real signature unknown; restored from __doc__
    """
    zmq_poll(sockets, timeout=-1)
    
        Poll a set of 0MQ sockets, native file descs. or sockets.
    
        Parameters
        ----------
        sockets : list of tuples of (socket, flags)
            Each element of this list is a two-tuple containing a socket
            and a flags. The socket may be a 0MQ socket or any object with
            a ``fileno()`` method. The flags can be zmq.POLLIN (for detecting
            for incoming messages), zmq.POLLOUT (for detecting that send is OK)
            or zmq.POLLIN|zmq.POLLOUT for detecting both.
        timeout : int
            The number of milliseconds to poll for. Negative means no timeout.
    """
    pass

# classes

class InterruptedSystemCall(__zmq_error.ZMQError, InterruptedError):
    """
    Wrapper for EINTR
    
        This exception should be caught internally in pyzmq
        to retry system calls, and not propagate to the user.
    
        .. versionadded:: 14.7
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    errno = 4


# variables with complex values

__all__ = [
    'zmq_poll',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020BC8769520>'

__spec__ = None # (!) real value is "ModuleSpec(name='zmq.backend.cython._poll', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020BC8769520>, origin='C:\\\\Users\\\\#Ale\\\\.conda\\\\envs\\\\GCS10004\\\\lib\\\\site-packages\\\\zmq\\\\backend\\\\cython\\\\_poll.cp39-win_amd64.pyd')"

__test__ = {}

