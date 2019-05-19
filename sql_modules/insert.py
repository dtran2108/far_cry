import sqlite3


def insert_frags_to_sqlite(connection, match_id, frags):
    """
    insert new record to table match_frag

    @param:
    connection: a sqlite3 Connection object
    match_id; the identification of a match
    frags: a list of frags
    """
    cursor = connection.cursor()
    new_frags = []
    for frag in frags:
        elements = list(frag)
        elements.insert(0, match_id)
        new_frags.append(tuple(elements))
    for new_frag in new_frags:
        if len(new_frag) == 3:
            cursor.execute('INSERT INTO match_frag (match_id, frag_time, killer_name) VALUES (?, ?, ?)', new_frag)
        else:
            cursor.execute('INSERT INTO match_frag VALUES (?, ?, ?, ?, ?)', new_frag)


def insert_match_to_sqlite(file_pathname, start_time, end_time,
                           game_mode, map_name, frags):
    """
     inserts a new record into the table match

    @param
    file_pathname: the path and name of the Far Cry's SQLite database;
    start_time: a datetime.datetime object with time zone information
                corresponding to the start of the game session.
    end_time: a datetime.datetime object with time zone information
              corresponding to the end of the game session.
    game_mode: multiplayer mode of the game session:
    map_name: name of the map that was played.
    frags: a list of tuples of the following form:
    (frag_time, killer_name[, victim_name, weapon_code])
    """
    conn = sqlite3.connect(file_pathname)
    values = (start_time, end_time, game_mode, map_name)
    c = conn.cursor()
    c.execute('INSERT INTO match (start_time, end_time, game_mode, map_name) VALUES (?, ?, ?, ?)', values)
    match_id = c.lastrowid
    insert_frags_to_sqlite(conn, match_id, frags)
    conn.commit()
    conn.close()
    return match_id