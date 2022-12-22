# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QRadioDataControl(QMediaControl):
    """ QRadioDataControl(parent: QObject = None) """
    def alternativeFrequenciesEnabledChanged(self, bool): # real signature unknown; restored from __doc__
        """ alternativeFrequenciesEnabledChanged(self, bool) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QRadioData_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QRadioData.Error
        error(self, QRadioData.Error) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def isAlternativeFrequenciesEnabled(self): # real signature unknown; restored from __doc__
        """ isAlternativeFrequenciesEnabled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def programType(self): # real signature unknown; restored from __doc__
        """ programType(self) -> QRadioData.ProgramType """
        pass

    def programTypeChanged(self, QRadioData_ProgramType): # real signature unknown; restored from __doc__
        """ programTypeChanged(self, QRadioData.ProgramType) [signal] """
        pass

    def programTypeName(self): # real signature unknown; restored from __doc__
        """ programTypeName(self) -> str """
        return ""

    def programTypeNameChanged(self, p_str): # real signature unknown; restored from __doc__
        """ programTypeNameChanged(self, str) [signal] """
        pass

    def radioText(self): # real signature unknown; restored from __doc__
        """ radioText(self) -> str """
        return ""

    def radioTextChanged(self, p_str): # real signature unknown; restored from __doc__
        """ radioTextChanged(self, str) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlternativeFrequenciesEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setAlternativeFrequenciesEnabled(self, bool) """
        pass

    def stationId(self): # real signature unknown; restored from __doc__
        """ stationId(self) -> str """
        return ""

    def stationIdChanged(self, p_str): # real signature unknown; restored from __doc__
        """ stationIdChanged(self, str) [signal] """
        pass

    def stationName(self): # real signature unknown; restored from __doc__
        """ stationName(self) -> str """
        return ""

    def stationNameChanged(self, p_str): # real signature unknown; restored from __doc__
        """ stationNameChanged(self, str) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


