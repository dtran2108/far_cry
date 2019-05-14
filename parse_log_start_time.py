#!/usr/bin/env python3
from datetime import datetime


def parse_log_start_time(log_data):
    """
    return a datetime object representing the time the Far Cry
    engine started to log at.

    @param
    log_data: the data read from a Far Cry server's log file
    """
    first_line = log_data.split('\n')[0]
    datetime_str = first_line.split('Log Started at')[1].strip()
    datetime_obj = datetime.strptime(datetime_str, '%A, %B %d, %Y %H:%M:%S')
    return datetime_obj
