# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraFocusControl(QMediaControl):
    """ QCameraFocusControl(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def customFocusPoint(self): # real signature unknown; restored from __doc__
        """ customFocusPoint(self) -> QPointF """
        pass

    def customFocusPointChanged(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ customFocusPointChanged(self, Union[QPointF, QPoint]) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def focusMode(self): # real signature unknown; restored from __doc__
        """ focusMode(self) -> QCameraFocus.FocusModes """
        pass

    def focusModeChanged(self, Union, QCameraFocus_FocusModes=None, QCameraFocus_FocusMode=None): # real signature unknown; restored from __doc__
        """ focusModeChanged(self, Union[QCameraFocus.FocusModes, QCameraFocus.FocusMode]) [signal] """
        pass

    def focusPointMode(self): # real signature unknown; restored from __doc__
        """ focusPointMode(self) -> QCameraFocus.FocusPointMode """
        pass

    def focusPointModeChanged(self, QCameraFocus_FocusPointMode): # real signature unknown; restored from __doc__
        """ focusPointModeChanged(self, QCameraFocus.FocusPointMode) [signal] """
        pass

    def focusZones(self): # real signature unknown; restored from __doc__
        """ focusZones(self) -> List[QCameraFocusZone] """
        return []

    def focusZonesChanged(self): # real signature unknown; restored from __doc__
        """ focusZonesChanged(self) [signal] """
        pass

    def isFocusModeSupported(self, Union, QCameraFocus_FocusModes=None, QCameraFocus_FocusMode=None): # real signature unknown; restored from __doc__
        """ isFocusModeSupported(self, Union[QCameraFocus.FocusModes, QCameraFocus.FocusMode]) -> bool """
        return False

    def isFocusPointModeSupported(self, QCameraFocus_FocusPointMode): # real signature unknown; restored from __doc__
        """ isFocusPointModeSupported(self, QCameraFocus.FocusPointMode) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCustomFocusPoint(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setCustomFocusPoint(self, Union[QPointF, QPoint]) """
        pass

    def setFocusMode(self, Union, QCameraFocus_FocusModes=None, QCameraFocus_FocusMode=None): # real signature unknown; restored from __doc__
        """ setFocusMode(self, Union[QCameraFocus.FocusModes, QCameraFocus.FocusMode]) """
        pass

    def setFocusPointMode(self, QCameraFocus_FocusPointMode): # real signature unknown; restored from __doc__
        """ setFocusPointMode(self, QCameraFocus.FocusPointMode) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


