# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QMediaGaplessPlaybackControl(QMediaControl):
    """ QMediaGaplessPlaybackControl(parent: QObject = None) """
    def advancedToNextMedia(self): # real signature unknown; restored from __doc__
        """ advancedToNextMedia(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def crossfadeTime(self): # real signature unknown; restored from __doc__
        """ crossfadeTime(self) -> float """
        return 0.0

    def crossfadeTimeChanged(self, p_float): # real signature unknown; restored from __doc__
        """ crossfadeTimeChanged(self, float) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isCrossfadeSupported(self): # real signature unknown; restored from __doc__
        """ isCrossfadeSupported(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def nextMedia(self): # real signature unknown; restored from __doc__
        """ nextMedia(self) -> QMediaContent """
        return QMediaContent

    def nextMediaChanged(self, QMediaContent): # real signature unknown; restored from __doc__
        """ nextMediaChanged(self, QMediaContent) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCrossfadeTime(self, p_float): # real signature unknown; restored from __doc__
        """ setCrossfadeTime(self, float) """
        pass

    def setNextMedia(self, QMediaContent): # real signature unknown; restored from __doc__
        """ setNextMedia(self, QMediaContent) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


