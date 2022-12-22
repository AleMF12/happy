# encoding: utf-8
# module PyQt5.QtQuick
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


from .QSGMaterialShader import QSGMaterialShader

class QSGMaterialRhiShader(QSGMaterialShader):
    """ QSGMaterialRhiShader() """
    def compile(self, *args, **kwargs): # real signature unknown
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QSGMaterialRhiShader.Flags """
        pass

    def fragmentShader(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def setFlag(self, Union, QSGMaterialRhiShader_Flags=None, QSGMaterialRhiShader_Flag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setFlag(self, Union[QSGMaterialRhiShader.Flags, QSGMaterialRhiShader.Flag], on: bool = True) """
        pass

    def setShaderSourceFile(self, *args, **kwargs): # real signature unknown
        pass

    def setShaderSourceFiles(self, *args, **kwargs): # real signature unknown
        pass

    def updateGraphicsPipelineState(self, QSGMaterialRhiShader_RenderState, QSGMaterialRhiShader_GraphicsPipelineState, QSGMaterial, QSGMaterial_1): # real signature unknown; restored from __doc__
        """ updateGraphicsPipelineState(self, QSGMaterialRhiShader.RenderState, QSGMaterialRhiShader.GraphicsPipelineState, QSGMaterial, QSGMaterial) -> bool """
        return False

    def updateSampledImage(self, QSGMaterialRhiShader_RenderState, p_int, QSGMaterial, QSGMaterial_1): # real signature unknown; restored from __doc__
        """ updateSampledImage(self, QSGMaterialRhiShader.RenderState, int, QSGMaterial, QSGMaterial) -> QSGTexture """
        return QSGTexture

    def updateUniformData(self, QSGMaterialRhiShader_RenderState, QSGMaterial, QSGMaterial_1): # real signature unknown; restored from __doc__
        """ updateUniformData(self, QSGMaterialRhiShader.RenderState, QSGMaterial, QSGMaterial) -> bool """
        return False

    def vertexShader(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    UpdatesGraphicsPipelineState = 1


