# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QAudioInputSelectorControl(QMediaControl):
    """ QAudioInputSelectorControl(parent: QObject = None) """
    def activeInput(self): # real signature unknown; restored from __doc__
        """ activeInput(self) -> str """
        return ""

    def activeInputChanged(self, p_str): # real signature unknown; restored from __doc__
        """ activeInputChanged(self, str) [signal] """
        pass

    def availableInputs(self): # real signature unknown; restored from __doc__
        """ availableInputs(self) -> List[str] """
        return []

    def availableInputsChanged(self): # real signature unknown; restored from __doc__
        """ availableInputsChanged(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultInput(self): # real signature unknown; restored from __doc__
        """ defaultInput(self) -> str """
        return ""

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def inputDescription(self, p_str): # real signature unknown; restored from __doc__
        """ inputDescription(self, str) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActiveInput(self, p_str): # real signature unknown; restored from __doc__
        """ setActiveInput(self, str) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


