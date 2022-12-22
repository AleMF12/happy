# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QAudioDecoderControl(QMediaControl):
    """ QAudioDecoderControl(parent: QObject = None) """
    def audioFormat(self): # real signature unknown; restored from __doc__
        """ audioFormat(self) -> QAudioFormat """
        return QAudioFormat

    def bufferAvailable(self): # real signature unknown; restored from __doc__
        """ bufferAvailable(self) -> bool """
        return False

    def bufferAvailableChanged(self, bool): # real signature unknown; restored from __doc__
        """ bufferAvailableChanged(self, bool) [signal] """
        pass

    def bufferReady(self): # real signature unknown; restored from __doc__
        """ bufferReady(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def durationChanged(self, p_int): # real signature unknown; restored from __doc__
        """ durationChanged(self, int) [signal] """
        pass

    def error(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ error(self, int, str) [signal] """
        pass

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def formatChanged(self, QAudioFormat): # real signature unknown; restored from __doc__
        """ formatChanged(self, QAudioFormat) [signal] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def positionChanged(self, p_int): # real signature unknown; restored from __doc__
        """ positionChanged(self, int) [signal] """
        pass

    def read(self): # real signature unknown; restored from __doc__
        """ read(self) -> QAudioBuffer """
        return QAudioBuffer

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAudioFormat(self, QAudioFormat): # real signature unknown; restored from __doc__
        """ setAudioFormat(self, QAudioFormat) """
        pass

    def setSourceDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setSourceDevice(self, QIODevice) """
        pass

    def setSourceFilename(self, p_str): # real signature unknown; restored from __doc__
        """ setSourceFilename(self, str) """
        pass

    def sourceChanged(self): # real signature unknown; restored from __doc__
        """ sourceChanged(self) [signal] """
        pass

    def sourceDevice(self): # real signature unknown; restored from __doc__
        """ sourceDevice(self) -> QIODevice """
        pass

    def sourceFilename(self): # real signature unknown; restored from __doc__
        """ sourceFilename(self) -> str """
        return ""

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAudioDecoder.State """
        pass

    def stateChanged(self, QAudioDecoder_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QAudioDecoder.State) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


