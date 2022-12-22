# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QAudioEncoderSettingsControl(QMediaControl):
    """ QAudioEncoderSettingsControl(parent: QObject = None) """
    def audioSettings(self): # real signature unknown; restored from __doc__
        """ audioSettings(self) -> QAudioEncoderSettings """
        return QAudioEncoderSettings

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def codecDescription(self, p_str): # real signature unknown; restored from __doc__
        """ codecDescription(self, str) -> str """
        return ""

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

    def setAudioSettings(self, QAudioEncoderSettings): # real signature unknown; restored from __doc__
        """ setAudioSettings(self, QAudioEncoderSettings) """
        pass

    def supportedAudioCodecs(self): # real signature unknown; restored from __doc__
        """ supportedAudioCodecs(self) -> List[str] """
        return []

    def supportedSampleRates(self, QAudioEncoderSettings): # real signature unknown; restored from __doc__
        """ supportedSampleRates(self, QAudioEncoderSettings) -> Tuple[List[int], bool] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


