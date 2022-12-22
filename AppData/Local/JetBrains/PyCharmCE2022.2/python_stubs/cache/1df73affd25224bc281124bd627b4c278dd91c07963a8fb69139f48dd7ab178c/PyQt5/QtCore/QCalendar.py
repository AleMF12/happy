# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\#Ale\.conda\envs\GCS10004\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCalendar(__sip.simplewrapper):
    """
    QCalendar()
    QCalendar(QCalendar.System)
    QCalendar(str)
    QCalendar(QCalendar)
    """
    def availableCalendars(self): # real signature unknown; restored from __doc__
        """ availableCalendars() -> List[str] """
        return []

    def dateFromParts(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        dateFromParts(self, int, int, int) -> QDate
        dateFromParts(self, QCalendar.YearMonthDay) -> QDate
        """
        return QDate

    def dateTimeToString(self, p_str, Union, QDateTime=None, datetime_datetime=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dateTimeToString(self, str, Union[QDateTime, datetime.datetime], Union[QDate, datetime.date], Union[QTime, datetime.time], QLocale) -> str """
        pass

    def dayOfWeek(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ dayOfWeek(self, Union[QDate, datetime.date]) -> int """
        return 0

    def daysInMonth(self, p_int, year=None): # real signature unknown; restored from __doc__
        """ daysInMonth(self, int, year: int = QCalendar.Unspecified) -> int """
        return 0

    def daysInYear(self, p_int): # real signature unknown; restored from __doc__
        """ daysInYear(self, int) -> int """
        return 0

    def hasYearZero(self): # real signature unknown; restored from __doc__
        """ hasYearZero(self) -> bool """
        return False

    def isDateValid(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ isDateValid(self, int, int, int) -> bool """
        return False

    def isGregorian(self): # real signature unknown; restored from __doc__
        """ isGregorian(self) -> bool """
        return False

    def isLeapYear(self, p_int): # real signature unknown; restored from __doc__
        """ isLeapYear(self, int) -> bool """
        return False

    def isLunar(self): # real signature unknown; restored from __doc__
        """ isLunar(self) -> bool """
        return False

    def isLuniSolar(self): # real signature unknown; restored from __doc__
        """ isLuniSolar(self) -> bool """
        return False

    def isProleptic(self): # real signature unknown; restored from __doc__
        """ isProleptic(self) -> bool """
        return False

    def isSolar(self): # real signature unknown; restored from __doc__
        """ isSolar(self) -> bool """
        return False

    def maximumDaysInMonth(self): # real signature unknown; restored from __doc__
        """ maximumDaysInMonth(self) -> int """
        return 0

    def maximumMonthsInYear(self): # real signature unknown; restored from __doc__
        """ maximumMonthsInYear(self) -> int """
        return 0

    def minimumDaysInMonth(self): # real signature unknown; restored from __doc__
        """ minimumDaysInMonth(self) -> int """
        return 0

    def monthName(self, QLocale, p_int, year=None, format=None): # real signature unknown; restored from __doc__
        """ monthName(self, QLocale, int, year: int = QCalendar.Unspecified, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def monthsInYear(self, p_int): # real signature unknown; restored from __doc__
        """ monthsInYear(self, int) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def partsFromDate(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ partsFromDate(self, Union[QDate, datetime.date]) -> QCalendar.YearMonthDay """
        pass

    def standaloneMonthName(self, QLocale, p_int, year=None, format=None): # real signature unknown; restored from __doc__
        """ standaloneMonthName(self, QLocale, int, year: int = QCalendar.Unspecified, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def standaloneWeekDayName(self, QLocale, p_int, format=None): # real signature unknown; restored from __doc__
        """ standaloneWeekDayName(self, QLocale, int, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def weekDayName(self, QLocale, p_int, format=None): # real signature unknown; restored from __doc__
        """ weekDayName(self, QLocale, int, format: QLocale.FormatType = QLocale.LongFormat) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Unspecified = -2147483648


