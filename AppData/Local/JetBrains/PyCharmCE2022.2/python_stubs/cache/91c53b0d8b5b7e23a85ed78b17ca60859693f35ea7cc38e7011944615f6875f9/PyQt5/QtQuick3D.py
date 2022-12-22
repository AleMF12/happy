# encoding: utf-8
# module PyQt5.QtQuick3D
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtQuick3D.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


# no functions
# classes

class QQuick3D(__sip.simplewrapper):
    """
    QQuick3D()
    QQuick3D(QQuick3D)
    """
    def idealSurfaceFormat(self, samples=-1): # real signature unknown; restored from __doc__
        """ idealSurfaceFormat(samples: int = -1) -> QSurfaceFormat """
        pass

    def __init__(self, QQuick3D=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQuick3DObject(__PyQt5_QtCore.QObject, __PyQt5_QtQml.QQmlParserStatus):
    # no doc
    def parentItem(self): # real signature unknown; restored from __doc__
        """ parentItem(self) -> QQuick3DObject """
        return QQuick3DObject

    def setParentItem(self, QQuick3DObject): # real signature unknown; restored from __doc__
        """ setParentItem(self, QQuick3DObject) """
        pass

    def setState(self, p_str): # real signature unknown; restored from __doc__
        """ setState(self, str) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> str """
        return ""

    def stateChanged(self): # real signature unknown; restored from __doc__
        """ stateChanged(self) [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QQuick3DGeometry(QQuick3DObject):
    """ QQuick3DGeometry(parent: QQuick3DObject = None) """
    def addAttribute(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAttribute(self, QQuick3DGeometry.Attribute.Semantic, int, QQuick3DGeometry.Attribute.ComponentType)
        addAttribute(self, QQuick3DGeometry.Attribute)
        """
        pass

    def attribute(self, p_int): # real signature unknown; restored from __doc__
        """ attribute(self, int) -> QQuick3DGeometry.Attribute """
        pass

    def attributeCount(self): # real signature unknown; restored from __doc__
        """ attributeCount(self) -> int """
        return 0

    def boundsMax(self): # real signature unknown; restored from __doc__
        """ boundsMax(self) -> QVector3D """
        pass

    def boundsMin(self): # real signature unknown; restored from __doc__
        """ boundsMin(self) -> QVector3D """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def classBegin(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def componentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def indexBuffer(self): # real signature unknown; restored from __doc__
        """ indexBuffer(self) -> QByteArray """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def nameChanged(self): # real signature unknown; restored from __doc__
        """ nameChanged(self) [signal] """
        pass

    def primitiveType(self): # real signature unknown; restored from __doc__
        """ primitiveType(self) -> QQuick3DGeometry.PrimitiveType """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBounds(self, QVector3D, QVector3D_1): # real signature unknown; restored from __doc__
        """ setBounds(self, QVector3D, QVector3D) """
        pass

    def setIndexData(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setIndexData(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def setPrimitiveType(self, QQuick3DGeometry_PrimitiveType): # real signature unknown; restored from __doc__
        """ setPrimitiveType(self, QQuick3DGeometry.PrimitiveType) """
        pass

    def setStride(self, p_int): # real signature unknown; restored from __doc__
        """ setStride(self, int) """
        pass

    def setVertexData(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setVertexData(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def stride(self): # real signature unknown; restored from __doc__
        """ stride(self) -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def vertexBuffer(self): # real signature unknown; restored from __doc__
        """ vertexBuffer(self) -> QByteArray """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass



# variables with complex values



