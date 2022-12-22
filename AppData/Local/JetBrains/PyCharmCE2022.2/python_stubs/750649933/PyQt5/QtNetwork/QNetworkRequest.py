# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkRequest(__sip.simplewrapper):
    """
    QNetworkRequest(url: QUrl = QUrl())
    QNetworkRequest(QNetworkRequest)
    """
    def attribute(self, QNetworkRequest_Attribute, defaultValue=None): # real signature unknown; restored from __doc__
        """ attribute(self, QNetworkRequest.Attribute, defaultValue: Any = None) -> Any """
        pass

    def hasRawHeader(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ hasRawHeader(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def header(self, QNetworkRequest_KnownHeaders): # real signature unknown; restored from __doc__
        """ header(self, QNetworkRequest.KnownHeaders) -> Any """
        pass

    def http2Configuration(self): # real signature unknown; restored from __doc__
        """ http2Configuration(self) -> QHttp2Configuration """
        return QHttp2Configuration

    def maximumRedirectsAllowed(self): # real signature unknown; restored from __doc__
        """ maximumRedirectsAllowed(self) -> int """
        return 0

    def originatingObject(self): # real signature unknown; restored from __doc__
        """ originatingObject(self) -> QObject """
        pass

    def peerVerifyName(self): # real signature unknown; restored from __doc__
        """ peerVerifyName(self) -> str """
        return ""

    def priority(self): # real signature unknown; restored from __doc__
        """ priority(self) -> QNetworkRequest.Priority """
        pass

    def rawHeader(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ rawHeader(self, Union[QByteArray, bytes, bytearray]) -> QByteArray """
        pass

    def rawHeaderList(self): # real signature unknown; restored from __doc__
        """ rawHeaderList(self) -> List[QByteArray] """
        return []

    def setAttribute(self, QNetworkRequest_Attribute, Any): # real signature unknown; restored from __doc__
        """ setAttribute(self, QNetworkRequest.Attribute, Any) """
        pass

    def setHeader(self, QNetworkRequest_KnownHeaders, Any): # real signature unknown; restored from __doc__
        """ setHeader(self, QNetworkRequest.KnownHeaders, Any) """
        pass

    def setHttp2Configuration(self, QHttp2Configuration): # real signature unknown; restored from __doc__
        """ setHttp2Configuration(self, QHttp2Configuration) """
        pass

    def setMaximumRedirectsAllowed(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumRedirectsAllowed(self, int) """
        pass

    def setOriginatingObject(self, QObject): # real signature unknown; restored from __doc__
        """ setOriginatingObject(self, QObject) """
        pass

    def setPeerVerifyName(self, p_str): # real signature unknown; restored from __doc__
        """ setPeerVerifyName(self, str) """
        pass

    def setPriority(self, QNetworkRequest_Priority): # real signature unknown; restored from __doc__
        """ setPriority(self, QNetworkRequest.Priority) """
        pass

    def setRawHeader(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setRawHeader(self, Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray]) """
        pass

    def setSslConfiguration(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, QSslConfiguration) """
        pass

    def setTransferTimeout(self, timeout=None): # real signature unknown; restored from __doc__
        """ setTransferTimeout(self, timeout: int = QNetworkRequest.TransferTimeoutConstant.DefaultTransferTimeoutConstant) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> QSslConfiguration """
        return QSslConfiguration

    def swap(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ swap(self, QNetworkRequest) """
        pass

    def transferTimeout(self): # real signature unknown; restored from __doc__
        """ transferTimeout(self) -> int """
        return 0

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AlwaysCache = 3
    AlwaysNetwork = 0
    AuthenticationReuseAttribute = 12
    AutoDeleteReplyOnFinishAttribute = 28
    Automatic = 0
    BackgroundRequestAttribute = 17
    CacheLoadControlAttribute = 4
    CacheSaveControlAttribute = 5
    ConnectionEncryptedAttribute = 3
    ContentDispositionHeader = 6
    ContentLengthHeader = 1
    ContentTypeHeader = 0
    CookieHeader = 4
    CookieLoadControlAttribute = 11
    CookieSaveControlAttribute = 13
    CustomVerbAttribute = 10
    DefaultTransferTimeoutConstant = 30000
    DoNotBufferUploadDataAttribute = 7
    EmitAllUploadProgressSignalsAttribute = 20
    ETagHeader = 10
    FollowRedirectsAttribute = 21
    HighPriority = 1
    HTTP2AllowedAttribute = 22
    Http2AllowedAttribute = 22
    Http2DirectAttribute = 26
    HTTP2WasUsedAttribute = 23
    Http2WasUsedAttribute = 23
    HttpPipeliningAllowedAttribute = 8
    HttpPipeliningWasUsedAttribute = 9
    HttpReasonPhraseAttribute = 1
    HttpStatusCodeAttribute = 0
    IfMatchHeader = 11
    IfModifiedSinceHeader = 9
    IfNoneMatchHeader = 12
    LastModifiedHeader = 3
    LocationHeader = 2
    LowPriority = 5
    Manual = 1
    ManualRedirectPolicy = 0
    NoLessSafeRedirectPolicy = 1
    NormalPriority = 3
    OriginalContentLengthAttribute = 24
    PreferCache = 2
    PreferNetwork = 1
    RedirectionTargetAttribute = 2
    RedirectPolicyAttribute = 25
    SameOriginRedirectPolicy = 2
    ServerHeader = 8
    SetCookieHeader = 5
    SourceIsFromCacheAttribute = 6
    SpdyAllowedAttribute = 18
    SpdyWasUsedAttribute = 19
    User = 1000
    UserAgentHeader = 7
    UserMax = 32767
    UserVerifiedRedirectPolicy = 3
    __hash__ = None


