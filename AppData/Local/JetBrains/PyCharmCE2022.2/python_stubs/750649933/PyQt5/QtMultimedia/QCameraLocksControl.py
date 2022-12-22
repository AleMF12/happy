# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraLocksControl(QMediaControl):
    """ QCameraLocksControl(parent: QObject = None) """
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

    def lockStatus(self, QCamera_LockType): # real signature unknown; restored from __doc__
        """ lockStatus(self, QCamera.LockType) -> QCamera.LockStatus """
        pass

    def lockStatusChanged(self, QCamera_LockType, QCamera_LockStatus, QCamera_LockChangeReason): # real signature unknown; restored from __doc__
        """ lockStatusChanged(self, QCamera.LockType, QCamera.LockStatus, QCamera.LockChangeReason) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def searchAndLock(self, Union, QCamera_LockTypes=None, QCamera_LockType=None): # real signature unknown; restored from __doc__
        """ searchAndLock(self, Union[QCamera.LockTypes, QCamera.LockType]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def supportedLocks(self): # real signature unknown; restored from __doc__
        """ supportedLocks(self) -> QCamera.LockTypes """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unlock(self, Union, QCamera_LockTypes=None, QCamera_LockType=None): # real signature unknown; restored from __doc__
        """ unlock(self, Union[QCamera.LockTypes, QCamera.LockType]) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


