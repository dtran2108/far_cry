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