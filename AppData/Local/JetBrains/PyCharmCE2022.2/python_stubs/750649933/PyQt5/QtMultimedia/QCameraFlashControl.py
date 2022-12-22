# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraFlashControl(QMediaControl):
    """ QCameraFlashControl(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def flashMode(self): # real signature unknown; restored from __doc__
        """ flashMode(self) -> QCameraExposure.FlashModes """
        pass

    def flashReady(self, bool): # real signature unknown; restored from __doc__
        """ flashReady(self, bool) [signal] """
        pass

    def isFlashModeSupported(self, Union, QCameraExposure_FlashModes=None, QCameraExposure_FlashMode=None): # real signature unknown; restored from __doc__
        """ isFlashModeSupported(self, Union[QCameraExposure.FlashModes, QCameraExposure.FlashMode]) -> bool """
        return False

    def isFlashReady(self): # real signature unknown; restored from __doc__
        """ isFlashReady(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFlashMode(self, Union, QCameraExposure_FlashModes=None, QCameraExposure_FlashMode=None): # real signature unknown; restored from __doc__
        """ setFlashMode(self, Union[QCameraExposure.FlashModes, QCameraExposure.FlashMode]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


