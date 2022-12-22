# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QVideoEncoderSettingsControl(QMediaControl):
    """ QVideoEncoderSettingsControl(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setVideoSettings(self, QVideoEncoderSettings): # real signature unknown; restored from __doc__
        """ setVideoSettings(self, QVideoEncoderSettings) """
        pass

    def supportedFrameRates(self, QVideoEncoderSettings): # real signature unknown; restored from __doc__
        """ supportedFrameRates(self, QVideoEncoderSettings) -> Tuple[List[float], bool] """
        pass

    def supportedResolutions(self, QVideoEncoderSettings): # real signature unknown; restored from __doc__
        """ supportedResolutions(self, QVideoEncoderSettings) -> Tuple[List[QSize], bool] """
        pass

    def supportedVideoCodecs(self): # real signature unknown; restored from __doc__
        """ supportedVideoCodecs(self) -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def videoCodecDescription(self, p_str): # real signature unknown; restored from __doc__
        """ videoCodecDescription(self, str) -> str """
        return ""

    def videoSettings(self): # real signature unknown; restored from __doc__
        """ videoSettings(self) -> QVideoEncoderSettings """
        return QVideoEncoderSettings

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


