# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraFeedbackControl(QMediaControl):
    """ QCameraFeedbackControl(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isEventFeedbackEnabled(self, QCameraFeedbackControl_EventType): # real signature unknown; restored from __doc__
        """ isEventFeedbackEnabled(self, QCameraFeedbackControl.EventType) -> bool """
        return False

    def isEventFeedbackLocked(self, QCameraFeedbackControl_EventType): # real signature unknown; restored from __doc__
        """ isEventFeedbackLocked(self, QCameraFeedbackControl.EventType) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resetEventFeedback(self, QCameraFeedbackControl_EventType): # real signature unknown; restored from __doc__
        """ resetEventFeedback(self, QCameraFeedbackControl.EventType) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEventFeedbackEnabled(self, QCameraFeedbackControl_EventType, bool): # real signature unknown; restored from __doc__
        """ setEventFeedbackEnabled(self, QCameraFeedbackControl.EventType, bool) -> bool """
        return False

    def setEventFeedbackSound(self, QCameraFeedbackControl_EventType, p_str): # real signature unknown; restored from __doc__
        """ setEventFeedbackSound(self, QCameraFeedbackControl.EventType, str) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AutoFocusFailed = 11
    AutoFocusInProgress = 9
    AutoFocusLocked = 10
    ImageCaptured = 3
    ImageError = 5
    ImageSaved = 4
    RecordingInProgress = 7
    RecordingStarted = 6
    RecordingStopped = 8
    ViewfinderStarted = 1
    ViewfinderStopped = 2


