#!/usr/bin/env python3
from datetime import datetime


def read_log_file(log_file_path):
    """
    return log data read from log file

    @param
    log_file_path: path to the log file
    """
    with open(log_file_path) as f:
        log_data = f.read()
    return log_data


def get_cvar(log_data):
    """
    return a dictionary with the key is the console
    variable and value is its value

    @param
    log_data: the data read from a Far Cry server's log file
    """
    cvar_list = []
    cvar_dict = {}
    for line in log_data.split('\n'):
        if 'cvar' in line:
            cvar_list.append(line[line.index('cvar: (') + 7:-1])
    for cvar in cvar_list:
        temp = cvar.split(',')
        cvar_dict[temp[0]] = temp[1]
    return cvar_dict


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


def parse_session_mode_and_map(log_data):
    """
    return a tuple (mode, map) where:
        - mode: indicates the multiplayer mode that was played
        - map: the name of the map that was player

    @param:
    log_data: the data read from a Far Cry server's log file
    """
    temp = ''
    for line in log_data.split('\n'):
        if "Loading level" in line:
            for word in line[8:]:
                if word != '-':
                    temp += word
            break
    temp = temp.split(',')
    game_map = temp[0][temp[0].index('/')+1:]
    game_mode = temp[1].split('mission ')[1]
    return (game_mode, game_map)


if __name__ == '__main__':
    start_time = parse_log_start_time(read_log_file('./logs/log06.txt'))
    parse_session_mode_and_map(read_log_file('./logs/log00.txt'))
