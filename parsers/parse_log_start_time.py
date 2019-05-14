from base_modules import get_cvar
from datetime import datetime


def add_timezone(timezone, datetime_str):
    """
    return a datetime string with timezone at the end

    @param
    timezone: the timezone
    datetime_str: the original string without timezone
    """
    if timezone[0] == '+' or timezone[0] == '-':
        datetime_str += ', %s' %timezone[0]
        datetime_str += '0%s00' %timezone[1]
    else:
        datetime_str += ', +'
        datetime_str += '0%s00' %timezone
    return datetime_str


def parse_log_start_time(log_data):
    """
    return a datetime object representing the time the Far Cry
    engine started to log at.

    @param
    log_data: the data read from a Far Cry server's log file
    """
    cvar_dict = get_cvar(log_data)
    timezone = cvar_dict['g_timezone']
    first_line = log_data.split('\n')[0]
    datetime_str = first_line.split('Log Started at')[1].strip()
    datetime_str = add_timezone(timezone, datetime_str)
    datetime_obj = datetime.strptime(datetime_str, '%A, %B %d, %Y %H:%M:%S, %z')
    return datetime_obj