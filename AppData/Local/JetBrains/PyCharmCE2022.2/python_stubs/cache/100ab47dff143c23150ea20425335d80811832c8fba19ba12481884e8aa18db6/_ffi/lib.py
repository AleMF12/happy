# encoding: utf-8
# module _ffi.lib
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\_argon2_cffi_bindings\_ffi.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ARGON2_AD_PTR_MISMATCH = -21

ARGON2_AD_TOO_LONG = -9
ARGON2_AD_TOO_SHORT = -8

ARGON2_ALLOCATE_MEMORY_CBK_NULL = -24

Argon2_d = 0

ARGON2_DECODING_FAIL = -32

ARGON2_DECODING_LENGTH_FAIL = -34

ARGON2_DEFAULT_FLAGS = 0

ARGON2_ENCODING_FAIL = -31

ARGON2_FLAG_CLEAR_PASSWORD = 1
ARGON2_FLAG_CLEAR_SECRET = 2

ARGON2_FREE_MEMORY_CBK_NULL = -23

Argon2_i = 1
Argon2_id = 2

ARGON2_INCORRECT_PARAMETER = -25
ARGON2_INCORRECT_TYPE = -26

ARGON2_LANES_TOO_FEW = -16
ARGON2_LANES_TOO_MANY = -17

ARGON2_MAX_AD_LENGTH = 4294967295

ARGON2_MAX_LANES = 16777215
ARGON2_MAX_MEMORY = 4294967295

ARGON2_MAX_MEMORY_BITS = 32

ARGON2_MAX_OUTLEN = 4294967295

ARGON2_MAX_PWD_LENGTH = 4294967295

ARGON2_MAX_SALT_LENGTH = 4294967295

ARGON2_MAX_SECRET = 4294967295
ARGON2_MAX_THREADS = 16777215
ARGON2_MAX_TIME = 4294967295

ARGON2_MEMORY_ALLOCATION_ERROR = -22

ARGON2_MEMORY_TOO_LITTLE = -14
ARGON2_MEMORY_TOO_MUCH = -15

ARGON2_MIN_AD_LENGTH = 0

ARGON2_MIN_LANES = 1
ARGON2_MIN_MEMORY = 8
ARGON2_MIN_OUTLEN = 4

ARGON2_MIN_PWD_LENGTH = 0

ARGON2_MIN_SALT_LENGTH = 8

ARGON2_MIN_SECRET = 0
ARGON2_MIN_THREADS = 1
ARGON2_MIN_TIME = 1

ARGON2_MISSING_ARGS = -30

ARGON2_OK = 0

ARGON2_OUTPUT_PTR_NULL = -1

ARGON2_OUTPUT_TOO_LONG = -3
ARGON2_OUTPUT_TOO_SHORT = -2

ARGON2_OUT_PTR_MISMATCH = -27

ARGON2_PWD_PTR_MISMATCH = -18

ARGON2_PWD_TOO_LONG = -5
ARGON2_PWD_TOO_SHORT = -4

ARGON2_SALT_PTR_MISMATCH = -19

ARGON2_SALT_TOO_LONG = -7
ARGON2_SALT_TOO_SHORT = -6

ARGON2_SECRET_PTR_MISMATCH = -20

ARGON2_SECRET_TOO_LONG = -11
ARGON2_SECRET_TOO_SHORT = -10

ARGON2_SYNC_POINTS = 4

ARGON2_THREADS_TOO_FEW = -28
ARGON2_THREADS_TOO_MANY = -29

ARGON2_THREAD_FAIL = -33

ARGON2_TIME_TOO_LARGE = -13
ARGON2_TIME_TOO_SMALL = -12

ARGON2_VERIFY_MISMATCH = -35

ARGON2_VERSION_10 = 16
ARGON2_VERSION_13 = 19
ARGON2_VERSION_NUMBER = 19

# functions

def argon2_ctx(struct_Argon2_Context, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int argon2_ctx(struct Argon2_Context *, enum Argon2_type);
    
    CFFI C function from _ffi.lib
    """
    pass

def argon2_encodedlen(uint32_t, uint32_t_1, uint32_t_2, uint32_t_3, uint32_t_4, enum_Argon2_type): # real signature unknown; restored from __doc__
    """
    uint32_t argon2_encodedlen(uint32_t, uint32_t, uint32_t, uint32_t, uint32_t, enum Argon2_type);
    
    CFFI C function from _ffi.lib
    """
    pass

def argon2_error_message(p_int): # real signature unknown; restored from __doc__
    """
    char *argon2_error_message(int);
    
    CFFI C function from _ffi.lib
    """
    pass

def argon2_hash(uint32_t, uint32_t_1, uint32_t_2, void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int argon2_hash(uint32_t, uint32_t, uint32_t, void *, size_t, void *, size_t, void *, size_t, char *, size_t, enum Argon2_type, uint32_t);
    
    CFFI C function from _ffi.lib
    """
    pass

def argon2_verify(char, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int argon2_verify(char *, void *, size_t, enum Argon2_type);
    
    CFFI C function from _ffi.lib
    """
    pass

# no classes
