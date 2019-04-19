import json

import replace_line as rl
import msgfunc as prnt
import fileutils as fileu


def replace_polybar( configuration, json_file):
    prnt.prnt( '-n', 'Replacing your Polybar configuration file')
    polybar_file = configuration["polybar"] + "/config"

    if(fileu.locate_file(polybar_file)):
        prnt.prnt( '-s', 'Located your polybar configuration file')
        if 'polybar' in json_file:
            polybar = json_file['polybar']
            prnt.prnt( '-s', 'Found you polybar info in the JSON file')
            for key, value in polybar.items():
                rl.replace_line(polybar_file, '' + key + ' =', '' + key + ' = '+value)
        else:
            prnt.prnt( '-f', 'Failed to locate polybar info in the JSON file')
    else:
        prnt.prnt( '-f', 'Failed to locate your polybar configuration file')
