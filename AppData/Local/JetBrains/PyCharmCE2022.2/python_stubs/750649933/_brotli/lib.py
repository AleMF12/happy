# encoding: utf-8
# module _brotli.lib
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\brotli\_brotli.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

BROTLI_DECODER_RESULT_ERROR = 0

BROTLI_DECODER_RESULT_NEEDS_MORE_INPUT = 2
BROTLI_DECODER_RESULT_NEEDS_MORE_OUTPUT = 3

BROTLI_DECODER_RESULT_SUCCESS = 1

BROTLI_DEFAULT_MODE = 0
BROTLI_DEFAULT_QUALITY = 11
BROTLI_DEFAULT_WINDOW = 22

BROTLI_FALSE = 0

BROTLI_MODE_FONT = 2
BROTLI_MODE_GENERIC = 0
BROTLI_MODE_TEXT = 1

BROTLI_OPERATION_FINISH = 2
BROTLI_OPERATION_FLUSH = 1
BROTLI_OPERATION_PROCESS = 0

BROTLI_PARAM_LGBLOCK = 3
BROTLI_PARAM_LGWIN = 2
BROTLI_PARAM_MODE = 0
BROTLI_PARAM_QUALITY = 1

BROTLI_TRUE = 1

# functions

def BrotliDecoderCreateInstance(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BrotliDecoderState *BrotliDecoderCreateInstance(void *(*)(void *, size_t), void(*)(void *, void *), void *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliDecoderDecompressStream(BrotliDecoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BrotliDecoderResult BrotliDecoderDecompressStream(BrotliDecoderState *, size_t *, uint8_t * *, size_t *, uint8_t * *, size_t *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliDecoderDestroyInstance(BrotliDecoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BrotliDecoderDestroyInstance(BrotliDecoderState *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliDecoderErrorString(BrotliDecoderErrorCode): # real signature unknown; restored from __doc__
    """
    char *BrotliDecoderErrorString(BrotliDecoderErrorCode);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliDecoderGetErrorCode(BrotliDecoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BrotliDecoderErrorCode BrotliDecoderGetErrorCode(BrotliDecoderState *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliDecoderHasMoreOutput(BrotliDecoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    _Bool BrotliDecoderHasMoreOutput(BrotliDecoderState *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliDecoderIsFinished(BrotliDecoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    _Bool BrotliDecoderIsFinished(BrotliDecoderState *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliDecoderIsUsed(BrotliDecoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    _Bool BrotliDecoderIsUsed(BrotliDecoderState *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliDecoderSetCustomDictionary(BrotliDecoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BrotliDecoderSetCustomDictionary(BrotliDecoderState *, size_t, uint8_t *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliEncoderCompress(p_int, p_int_1, enum_BrotliEncoderMode, size_t, uint8_t, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    _Bool BrotliEncoderCompress(int, int, enum BrotliEncoderMode, size_t, uint8_t *, size_t *, uint8_t *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliEncoderCompressStream(BrotliEncoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    _Bool BrotliEncoderCompressStream(BrotliEncoderState *, enum BrotliEncoderOperation, size_t *, uint8_t * *, size_t *, uint8_t * *, size_t *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliEncoderCreateInstance(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    BrotliEncoderState *BrotliEncoderCreateInstance(void *(*)(void *, size_t), void(*)(void *, void *), void *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliEncoderDestroyInstance(BrotliEncoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BrotliEncoderDestroyInstance(BrotliEncoderState *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliEncoderHasMoreOutput(BrotliEncoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    _Bool BrotliEncoderHasMoreOutput(BrotliEncoderState *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliEncoderIsFinished(BrotliEncoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    _Bool BrotliEncoderIsFinished(BrotliEncoderState *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliEncoderSetCustomDictionary(BrotliEncoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void BrotliEncoderSetCustomDictionary(BrotliEncoderState *, size_t, uint8_t *);
    
    CFFI C function from _brotli.lib
    """
    pass

def BrotliEncoderSetParameter(BrotliEncoderState, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    _Bool BrotliEncoderSetParameter(BrotliEncoderState *, enum BrotliEncoderParameter, uint32_t);
    
    CFFI C function from _brotli.lib
    """
    pass

# no classes
