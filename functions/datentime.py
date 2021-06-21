from datetime import date, datetime

MODULE_NAME = "datetime"
MODULE_AUTHOR = "Tomas Caram <tcaramm@gmail.com>"
MODULE_VERSION = 0.1


def get_date():
    """
    @Label(get_date)
    @Description(Get today's date)
    @Parameters()
    @Color(#00ff00)
    @Return(string)
    """

    return date.today()

def get_date_day():
    """
    @Label(get_date_day)
    @Description(Get current day from today's date)
    @Parameters()
    @Color(#00ff00)
    @Return(string)
    """

    return date.today().day

def get_date_month():
    """
    @Label(get_date_month)
    @Description(Get current month from today's date)
    @Parameters()
    @Color(#00ff00)
    @Return(string)
    """

    return date.today().month

def get_date_year():
    """
    @Label(get_date_year)
    @Description(Get current year from today's date)
    @Parameters()
    @Color(#00ff00)
    @Return(string)
    """

    return date.today().year

def get_time_in_seconds():
    """
    @Label(get_time_in_seconds)
    @Description(Get current time in seconds)
    @Parameters()
    @Color(#00ff00)
    @Return(string)
    """

    return datetime.now().time().second


def get_time_in_minutes():
    """
    @Label(get_time_in_minutes)
    @Description(Get current time in minutes)
    @Parameters()
    @Color(#00ff00)
    @Return(string)
    """

    return datetime.now().time().minute


def get_time_in_hours():
    """
    @Label(get_time_in_hours)
    @Description(Get current time in hours)
    @Parameters()
    @Color(#00ff00)
    @Return(string)
    """

    return datetime.now().time().hour