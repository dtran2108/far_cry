#!/usr/bin/env python3
from parsers.parse_frags import parse_frags
from base_modules import read_log_file, write_frag_csv_file
from parsers.parse_mode_and_map import parse_session_mode_and_map
from parsers.parse_log_time import parse_log_start_time, parse_game_session_start_and_end_time
from parsers.prettify_frags import load_json_file, prettify_frags


def main():
    log_data = read_log_file('./logs/log00.txt')
    start_time = parse_log_start_time(log_data)
    icons = load_json_file('./icon.json')
    frags = parse_frags(log_data)
    game_map = parse_session_mode_and_map(log_data)[1]
    print(parse_game_session_start_and_end_time(log_data, game_map, start_time))
    write_frag_csv_file('./csv_files/log00.csv', frags)
    # print(prettify_frags(frags))


if __name__ == '__main__':
    main()
