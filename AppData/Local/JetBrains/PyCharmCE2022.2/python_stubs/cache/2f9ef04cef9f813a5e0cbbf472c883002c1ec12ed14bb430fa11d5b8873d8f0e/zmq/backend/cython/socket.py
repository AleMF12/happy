# encoding: utf-8
# module zmq.backend.cython.socket
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\zmq\backend\cython\socket.cp39-win_amd64.pyd
# by generator 1.147
""" 0MQ Socket class. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import codecs as codecs # C:\Users\#Ale\.conda\envs\GCS10004\lib\codecs.py
import copy as copy_mod # C:\Users\#Ale\.conda\envs\GCS10004\lib\copy.py
import random as random # C:\Users\#Ale\.conda\envs\GCS10004\lib\random.py
import struct as struct # C:\Users\#Ale\.conda\envs\GCS10004\lib\struct.py
import sys as sys # <module 'sys' (built-in)>
import time as time # <module 'time' (built-in)>
import pickle as pickle # C:\Users\#Ale\.conda\envs\GCS10004\lib\pickle.py
import zmq as zmq # C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\zmq\__init__.py
import enum as __enum
import zmq.error as __zmq_error


# Variables with simple values

cPickle = None

IPC_PATH_MAX_LEN = 0

# functions

def _check_version(min_version_info, msg=None): # reliably restored by inspect
    """
    Check for libzmq
    
        raises ZMQVersionError if current zmq version is not at least min_version
    
        min_version_info is a tuple of integers, and will be compared against zmq.zmq_version_info().
    """
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class ZMQError(__zmq_error.ZMQBaseError):
    """
    Wrap an errno style error.
    
        Parameters
        ----------
        errno : int
            The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
            used.
        msg : string
            Description of the error or None.
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        """
        Wrap an errno style error.
        
                Parameters
                ----------
                errno : int
                    The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
                    used.
                msg : string
                    Description of the error or None.
        """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    errno = None
    __annotations__ = {
        'errno': typing.Optional[int],
    }


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


