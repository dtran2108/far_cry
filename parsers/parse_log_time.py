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


def update_full_time(original_full_time, update_time):
    """
    return a datetime object which is in an update form 
    of the original time
    for example:
        orgiginal: 2019-03-12 12:37:24-05:00
        time need to update: 57:24
        >>> update_full_time(2019-03-12 12:37:24-05:00, 57:24)
        2019-03-12 12:57:24-05:00

    @param
    original_full_time: a root datetime object
    update_time: a string which has minute and second need
                 to be updated
    """
    update_minute = int(update_time.split(':')[0])
    update_second = int(update_time.split(':')[1])
    root_hour = original_full_time.hour
    if update_minute == 0:
        return original_full_time.replace(hour=root_hour+1, minute=update_minute, second=update_second)
    else:
        return original_full_time.replace(minute=update_minute, second=update_second)


def parse_game_session_start_and_end_time(log_data, game_map, log_start_time):
    """
    returns the approximate start and end time of the game session

    @param
    log_data: the data read from a Far Cry server's log file
    game_map: the name of the map that was player, for instance mp_surf
    log_start_time: a datetime.datetime object representing the time the
                    Far Cry engine started to log at.
    """
    for line in log_data.split('\n'):
        if 'Level {} loaded'.format(game_map) in line:
            game_start_time = line.split()[0][1:-1]
        if 'Statistics' in line:
            game_end_time = line.split()[0][1:-1]
    full_game_start_time = update_full_time(log_start_time, game_start_time)
    full_game_end_time = update_full_time(log_start_time, game_end_time)
    return (full_game_start_time, full_game_end_time)