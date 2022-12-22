# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraViewfinderSettingsControl(QMediaControl):
    """ QCameraViewfinderSettingsControl(parent: QObject = None) """
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

    def isViewfinderParameterSupported(self, QCameraViewfinderSettingsControl_ViewfinderParameter): # real signature unknown; restored from __doc__
        """ isViewfinderParameterSupported(self, QCameraViewfinderSettingsControl.ViewfinderParameter) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setViewfinderParameter(self, QCameraViewfinderSettingsControl_ViewfinderParameter, Any): # real signature unknown; restored from __doc__
        """ setViewfinderParameter(self, QCameraViewfinderSettingsControl.ViewfinderParameter, Any) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewfinderParameter(self, QCameraViewfinderSettingsControl_ViewfinderParameter): # real signature unknown; restored from __doc__
        """ viewfinderParameter(self, QCameraViewfinderSettingsControl.ViewfinderParameter) -> Any """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    MaximumFrameRate = 3
    MinimumFrameRate = 2
    PixelAspectRatio = 1
    PixelFormat = 4
    Resolution = 0
    UserParameter = 1000


