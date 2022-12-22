# encoding: utf-8
# module winpty.winpty
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\winpty\winpty.cp39-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

__version__ = '2.0.2'

# no functions
# classes

class PTY(object):
    """
    Create a pseudo terminal (PTY) of a given size.
    
    The pseudo-terminal must define a non-zero, positive size for both columns and rows.
    
    Arguments
    ---------
    cols: int
        Number of columns (width) that the pseudo-terminal should have in characters.
    rows: int
        Number of rows (height) that the pseudo-terminal should have in characters.
    backend: Optional[int]
        Pseudo-terminal backend to use, see `winpty.Backend`. If None, then the backend
        will be set automatically based on the available APIs.
    mouse_mode: Optional[int]
        Set the mouse mode to one of the WINPTY_MOUSE_MODE_xxx constants.
        See `winpty.MouseMode`. Default: 0.
    timeout: Optional[int]
        Amount of time to wait for the agent (in ms) to startup and to wait for any given
        agent RPC request.  Must be greater than 0. Default: 30000.
    agent_config: Optional[int]
        A set of zero or more WINPTY_FLAG_xxx values. See `winpty.AgentConfig`.
        Default: WINPTY_FLAG_COLOR_ESCAPES
    
    Raises
    ------
    WinptyError:
        If an error occurred whilist creating the pseudo terminal instance.
    
    Notes
    -----
    1. Optional argument values will take effect if and only if the backend is set to
    `winpty.Backend.Winpty`, either automatically or manually.
    
    2. ConPTY backend will take precedence over WinPTY, as it is native to Windows
    and therefore is faster.
    
    3. Automatic backend selection will be determined based on both the compilation
    flags used to compile pywinpty and the availability of the APIs on the runtime
    system.
    """
    def get_exitstatus(self, *args, **kwargs): # real signature unknown
        """
        Determine the exit status code of the process that is running behind the pseudoterminal.
        
        Returns
        -------
        status: Optional[int]
            None if the process has not started nor finished, otherwise it corresponds to the
            status code at the time of exit.
        
        Raises
        ------
        WinptyError
            If there was an error whilst trying to determine the exit status of the process.
        """
        pass

    def isalive(self, *args, **kwargs): # real signature unknown
        """
        Determine if the application process that is running behind the pseudoterminal is alive.
        
        Returns
        -------
        alive: bool
            True, the process is alive. False, otherwise.
        
        Raises
        ------
        WinptyError
            If there was an error whilst trying to determine the status of the process.
        """
        pass

    def iseof(self, *args, **kwargs): # real signature unknown
        """
        Determine if the application process that is running behind the pseudoterminal reached EOF.
        
        Returns
        -------
        eof: False
            True, if the process emitted the end-of-file escape sequence. False, otherwise.
        
        Raises
        ------
        WinptyError
            If there was an error whilst trying to determine the EOF status of the process.
        """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """
        Read a number of bytes from the pseudoterminal output stream.
        
        Arguments
        ---------
        length: int
            Maximum number of bytes to read from the pseudoterminal.
        blocking: bool
            If True, the call will be blocked until the requested number of bytes
            are available to read. Otherwise, it will return an empty byte string
            if there are no available bytes to read.
        
        Returns
        -------
        output: bytes
            A byte string that contains the output of the pseudoterminal.
        
        Raises
        ------
        WinptyError
            If there was an error whilst trying to read the requested number of bytes
            from the pseudoterminal.
        
        Notes
        -----
        Use the `blocking=True` mode only if the process is awaiting on a thread, otherwise
        this call may block your application, which only can be interrupted by killing the
        process.
        """
        pass

    def set_size(self, *args, **kwargs): # real signature unknown
        """
        Modify the size of the pseudo terminal.
        
        The value for the columns and rows should be non-zero and positive.
        
        Arguments
        ---------
        cols: int
            Size in characters that the pseudo terminal should have.
        rows: int
            Size in characters that the pseudo terminal should have.
        
        Raises
        ------
        WinptyError
            If an error occurred whilist resizing the pseudo terminal.
        """
        pass

    def spawn(self, *args, **kwargs): # real signature unknown
        """
        Start an application that will communicate through the pseudo-terminal.
        
        Arguments
        ---------
        appname: bytes
            Byte string that contains the path to the application that will
            be started.
        cmdline: Optional[bytes]
            Byte string that contains the parameters to start the application,
            separated by whitespace.
        cwd: Optional[bytes]
            Byte string that contains the working directory that the application
            should have. If None, the application will inherit the current working
            directory of the Python interpreter.
        env: Optional[bytes]
            Byte string that contains the name and values of the environment
            variables that the application should have. Each (name, value) pair
            should be declared as `name=value` and each pair must be separated
            by an empty byte `\0`. If None, then the application will inherit
            the environment variables of the Python interpreter.
        
        Returns
        -------
        spawned: bool
            True if the application was started successfully and False otherwise.
        
        Raises
        ------
        WinptyError
            If an error occurred when trying to start the application process.
        
        Notes
        -----
        For a more detailed information about the values of the arguments, see:
        https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
        """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Write a byte string into the pseudoterminal input stream.
        
        Arguments
        ---------
        to_write: bytes
            The byte sequence that is going to be sent to the pseudoterminal.
        
        Returns
        -------
        num_bytes: int
            The number of bytes that were written successfully.
        
        Raises
        ------
        WinptyError
            If there was an error whilst trying to write the requested number of bytes
            into the pseudoterminal.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    fd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the process handle number."""

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the process identifier (PID) of the running process."""



class WinptyError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__all__ = [
    '__version__',
    'WinptyError',
    'PTY',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026DF146C370>'

__spec__ = None # (!) real value is "ModuleSpec(name='winpty.winpty', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026DF146C370>, origin='C:\\\\Users\\\\#Ale\\\\.conda\\\\envs\\\\GCS10004\\\\lib\\\\site-packages\\\\winpty\\\\winpty.cp39-win_amd64.pyd')"