class Socket(object):
    """
    Socket(context, socket_type)
    
        A 0MQ socket.
    
        These objects will generally be constructed via the socket() method of a Context object.
    
        Note: 0MQ Sockets are *not* threadsafe. **DO NOT** share them across threads.
    
        Parameters
        ----------
        context : Context
            The 0MQ Context this Socket belongs to.
        socket_type : int
            The socket type, which can be any of the 0MQ socket types:
            REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, XPUB, XSUB.
    
        See Also
        --------
        .Context.socket : method for creating a socket bound to a Context.
    """
    def bind(self, addr): # real signature unknown; restored from __doc__
        """
        s.bind(addr)
        
                Bind the socket to an address.
        
                This causes the socket to listen on a network port. Sockets on the
                other side of this connection will use ``Socket.connect(addr)`` to
                connect to this socket.
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported include
                    tcp, udp, pgm, epgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def close(self, linger=None): # real signature unknown; restored from __doc__
        """
        s.close(linger=None)
        
                Close the socket.
        
                If linger is specified, LINGER sockopt will be set prior to closing.
        
                This can be called to close the socket by hand. If this is not
                called, the socket will automatically be closed when it is
                garbage collected.
        """
        pass

    def connect(self, addr): # real signature unknown; restored from __doc__
        """
        s.connect(addr)
        
                Connect to a remote 0MQ socket.
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, udp, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def disconnect(self, addr): # real signature unknown; restored from __doc__
        """
        s.disconnect(addr)
        
                Disconnect from a remote 0MQ socket (undoes a call to connect).
        
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, udp, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def get(self, option): # real signature unknown; restored from __doc__
        """
        s.get(option)
        
                Get the value of a socket option.
        
                See the 0MQ API documentation for details on specific options.
        
                Parameters
                ----------
                option : int
                    The option to get.  Available values will depend on your
                    version of libzmq.  Examples include::
        
                        zmq.IDENTITY, HWM, LINGER, FD, EVENTS
        
                Returns
                -------
                optval : int or bytes
                    The value of the option as a bytestring or int.
        """
        pass

    def join(self, group): # real signature unknown; restored from __doc__
        """
        join(group)
        
                Join a RADIO-DISH group
        
                Only for DISH sockets.
        
                libzmq and pyzmq must have been built with ZMQ_BUILD_DRAFT_API
        
                .. versionadded:: 17
        """
        pass

    def leave(self, group): # real signature unknown; restored from __doc__
        """
        leave(group)
        
                Leave a RADIO-DISH group
        
                Only for DISH sockets.
        
                libzmq and pyzmq must have been built with ZMQ_BUILD_DRAFT_API
        
                .. versionadded:: 17
        """
        pass

    def monitor(self, addr, flags): # real signature unknown; restored from __doc__
        """
        s.monitor(addr, flags)
        
                Start publishing socket events on inproc.
                See libzmq docs for zmq_monitor for details.
        
                While this function is available from libzmq 3.2,
                pyzmq cannot parse monitor messages from libzmq prior to 4.0.
        
                .. versionadded: libzmq-3.2
                .. versionadded: 14.0
        
                Parameters
                ----------
                addr : str
                    The inproc url used for monitoring. Passing None as
                    the addr will cause an existing socket monitor to be
                    deregistered.
                events : int [default: zmq.EVENT_ALL]
                    The zmq event bitmask for which events will be sent to the monitor.
        """
        pass

    def recv(self, flags=0, copy=True, track=False): # real signature unknown; restored from __doc__
        """
        s.recv(flags=0, copy=True, track=False)
        
                Receive a message.
        
                With flags=NOBLOCK, this raises :class:`ZMQError` if no messages have
                arrived; otherwise, this waits until a message arrives.
                See :class:`Poller` for more general non-blocking I/O.
        
                Parameters
                ----------
                flags : int
                    0 or NOBLOCK.
                copy : bool
                    Should the message be received in a copying or non-copying manner?
                    If False a Frame object is returned, if True a string copy of
                    message is returned.
                track : bool
                    Should the message be tracked for notification that ZMQ has
                    finished with it? (ignored if copy=True)
        
                Returns
                -------
                msg : bytes or Frame
                    The received message frame.  If `copy` is False, then it will be a Frame,
                    otherwise it will be bytes.
        
                Raises
                ------
                ZMQError
                    for any of the reasons zmq_msg_recv might fail (including if
                    NOBLOCK is set and no new messages have arrived).
        """
        pass

    def send(self, *args, **kwargs): # real signature unknown
        """
        Send a single zmq message frame on this socket.
        
                This queues the message to be sent by the IO thread at a later time.
        
                With flags=NOBLOCK, this raises :class:`ZMQError` if the queue is full;
                otherwise, this waits until space is available.
                See :class:`Poller` for more general non-blocking I/O.
        
                Parameters
                ----------
                data : bytes, Frame, memoryview
                    The content of the message. This can be any object that provides
                    the Python buffer API (`memoryview(data)` can be called).
                flags : int
                    0, NOBLOCK, SNDMORE, or NOBLOCK|SNDMORE.
                copy : bool
                    Should the message be sent in a copying or non-copying manner.
                track : bool
                    Should the message be tracked for notification that ZMQ has
                    finished with it? (ignored if copy=True)
        
                Returns
                -------
                None : if `copy` or not track
                    None if message was sent, raises an exception otherwise.
                MessageTracker : if track and not copy
                    a MessageTracker object, whose `pending` property will
                    be True until the send is completed.
        
                Raises
                ------
                TypeError
                    If a unicode object is passed
                ValueError
                    If `track=True`, but an untracked Frame is passed.
                ZMQError
                    for any of the reasons zmq_msg_send might fail (including
                    if NOBLOCK is set and the outgoing queue is full).
        """
        pass

    def set(self, option, optval): # real signature unknown; restored from __doc__
        """
        s.set(option, optval)
        
                Set socket options.
        
                See the 0MQ API documentation for details on specific options.
        
                Parameters
                ----------
                option : int
                    The option to set.  Available values will depend on your
                    version of libzmq.  Examples include::
        
                        zmq.SUBSCRIBE, UNSUBSCRIBE, IDENTITY, HWM, LINGER, FD
        
                optval : int or bytes
                    The value of the option to set.
        
                Notes
                -----
                .. warning::
        
                    All options other than zmq.SUBSCRIBE, zmq.UNSUBSCRIBE and
                    zmq.LINGER only take effect for subsequent socket bind/connects.
        """
        pass

    def unbind(self, addr): # real signature unknown; restored from __doc__
        """
        s.unbind(addr)
        
                Unbind from an address (undoes a call to bind).
        
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, udp, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def __init__(self, context, socket_type): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The address of the underlying libzmq socket"""

    _closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000233DB7A44B0>'


class SocketOption(__enum.IntEnum):
    """
    Options for Socket.get/set
    
        .. versionadded:: 23
    """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __new_member__(cls, value, opt_type="<_OptType.int: 'int'>"): # reliably restored by inspect
        """ Attach option type as `._opt_type` """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    AFFINITY = 4
    BACKLOG = 19
    BINDTODEVICE = 92
    BLOCKY = 70
    CONFLATE = 54
    CONNECT_RID = 61
    CONNECT_ROUTING_ID = 61
    CONNECT_TIMEOUT = 79
    CURVE_PUBLICKEY = 48
    CURVE_SECRETKEY = 49
    CURVE_SERVER = 47
    CURVE_SERVERKEY = 50
    DELAY_ATTACH_ON_CONNECT = 39
    DISCONNECT_MSG = 111
    EVENTS = 15
    FAIL_UNROUTABLE = 33
    FD = 14
    GSSAPI_PLAINTEXT = 65
    GSSAPI_PRINCIPAL = 63
    GSSAPI_PRINCIPAL_NAMETYPE = 90
    GSSAPI_SERVER = 62
    GSSAPI_SERVICE_PRINCIPAL = 64
    GSSAPI_SERVICE_PRINCIPAL_NAMETYPE = 91
    HANDSHAKE_IVL = 66
    HEARTBEAT_IVL = 75
    HEARTBEAT_TIMEOUT = 77
    HEARTBEAT_TTL = 76
    HELLO_MSG = 110
    HWM = 1
    IDENTITY = 5
    IMMEDIATE = 39
    INVERT_MATCHING = 74
    IN_BATCH_SIZE = 101
    IPC_FILTER_GID = 60
    IPC_FILTER_PID = 58
    IPC_FILTER_UID = 59
    IPV4ONLY = 31
    IPV6 = 42
    LAST_ENDPOINT = 32
    LINGER = 17
    LOOPBACK_FASTPATH = 94
    MAXMSGSIZE = 22
    MECHANISM = 43
    METADATA = 95
    MULTICAST_HOPS = 25
    MULTICAST_LOOP = 96
    MULTICAST_MAXTPDU = 84
    ONLY_FIRST_SUBSCRIBE = 108
    OUT_BATCH_SIZE = 102
    PLAIN_PASSWORD = 46
    PLAIN_SERVER = 44
    PLAIN_USERNAME = 45
    PRIORITY = 112
    PROBE_ROUTER = 51
    RATE = 8
    RCVBUF = 12
    RCVHWM = 24
    RCVMORE = 13
    RCVTIMEO = 27
    RECONNECT_IVL = 18
    RECONNECT_IVL_MAX = 21
    RECONNECT_STOP = 109
    RECOVERY_IVL = 9
    REQ_CORRELATE = 52
    REQ_RELAXED = 53
    ROUTER_BEHAVIOR = 33
    ROUTER_HANDOVER = 56
    ROUTER_MANDATORY = 33
    ROUTER_NOTIFY = 97
    ROUTER_RAW = 41
    ROUTING_ID = 5
    SNDBUF = 11
    SNDHWM = 23
    SNDTIMEO = 28
    SOCKS_PASSWORD = 100
    SOCKS_PROXY = 68
    SOCKS_USERNAME = 99
    STREAM_NOTIFY = 73
    SUBSCRIBE = 6
    TCP_ACCEPT_FILTER = 38
    TCP_KEEPALIVE = 34
    TCP_KEEPALIVE_CNT = 35
    TCP_KEEPALIVE_IDLE = 36
    TCP_KEEPALIVE_INTVL = 37
    TCP_MAXRT = 80
    THREAD_SAFE = 81
    TOS = 57
    TYPE = 16
    UNSUBSCRIBE = 7
    USE_FD = 89
    VMCI_BUFFER_MAX_SIZE = 87
    VMCI_BUFFER_MIN_SIZE = 86
    VMCI_BUFFER_SIZE = 85
    VMCI_CONNECT_TIMEOUT = 88
    WSS_CERT_PEM = 104
    WSS_HOSTNAME = 106
    WSS_KEY_PEM = 103
    WSS_TRUST_PEM = 105
    WSS_TRUST_SYSTEM = 107
    XPUB_MANUAL = 71
    XPUB_MANUAL_LAST_VALUE = 98
    XPUB_NODROP = 69
    XPUB_VERBOSE = 40
    XPUB_VERBOSER = 78
    XPUB_WELCOME_MSG = 72
    ZAP_DOMAIN = 55
    ZAP_ENFORCE_DOMAIN = 93
    _member_map_ = {
        'AFFINITY': 4,
        'BACKLOG': 19,
        'BINDTODEVICE': 92,
        'BLOCKY': 70,
        'CONFLATE': 54,
        'CONNECT_RID': 61,
        'CONNECT_ROUTING_ID': 61,
        'CONNECT_TIMEOUT': 79,
        'CURVE_PUBLICKEY': 48,
        'CURVE_SECRETKEY': 49,
        'CURVE_SERVER': 47,
        'CURVE_SERVERKEY': 50,
        'DELAY_ATTACH_ON_CONNECT': 39,
        'DISCONNECT_MSG': 111,
        'EVENTS': 15,
        'FAIL_UNROUTABLE': 33,
        'FD': 14,
        'GSSAPI_PLAINTEXT': 65,
        'GSSAPI_PRINCIPAL': 63,
        'GSSAPI_PRINCIPAL_NAMETYPE': 90,
        'GSSAPI_SERVER': 62,
        'GSSAPI_SERVICE_PRINCIPAL': 64,
        'GSSAPI_SERVICE_PRINCIPAL_NAMETYPE': 91,
        'HANDSHAKE_IVL': 66,
        'HEARTBEAT_IVL': 75,
        'HEARTBEAT_TIMEOUT': 77,
        'HEARTBEAT_TTL': 76,
        'HELLO_MSG': 110,
        'HWM': 1,
        'IDENTITY': 5,
        'IMMEDIATE': 39,
        'INVERT_MATCHING': 74,
        'IN_BATCH_SIZE': 101,
        'IPC_FILTER_GID': 60,
        'IPC_FILTER_PID': 58,
        'IPC_FILTER_UID': 59,
        'IPV4ONLY': 31,
        'IPV6': 42,
        'LAST_ENDPOINT': 32,
        'LINGER': 17,
        'LOOPBACK_FASTPATH': 94,
        'MAXMSGSIZE': 22,
        'MECHANISM': 43,
        'METADATA': 95,
        'MULTICAST_HOPS': 25,
        'MULTICAST_LOOP': 96,
        'MULTICAST_MAXTPDU': 84,
        'ONLY_FIRST_SUBSCRIBE': 108,
        'OUT_BATCH_SIZE': 102,
        'PLAIN_PASSWORD': 46,
        'PLAIN_SERVER': 44,
        'PLAIN_USERNAME': 45,
        'PRIORITY': 112,
        'PROBE_ROUTER': 51,
        'RATE': 8,
        'RCVBUF': 12,
        'RCVHWM': 24,
        'RCVMORE': 13,
        'RCVTIMEO': 27,
        'RECONNECT_IVL': 18,
        'RECONNECT_IVL_MAX': 21,
        'RECONNECT_STOP': 109,
        'RECOVERY_IVL': 9,
        'REQ_CORRELATE': 52,
        'REQ_RELAXED': 53,
        'ROUTER_BEHAVIOR': 33,
        'ROUTER_HANDOVER': 56,
        'ROUTER_MANDATORY': 33,
        'ROUTER_NOTIFY': 97,
        'ROUTER_RAW': 41,
        'ROUTING_ID': 5,
        'SNDBUF': 11,
        'SNDHWM': 23,
        'SNDTIMEO': 28,
        'SOCKS_PASSWORD': 100,
        'SOCKS_PROXY': 68,
        'SOCKS_USERNAME': 99,
        'STREAM_NOTIFY': 73,
        'SUBSCRIBE': 6,
        'TCP_ACCEPT_FILTER': 38,
        'TCP_KEEPALIVE': 34,
        'TCP_KEEPALIVE_CNT': 35,
        'TCP_KEEPALIVE_IDLE': 36,
        'TCP_KEEPALIVE_INTVL': 37,
        'TCP_MAXRT': 80,
        'THREAD_SAFE': 81,
        'TOS': 57,
        'TYPE': 16,
        'UNSUBSCRIBE': 7,
        'USE_FD': 89,
        'VMCI_BUFFER_MAX_SIZE': 87,
        'VMCI_BUFFER_MIN_SIZE': 86,
        'VMCI_BUFFER_SIZE': 85,
        'VMCI_CONNECT_TIMEOUT': 88,
        'WSS_CERT_PEM': 104,
        'WSS_HOSTNAME': 106,
        'WSS_KEY_PEM': 103,
        'WSS_TRUST_PEM': 105,
        'WSS_TRUST_SYSTEM': 107,
        'XPUB_MANUAL': 71,
        'XPUB_MANUAL_LAST_VALUE': 98,
        'XPUB_NODROP': 69,
        'XPUB_VERBOSE': 40,
        'XPUB_VERBOSER': 78,
        'XPUB_WELCOME_MSG': 72,
        'ZAP_DOMAIN': 55,
        'ZAP_ENFORCE_DOMAIN': 93,
    }
    _member_names_ = [
        'HWM',
        'AFFINITY',
        'ROUTING_ID',
        'SUBSCRIBE',
        'UNSUBSCRIBE',
        'RATE',
        'RECOVERY_IVL',
        'SNDBUF',
        'RCVBUF',
        'RCVMORE',
        'FD',
        'EVENTS',
        'TYPE',
        'LINGER',
        'RECONNECT_IVL',
        'BACKLOG',
        'RECONNECT_IVL_MAX',
        'MAXMSGSIZE',
        'SNDHWM',
        'RCVHWM',
        'MULTICAST_HOPS',
        'RCVTIMEO',
        'SNDTIMEO',
        'LAST_ENDPOINT',
        'ROUTER_MANDATORY',
        'TCP_KEEPALIVE',
        'TCP_KEEPALIVE_CNT',
        'TCP_KEEPALIVE_IDLE',
        'TCP_KEEPALIVE_INTVL',
        'IMMEDIATE',
        'XPUB_VERBOSE',
        'ROUTER_RAW',
        'IPV6',
        'MECHANISM',
        'PLAIN_SERVER',
        'PLAIN_USERNAME',
        'PLAIN_PASSWORD',
        'CURVE_SERVER',
        'CURVE_PUBLICKEY',
        'CURVE_SECRETKEY',
        'CURVE_SERVERKEY',
        'PROBE_ROUTER',
        'REQ_CORRELATE',
        'REQ_RELAXED',
        'CONFLATE',
        'ZAP_DOMAIN',
        'ROUTER_HANDOVER',
        'TOS',
        'CONNECT_ROUTING_ID',
        'GSSAPI_SERVER',
        'GSSAPI_PRINCIPAL',
        'GSSAPI_SERVICE_PRINCIPAL',
        'GSSAPI_PLAINTEXT',
        'HANDSHAKE_IVL',
        'SOCKS_PROXY',
        'XPUB_NODROP',
        'BLOCKY',
        'XPUB_MANUAL',
        'XPUB_WELCOME_MSG',
        'STREAM_NOTIFY',
        'INVERT_MATCHING',
        'HEARTBEAT_IVL',
        'HEARTBEAT_TTL',
        'HEARTBEAT_TIMEOUT',
        'XPUB_VERBOSER',
        'CONNECT_TIMEOUT',
        'TCP_MAXRT',
        'THREAD_SAFE',
        'MULTICAST_MAXTPDU',
        'VMCI_BUFFER_SIZE',
        'VMCI_BUFFER_MIN_SIZE',
        'VMCI_BUFFER_MAX_SIZE',
        'VMCI_CONNECT_TIMEOUT',
        'USE_FD',
        'GSSAPI_PRINCIPAL_NAMETYPE',
        'GSSAPI_SERVICE_PRINCIPAL_NAMETYPE',
        'BINDTODEVICE',
        'TCP_ACCEPT_FILTER',
        'IPC_FILTER_PID',
        'IPC_FILTER_UID',
        'IPC_FILTER_GID',
        'IPV4ONLY',
        'ZAP_ENFORCE_DOMAIN',
        'LOOPBACK_FASTPATH',
        'METADATA',
        'MULTICAST_LOOP',
        'ROUTER_NOTIFY',
        'XPUB_MANUAL_LAST_VALUE',
        'SOCKS_USERNAME',
        'SOCKS_PASSWORD',
        'IN_BATCH_SIZE',
        'OUT_BATCH_SIZE',
        'WSS_KEY_PEM',
        'WSS_CERT_PEM',
        'WSS_TRUST_PEM',
        'WSS_HOSTNAME',
        'WSS_TRUST_SYSTEM',
        'ONLY_FIRST_SUBSCRIBE',
        'RECONNECT_STOP',
        'HELLO_MSG',
        'DISCONNECT_MSG',
        'PRIORITY',
    ]
    _member_type_ = int
    _value2member_map_ = {
        1: 1,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        27: 27,
        28: 28,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
        44: 44,
        45: 45,
        46: 46,
        47: 47,
        48: 48,
        49: 49,
        50: 50,
        51: 51,
        52: 52,
        53: 53,
        54: 54,
        55: 55,
        56: 56,
        57: 57,
        58: 58,
        59: 59,
        60: 60,
        61: 61,
        62: 62,
        63: 63,
        64: 64,
        65: 65,
        66: 66,
        68: 68,
        69: 69,
        70: 70,
        71: 71,
        72: 72,
        73: 73,
        74: 74,
        75: 75,
        76: 76,
        77: 77,
        78: 78,
        79: 79,
        80: 80,
        81: 81,
        84: 84,
        85: 85,
        86: 86,
        87: 87,
        88: 88,
        89: 89,
        90: 90,
        91: 91,
        92: 92,
        93: 93,
        94: 94,
        95: 95,
        96: 96,
        97: 97,
        98: 98,
        99: 99,
        100: 100,
        101: 101,
        102: 102,
        103: 103,
        104: 104,
        105: 105,
        106: 106,
        107: 107,
        108: 108,
        109: 109,
        110: 110,
        111: 111,
        112: 112,
    }
    __annotations__ = {
        '_opt_type': str,
    }


class ZMQBindError(__zmq_error.ZMQBaseError):
    """
    An error for ``Socket.bind_to_random_port()``.
    
        See Also
        --------
        .Socket.bind_to_random_port
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class _OptType(__enum.Enum):
    """ An enumeration. """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    bytes = None # (!) real value is "<_OptType.bytes: 'bytes'>"
    fd = None # (!) real value is "<_OptType.fd: 'fd'>"
    int = None # (!) real value is "<_OptType.int: 'int'>"
    int64 = None # (!) real value is "<_OptType.int64: 'int64'>"
    _member_map_ = {
        'bytes': None, # (!) real value is "<_OptType.bytes: 'bytes'>"
        'fd': None, # (!) real value is "<_OptType.fd: 'fd'>"
        'int': None, # (!) real value is "<_OptType.int: 'int'>"
        'int64': None, # (!) real value is "<_OptType.int64: 'int64'>"
    }
    _member_names_ = [
        'int',
        'int64',
        'bytes',
        'fd',
    ]
    _member_type_ = object
    _value2member_map_ = {
        'bytes': None, # (!) real value is "<_OptType.bytes: 'bytes'>"
        'fd': None, # (!) real value is "<_OptType.fd: 'fd'>"
        'int': None, # (!) real value is "<_OptType.int: 'int'>"
        'int64': None, # (!) real value is "<_OptType.int64: 'int64'>"
    }


# variables with complex values

__all__ = [
    'Socket',
    'IPC_PATH_MAX_LEN',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000233DB7A4520>'

__spec__ = None # (!) real value is "ModuleSpec(name='zmq.backend.cython.socket', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000233DB7A4520>, origin='C:\\\\Users\\\\#Ale\\\\.conda\\\\envs\\\\GCS10004\\\\lib\\\\site-packages\\\\zmq\\\\backend\\\\cython\\\\socket.cp39-win_amd64.pyd')"

__test__ = {}

