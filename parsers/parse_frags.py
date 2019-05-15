from .parse_log_time import parse_log_start_time


def get_frag_lines(log_data):
    """
    return a list contains lines of frag history

    @param
    log_data: the data read from a Far Cry server's log file
    """
    frag_line_list = []
    for line in log_data.split('\n'):
        if 'killed' in line:
            frag_line_list.append(line)
    return frag_line_list


def get_frag(frag_line, log_start_time):
    """
    return a tuple of the following form:
        (frag_time, killer_name, victim_name, weapon_code)
    or, the simple following form, if the player committed suicide:
        (frag_time, killer_name)

    @param
    frag_line: a single line of frag, for example,
               <47:26> <Lua> cyap killed papazark with SniperRifle

    log_start_time: a datetime.datetime object representing the time
                    the Far Cry engine started to log at
    """
    elements = frag_line.split()
    frag_time = elements[0][1:-1].split(':')
    start_hour = log_start_time.hour
    frag_minute = int(frag_time[0])
    frag_second = int(frag_time[1])
    if frag_minute == 0:
        full_frag_time = log_start_time.replace(hour=start_hour+1,
                            minute=frag_minute, second=frag_second)
    full_frag_time = log_start_time.replace(minute=frag_minute, second=frag_second)
    if 'itself' in elements:
        return (full_frag_time, elements[elements.index('<Lua>')+1:elements.index('killed')])
    else:
        return (full_frag_time, ' '.join(elements[elements.index('<Lua>')+1:elements.index('killed')]),
                ' '.join(elements[elements.index('killed')+1:elements.index('with')]), elements[-1])


def parse_frags(log_data):
    """
    return a list of frags

    @param
    log_data: the data read from a Far Cry server's log file
    """
    frag_lines = get_frag_lines(log_data)
    start_time = parse_log_start_time(log_data)
    frag_list = []
    for line in frag_lines:
        frag_list.append(get_frag(line, start_time))
    return frag_list