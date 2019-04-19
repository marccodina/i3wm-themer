import json

import replace_line as rl
import msgfunc as prnt
import fileutils as fileu

def replace_xresources( configuration, json_file):
    prnt.prnt( '-n', 'Replacing the colors in .Xresources')

    if( fileu.locate_file(configuration['.Xresources'])):
        prnt.prnt( '-s', 'Located your .Xresources file')
        if 'Xresources' in json_file:
            xresources = json_file['Xresources']
            prnt.prnt( '-s', 'Found the Xresources info in the JSON file')
            for key, value in xresources.items():
                rl.replace_line(configuration['.Xresources'], key+':', key+': '+value)
        else:
            prnt.prnt( '-f', 'Failed to locate the Xresources info in the JSON file')
    else:
        prnt.prnt( '-f', 'Failed to locate your .Xresources file')
