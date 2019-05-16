import csv


def read_log_file(log_file_path):
    """
    return log data read from log file

    @param
    log_file_path: path-like object giving the pathname
                   (absolute or relative to the current
                   working directory) of the log file
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


def write_frag_csv_file(log_file_pathname, frags):
    """
    @param
    log_file_pathname: the pathname of the CSV file to store the frags in
    frags: an array of tuples of the frags
    """
    with open(log_file_pathname, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(frags)
