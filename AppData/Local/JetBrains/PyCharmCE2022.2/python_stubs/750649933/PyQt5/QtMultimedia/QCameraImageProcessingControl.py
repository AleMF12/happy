# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraImageProcessingControl(QMediaControl):
    """ QCameraImageProcessingControl(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isParameterSupported(self, QCameraImageProcessingControl_ProcessingParameter): # real signature unknown; restored from __doc__
        """ isParameterSupported(self, QCameraImageProcessingControl.ProcessingParameter) -> bool """
        return False

    def isParameterValueSupported(self, QCameraImageProcessingControl_ProcessingParameter, Any): # real signature unknown; restored from __doc__
        """ isParameterValueSupported(self, QCameraImageProcessingControl.ProcessingParameter, Any) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def parameter(self, QCameraImageProcessingControl_ProcessingParameter): # real signature unknown; restored from __doc__
        """ parameter(self, QCameraImageProcessingControl.ProcessingParameter) -> Any """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setParameter(self, QCameraImageProcessingControl_ProcessingParameter, Any): # real signature unknown; restored from __doc__
        """ setParameter(self, QCameraImageProcessingControl.ProcessingParameter, Any) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Brightness = 4
    BrightnessAdjustment = 9
    ColorFilter = 12
    ColorTemperature = 1
    Contrast = 2
    ContrastAdjustment = 7
    Denoising = 6
    DenoisingAdjustment = 11
    ExtendedParameter = 1000
    Saturation = 3
    SaturationAdjustment = 8
    Sharpening = 5
    SharpeningAdjustment = 10
    WhiteBalancePreset = 0


