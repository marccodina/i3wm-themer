import json

import replace_line as rl
import msgfunc as prnt
import fileutils as fileu

fields = [
    "background",
    "foreground",
    "disabled",
    "primary",
    "warning",
    "alert",
    "modules-left",
    "modules-center",
    "modules-right",
]

def replace_polybar( configuration, json_file):
    prnt.prnt( '-n', 'Replacing your Polybar configuration file')

    if( fileu.locate_file( configuration['polybar-config'])):
        prnt.prnt( '-s', 'Located your polybar configuration file')
        if 'polybar' in json_file:
            polybar = json_file['polybar']
            prnt.prnt( '-s', 'Found you polybar info in the JSON file')
            for field in fields:
                rl.replace_line( configuration['polybar-config'], '' + field + ' =', '' + field + ' = '+polybar[field])
        else:
            prnt.prnt( '-f', 'Failed to locate polybar info in the JSON file')
    else:
        prnt.prnt( '-f', 'Failed to locate your polybar configuration file')
