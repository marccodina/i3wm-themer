import json

import replace_line as rl
import msgfunc as prnt
import fileutils as fileu

def replace_i3( configuration, json_file):
    prnt.prnt( '-n', 'Replacing the colors in your i3 configuration file')
    i3_file = configuration['i3'] + "/config"

    if( fileu.locate_file(i3_file)):
        prnt.prnt( '-s', 'Located your i3 configuration file')
        if 'i3' in json_file:
            i3wm = json_file['i3']
            prnt.prnt( '-s', 'Found the i3wm info in the JSON file')
            for key, value in i3wm.items():
                rl.replace_line(i3_file, key, key + " " + value)
    else:
        prnt.prnt( '-f', 'Failed to locate your i3 configuration file')
