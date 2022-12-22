# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QDate(__sip.simplewrapper):
    """
    QDate()
    QDate(int, int, int)
    QDate(int, int, int, QCalendar)
    QDate(QDate)
    """
    def addDays(self, p_int): # real signature unknown; restored from __doc__
        """ addDays(self, int) -> QDate """
        return QDate

    def addMonths(self, p_int, QCalendar=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addMonths(self, int) -> QDate
        addMonths(self, int, QCalendar) -> QDate
        """
        return QDate

    def addYears(self, p_int, QCalendar=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addYears(self, int) -> QDate
        addYears(self, int, QCalendar) -> QDate
        """
        return QDate

    def currentDate(self): # real signature unknown; restored from __doc__
        """ currentDate() -> QDate """
        return QDate

    def day(self, QCalendar=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        day(self) -> int
        day(self, QCalendar) -> int
        """
        return 0

    def dayOfWeek(self, QCalendar=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        dayOfWeek(self) -> int
        dayOfWeek(self, QCalendar) -> int
        """
        return 0

    def dayOfYear(self, QCalendar=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        dayOfYear(self) -> int
        dayOfYear(self, QCalendar) -> int
        """
        return 0

    def daysInMonth(self, QCalendar=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        daysInMonth(self) -> int
        daysInMonth(self, QCalendar) -> int
        """
        return 0

    def daysInYear(self, QCalendar=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        daysInYear(self) -> int
        daysInYear(self, QCalendar) -> int
        """
        return 0

    def daysTo(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ daysTo(self, Union[QDate, datetime.date]) -> int """
        return 0

    def endOfDay(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        endOfDay(self, spec: Qt.TimeSpec = Qt.LocalTime, offsetSeconds: int = 0) -> QDateTime
        endOfDay(self, QTimeZone) -> QDateTime
        """
        return QDateTime

    def fromJulianDay(self, p_int): # real signature unknown; restored from __doc__
        """ fromJulianDay(int) -> QDate """
        return QDate

    def fromString(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromString(str, format: Qt.DateFormat = Qt.TextDate) -> QDate
        fromString(str, str) -> QDate
        fromString(str, str, QCalendar) -> QDate
        """
        return QDate

    def getDate(self): # real signature unknown; restored from __doc__
        """ getDate(self) -> Tuple[int, int, int] """
        pass

    def isLeapYear(self, p_int): # real signature unknown; restored from __doc__
        """ isLeapYear(int) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self, p_int=None, p_int_1=None, p_int_2=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isValid(self) -> bool
        isValid(int, int, int) -> bool
        """
        return False

    def longDayName(self, p_int, type=None): # real signature unknown; restored from __doc__
        """ longDayName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def longMonthName(self, p_int, type=None): # real signature unknown; restored from __doc__
        """ longMonthName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def month(self, QCalendar=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        month(self) -> int
        month(self, QCalendar) -> int
        """
        return 0

    def setDate(self, p_int, p_int_1, p_int_2, QCalendar=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setDate(self, int, int, int) -> bool
        setDate(self, int, int, int, QCalendar) -> bool
        """
        return False

    def shortDayName(self, p_int, type=None): # real signature unknown; restored from __doc__
        """ shortDayName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def shortMonthName(self, p_int, type=None): # real signature unknown; restored from __doc__
        """ shortMonthName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def startOfDay(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        startOfDay(self, spec: Qt.TimeSpec = Qt.LocalTime, offsetSeconds: int = 0) -> QDateTime
        startOfDay(self, QTimeZone) -> QDateTime
        """
        return QDateTime

    def toJulianDay(self): # real signature unknown; restored from __doc__
        """ toJulianDay(self) -> int """
        return 0

    def toPyDate(self): # real signature unknown; restored from __doc__
        """ toPyDate(self) -> datetime.date """
        pass

    def toString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toString(self, format: Qt.DateFormat = Qt.TextDate) -> str
        toString(self, Qt.DateFormat, QCalendar) -> str
        toString(self, str) -> str
        toString(self, str, QCalendar) -> str
        """
        return ""

    def weekNumber(self): # real signature unknown; restored from __doc__
        """ weekNumber(self) -> Tuple[int, int] """
        pass

    def year(self, QCalendar=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        year(self) -> int
        year(self, QCalendar) -> int
        """
        return 0

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DateFormat = 0
    StandaloneFormat = 1


