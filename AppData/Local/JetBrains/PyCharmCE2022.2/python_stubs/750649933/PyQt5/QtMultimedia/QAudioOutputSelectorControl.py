# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QAudioOutputSelectorControl(QMediaControl):
    """ QAudioOutputSelectorControl(parent: QObject = None) """
    def activeOutput(self): # real signature unknown; restored from __doc__
        """ activeOutput(self) -> str """
        return ""

    def activeOutputChanged(self, p_str): # real signature unknown; restored from __doc__
        """ activeOutputChanged(self, str) [signal] """
        pass

    def availableOutputs(self): # real signature unknown; restored from __doc__
        """ availableOutputs(self) -> List[str] """
        return []

    def availableOutputsChanged(self): # real signature unknown; restored from __doc__
        """ availableOutputsChanged(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultOutput(self): # real signature unknown; restored from __doc__
        """ defaultOutput(self) -> str """
        return ""

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def outputDescription(self, p_str): # real signature unknown; restored from __doc__
        """ outputDescription(self, str) -> str """
        return ""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActiveOutput(self, p_str): # real signature unknown; restored from __doc__
        """ setActiveOutput(self, str) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


