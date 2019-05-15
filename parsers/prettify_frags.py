import json


def load_json_file(json_file):
    """
    read json file and return a dictionary

    @param
    json_file: a absolute or relative path to
               the json file
    """
    with open(json_file, 'rb') as f:
        json_str = f.read()
    data_store = json.loads(json_str)
    return data_store


def get_weapon_icon(weapon, icon_dict):
    """
    return the icon of the weapon

    @param
    weapon: code of the weapon
    icon_dict: dictionary which contains icon
    """
    for icon in icon_dict:
        if weapon in icon_dict[icon]:
            return icon


def prettify_single_frag(frag):
    """
    return a string of the following format:
        [frag_time] 😛 killer_name weapon_icon 😦 victim_name
    or, the simple following form, if the player committed suicide:
        [frag_time] 😦 victim_name ☠

    @param
    frag: a tuple of the following format:
          (frag_time, killer_name, victim_name, weapon)
    """
    icon_dict = load_json_file('icon.json')
    weapon = frag[-1]
    weapon_icon = get_weapon_icon(weapon, icon_dict)
    if len(frag) == 2:
        return '[%s] 😦 %s ☠' %(frag[0], frag[1])
    else:
        return '[%s] 😛 %s %s 😦 %s' %(frag[0], frag[1], weapon_icon, frag[2])


def prettify_frags(frags):
    """
    returns a list of strings

    @param
    frags: an array of tuples of frags parsed from a Far Cry server's log file
    """
    prettified_frags = []
    for frag in frags:
        prettified_frags.append(prettify_single_frag(frag))
    return prettified_frags
