# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QMediaRecorderControl(QMediaControl):
    """ QMediaRecorderControl(parent: QObject = None) """
    def actualLocationChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ actualLocationChanged(self, QUrl) [signal] """
        pass

    def applySettings(self): # real signature unknown; restored from __doc__
        """ applySettings(self) """
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

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def mutedChanged(self, bool): # real signature unknown; restored from __doc__
        """ mutedChanged(self, bool) [signal] """
        pass

    def outputLocation(self): # real signature unknown; restored from __doc__
        """ outputLocation(self) -> QUrl """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setMuted(self, bool): # real signature unknown; restored from __doc__
        """ setMuted(self, bool) """
        pass

    def setOutputLocation(self, QUrl): # real signature unknown; restored from __doc__
        """ setOutputLocation(self, QUrl) -> bool """
        return False

    def setState(self, QMediaRecorder_State): # real signature unknown; restored from __doc__
        """ setState(self, QMediaRecorder.State) """
        pass

    def setVolume(self, p_float): # real signature unknown; restored from __doc__
        """ setVolume(self, float) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QMediaRecorder.State """
        pass

    def stateChanged(self, QMediaRecorder_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QMediaRecorder.State) [signal] """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QMediaRecorder.Status """
        pass

    def statusChanged(self, QMediaRecorder_Status): # real signature unknown; restored from __doc__
        """ statusChanged(self, QMediaRecorder.Status) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> float """
        return 0.0

    def volumeChanged(self, p_float): # real signature unknown; restored from __doc__
        """ volumeChanged(self, float) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


