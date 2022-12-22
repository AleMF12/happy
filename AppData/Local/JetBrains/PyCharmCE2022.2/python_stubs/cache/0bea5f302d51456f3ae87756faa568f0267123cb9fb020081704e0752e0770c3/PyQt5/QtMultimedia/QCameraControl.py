# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraControl(QMediaControl):
    """ QCameraControl(parent: QObject = None) """
    def canChangeProperty(self, QCameraControl_PropertyChangeType, QCamera_Status): # real signature unknown; restored from __doc__
        """ canChangeProperty(self, QCameraControl.PropertyChangeType, QCamera.Status) -> bool """
        return False

    def captureMode(self): # real signature unknown; restored from __doc__
        """ captureMode(self) -> QCamera.CaptureModes """
        pass

    def captureModeChanged(self, Union, QCamera_CaptureModes=None, QCamera_CaptureMode=None): # real signature unknown; restored from __doc__
        """ captureModeChanged(self, Union[QCamera.CaptureModes, QCamera.CaptureMode]) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ error(self, int, str) [signal] """
        pass

    def isCaptureModeSupported(self, Union, QCamera_CaptureModes=None, QCamera_CaptureMode=None): # real signature unknown; restored from __doc__
        """ isCaptureModeSupported(self, Union[QCamera.CaptureModes, QCamera.CaptureMode]) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCaptureMode(self, Union, QCamera_CaptureModes=None, QCamera_CaptureMode=None): # real signature unknown; restored from __doc__
        """ setCaptureMode(self, Union[QCamera.CaptureModes, QCamera.CaptureMode]) """
        pass

    def setState(self, QCamera_State): # real signature unknown; restored from __doc__
        """ setState(self, QCamera.State) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QCamera.State """
        pass

    def stateChanged(self, QCamera_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QCamera.State) [signal] """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QCamera.Status """
        pass

    def statusChanged(self, QCamera_Status): # real signature unknown; restored from __doc__
        """ statusChanged(self, QCamera.Status) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    CaptureMode = 1
    ImageEncodingSettings = 2
    VideoEncodingSettings = 3
    Viewfinder = 4
    ViewfinderSettings = 5


