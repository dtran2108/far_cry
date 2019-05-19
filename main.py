#!/usr/bin/env python3
from parsers.parse_frags import parse_frags
from base_modules import read_log_file, write_frag_csv_file
from parsers.parse_mode_and_map import parse_session_mode_and_map
from parsers.parse_log_time import parse_log_start_time, parse_game_session_start_and_end_time
from parsers.prettify_frags import load_json_file, prettify_frags
from sql_modules.insert import insert_match_to_sqlite


def main():
    log_data = read_log_file('./logs/log00.txt')
    mode_game, map_game = parse_session_mode_and_map(log_data)
    start_time = parse_log_start_time(log_data)
    game_start_time, game_end_time = parse_game_session_start_and_end_time(log_data, map_game, start_time)
    frags = parse_frags(log_data)
    insert_match_to_sqlite('./farcry.db', game_start_time, game_end_time, mode_game, map_game, frags)


if __name__ == '__main__':
    main()
