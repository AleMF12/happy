# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QMediaPlayerControl(QMediaControl):
    """ QMediaPlayerControl(parent: QObject = None) """
    def audioAvailableChanged(self, bool): # real signature unknown; restored from __doc__
        """ audioAvailableChanged(self, bool) [signal] """
        pass

    def availablePlaybackRanges(self): # real signature unknown; restored from __doc__
        """ availablePlaybackRanges(self) -> QMediaTimeRange """
        return QMediaTimeRange

    def availablePlaybackRangesChanged(self, QMediaTimeRange): # real signature unknown; restored from __doc__
        """ availablePlaybackRangesChanged(self, QMediaTimeRange) [signal] """
        pass

    def bufferStatus(self): # real signature unknown; restored from __doc__
        """ bufferStatus(self) -> int """
        return 0

    def bufferStatusChanged(self, p_int): # real signature unknown; restored from __doc__
        """ bufferStatusChanged(self, int) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def durationChanged(self, p_int): # real signature unknown; restored from __doc__
        """ durationChanged(self, int) [signal] """
        pass

    def error(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ error(self, int, str) [signal] """
        pass

    def isAudioAvailable(self): # real signature unknown; restored from __doc__
        """ isAudioAvailable(self) -> bool """
        return False

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def isSeekable(self): # real signature unknown; restored from __doc__
        """ isSeekable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isVideoAvailable(self): # real signature unknown; restored from __doc__
        """ isVideoAvailable(self) -> bool """
        return False

    def media(self): # real signature unknown; restored from __doc__
        """ media(self) -> QMediaContent """
        return QMediaContent

    def mediaChanged(self, QMediaContent): # real signature unknown; restored from __doc__
        """ mediaChanged(self, QMediaContent) [signal] """
        pass

    def mediaStatus(self): # real signature unknown; restored from __doc__
        """ mediaStatus(self) -> QMediaPlayer.MediaStatus """
        pass

    def mediaStatusChanged(self, QMediaPlayer_MediaStatus): # real signature unknown; restored from __doc__
        """ mediaStatusChanged(self, QMediaPlayer.MediaStatus) [signal] """
        pass

    def mediaStream(self): # real signature unknown; restored from __doc__
        """ mediaStream(self) -> QIODevice """
        pass

    def mutedChanged(self, bool): # real signature unknown; restored from __doc__
        """ mutedChanged(self, bool) [signal] """
        pass

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def play(self): # real signature unknown; restored from __doc__
        """ play(self) """
        pass

    def playbackRate(self): # real signature unknown; restored from __doc__
        """ playbackRate(self) -> float """
        return 0.0

    def playbackRateChanged(self, p_float): # real signature unknown; restored from __doc__
        """ playbackRateChanged(self, float) [signal] """
        pass

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def positionChanged(self, p_int): # real signature unknown; restored from __doc__
        """ positionChanged(self, int) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def seekableChanged(self, bool): # real signature unknown; restored from __doc__
        """ seekableChanged(self, bool) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setMedia(self, QMediaContent, QIODevice): # real signature unknown; restored from __doc__
        """ setMedia(self, QMediaContent, QIODevice) """
        pass

    def setMuted(self, bool): # real signature unknown; restored from __doc__
        """ setMuted(self, bool) """
        pass

    def setPlaybackRate(self, p_float): # real signature unknown; restored from __doc__
        """ setPlaybackRate(self, float) """
        pass

    def setPosition(self, p_int): # real signature unknown; restored from __doc__
        """ setPosition(self, int) """
        pass

    def setVolume(self, p_int): # real signature unknown; restored from __doc__
        """ setVolume(self, int) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QMediaPlayer.State """
        pass

    def stateChanged(self, QMediaPlayer_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QMediaPlayer.State) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def videoAvailableChanged(self, bool): # real signature unknown; restored from __doc__
        """ videoAvailableChanged(self, bool) [signal] """
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> int """
        return 0

    def volumeChanged(self, p_int): # real signature unknown; restored from __doc__
        """ volumeChanged(self, int) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


