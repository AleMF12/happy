# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraImageCaptureControl(QMediaControl):
    """ QCameraImageCaptureControl(parent: QObject = None) """
    def cancelCapture(self): # real signature unknown; restored from __doc__
        """ cancelCapture(self) """
        pass

    def capture(self, p_str): # real signature unknown; restored from __doc__
        """ capture(self, str) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def driveMode(self): # real signature unknown; restored from __doc__
        """ driveMode(self) -> QCameraImageCapture.DriveMode """
        pass

    def error(self, p_int, p_int_1, p_str): # real signature unknown; restored from __doc__
        """ error(self, int, int, str) [signal] """
        pass

    def imageAvailable(self, p_int, QVideoFrame): # real signature unknown; restored from __doc__
        """ imageAvailable(self, int, QVideoFrame) [signal] """
        pass

    def imageCaptured(self, p_int, QImage): # real signature unknown; restored from __doc__
        """ imageCaptured(self, int, QImage) [signal] """
        pass

    def imageExposed(self, p_int): # real signature unknown; restored from __doc__
        """ imageExposed(self, int) [signal] """
        pass

    def imageMetadataAvailable(self, p_int, p_str, Any): # real signature unknown; restored from __doc__
        """ imageMetadataAvailable(self, int, str, Any) [signal] """
        pass

    def imageSaved(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ imageSaved(self, int, str) [signal] """
        pass

    def isReadyForCapture(self): # real signature unknown; restored from __doc__
        """ isReadyForCapture(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def readyForCaptureChanged(self, bool): # real signature unknown; restored from __doc__
        """ readyForCaptureChanged(self, bool) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDriveMode(self, QCameraImageCapture_DriveMode): # real signature unknown; restored from __doc__
        """ setDriveMode(self, QCameraImageCapture.DriveMode) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


