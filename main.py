#!/usr/bin/env python3
from parsers.parse_frags import parse_frags
from base_modules import read_log_file
from parsers.parse_mode_and_map import parse_session_mode_and_map


if __name__ == '__main__':
    log_data = read_log_file('./logs/log00.txt')
    print(parse_frags(log_data))