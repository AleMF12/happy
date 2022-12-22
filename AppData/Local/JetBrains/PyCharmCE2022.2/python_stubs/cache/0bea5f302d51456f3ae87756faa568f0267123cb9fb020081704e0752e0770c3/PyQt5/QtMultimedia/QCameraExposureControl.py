# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraExposureControl(QMediaControl):
    """ QCameraExposureControl(parent: QObject = None) """
    def actualValue(self, QCameraExposureControl_ExposureParameter): # real signature unknown; restored from __doc__
        """ actualValue(self, QCameraExposureControl.ExposureParameter) -> Any """
        pass

    def actualValueChanged(self, p_int): # real signature unknown; restored from __doc__
        """ actualValueChanged(self, int) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isParameterSupported(self, QCameraExposureControl_ExposureParameter): # real signature unknown; restored from __doc__
        """ isParameterSupported(self, QCameraExposureControl.ExposureParameter) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def parameterRangeChanged(self, p_int): # real signature unknown; restored from __doc__
        """ parameterRangeChanged(self, int) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestedValue(self, QCameraExposureControl_ExposureParameter): # real signature unknown; restored from __doc__
        """ requestedValue(self, QCameraExposureControl.ExposureParameter) -> Any """
        pass

    def requestedValueChanged(self, p_int): # real signature unknown; restored from __doc__
        """ requestedValueChanged(self, int) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setValue(self, QCameraExposureControl_ExposureParameter, Any): # real signature unknown; restored from __doc__
        """ setValue(self, QCameraExposureControl.ExposureParameter, Any) -> bool """
        return False

    def supportedParameterRange(self, QCameraExposureControl_ExposureParameter): # real signature unknown; restored from __doc__
        """ supportedParameterRange(self, QCameraExposureControl.ExposureParameter) -> Tuple[List[Any], bool] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Aperture = 1
    ExposureCompensation = 3
    ExposureMode = 8
    ExtendedExposureParameter = 1000
    FlashCompensation = 5
    FlashPower = 4
    ISO = 0
    MeteringMode = 9
    ShutterSpeed = 2
    SpotMeteringPoint = 7
    TorchPower = 6


