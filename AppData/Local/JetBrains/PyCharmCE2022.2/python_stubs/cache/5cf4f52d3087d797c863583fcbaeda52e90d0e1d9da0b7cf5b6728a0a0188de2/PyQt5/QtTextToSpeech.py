# encoding: utf-8
# module PyQt5.QtTextToSpeech
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtTextToSpeech.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QTextToSpeech(__PyQt5_QtCore.QObject):
    """
    QTextToSpeech(parent: QObject = None)
    QTextToSpeech(str, parent: QObject = None)
    """
    def availableEngines(self): # real signature unknown; restored from __doc__
        """ availableEngines() -> List[str] """
        return []

    def availableLocales(self): # real signature unknown; restored from __doc__
        """ availableLocales(self) -> List[QLocale] """
        return []

    def availableVoices(self): # real signature unknown; restored from __doc__
        """ availableVoices(self) -> List[QVoice] """
        return []

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

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        pass

    def localeChanged(self, QLocale): # real signature unknown; restored from __doc__
        """ localeChanged(self, QLocale) [signal] """
        pass

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def pitch(self): # real signature unknown; restored from __doc__
        """ pitch(self) -> float """
        return 0.0

    def pitchChanged(self, p_float): # real signature unknown; restored from __doc__
        """ pitchChanged(self, float) [signal] """
        pass

    def rate(self): # real signature unknown; restored from __doc__
        """ rate(self) -> float """
        return 0.0

    def rateChanged(self, p_float): # real signature unknown; restored from __doc__
        """ rateChanged(self, float) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def say(self, p_str): # real signature unknown; restored from __doc__
        """ say(self, str) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def setPitch(self, p_float): # real signature unknown; restored from __doc__
        """ setPitch(self, float) """
        pass

    def setRate(self, p_float): # real signature unknown; restored from __doc__
        """ setRate(self, float) """
        pass

    def setVoice(self, QVoice): # real signature unknown; restored from __doc__
        """ setVoice(self, QVoice) """
        pass

    def setVolume(self, p_float): # real signature unknown; restored from __doc__
        """ setVolume(self, float) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QTextToSpeech.State """
        pass

    def stateChanged(self, QTextToSpeech_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QTextToSpeech.State) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def voice(self): # real signature unknown; restored from __doc__
        """ voice(self) -> QVoice """
        return QVoice

    def voiceChanged(self, QVoice): # real signature unknown; restored from __doc__
        """ voiceChanged(self, QVoice) [signal] """
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> float """
        return 0.0

    def volumeChanged(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        volumeChanged(self, float) [signal]
        volumeChanged(self, int) [signal]
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    BackendError = 3
    Paused = 2
    Ready = 0
    Speaking = 1


class QVoice(__sip.simplewrapper):
    """
    QVoice()
    QVoice(QVoice)
    """
    def age(self): # real signature unknown; restored from __doc__
        """ age(self) -> QVoice.Age """
        pass

    def ageName(self, QVoice_Age): # real signature unknown; restored from __doc__
        """ ageName(QVoice.Age) -> str """
        return ""

    def gender(self): # real signature unknown; restored from __doc__
        """ gender(self) -> QVoice.Gender """
        pass

    def genderName(self, QVoice_Gender): # real signature unknown; restored from __doc__
        """ genderName(QVoice.Gender) -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QVoice=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Adult = 2
    Child = 0
    Female = 1
    Male = 0
    Other = 4
    Senior = 3
    Teenager = 1
    Unknown = 2
    __hash__ = None


# variables with complex values



