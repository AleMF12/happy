# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QVideoDeviceSelectorControl(QMediaControl):
    """ QVideoDeviceSelectorControl(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultDevice(self): # real signature unknown; restored from __doc__
        """ defaultDevice(self) -> int """
        return 0

    def deviceCount(self): # real signature unknown; restored from __doc__
        """ deviceCount(self) -> int """
        return 0

    def deviceDescription(self, p_int): # real signature unknown; restored from __doc__
        """ deviceDescription(self, int) -> str """
        return ""

    def deviceName(self, p_int): # real signature unknown; restored from __doc__
        """ deviceName(self, int) -> str """
        return ""

    def devicesChanged(self): # real signature unknown; restored from __doc__
        """ devicesChanged(self) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def selectedDevice(self): # real signature unknown; restored from __doc__
        """ selectedDevice(self) -> int """
        return 0

    def selectedDeviceChanged(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        selectedDeviceChanged(self, int) [signal]
        selectedDeviceChanged(self, str) [signal]
        """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setSelectedDevice(self, p_int): # real signature unknown; restored from __doc__
        """ setSelectedDevice(self, int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


