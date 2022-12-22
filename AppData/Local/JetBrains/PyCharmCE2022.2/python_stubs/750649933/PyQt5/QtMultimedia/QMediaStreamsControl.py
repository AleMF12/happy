# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QMediaStreamsControl(QMediaControl):
    """ QMediaStreamsControl(parent: QObject = None) """
    def activeStreamsChanged(self): # real signature unknown; restored from __doc__
        """ activeStreamsChanged(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, p_int): # real signature unknown; restored from __doc__
        """ isActive(self, int) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def metaData(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ metaData(self, int, str) -> Any """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActive(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setActive(self, int, bool) """
        pass

    def streamCount(self): # real signature unknown; restored from __doc__
        """ streamCount(self) -> int """
        return 0

    def streamsChanged(self): # real signature unknown; restored from __doc__
        """ streamsChanged(self) [signal] """
        pass

    def streamType(self, p_int): # real signature unknown; restored from __doc__
        """ streamType(self, int) -> QMediaStreamsControl.StreamType """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AudioStream = 2
    DataStream = 4
    SubPictureStream = 3
    UnknownStream = 0
    VideoStream = 1


