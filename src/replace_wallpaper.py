import json

import os.path
from shutil import copyfile

import replace_line as rl
import msgfunc as prnt
import fileutils as fileu


def replace_wallpaper( configuration, json_file):
    prnt.prnt( '-n', 'Replacing wallpaper')
    nitrogen_file = configuration['nitrogen'] + "/bg-saved.cfg"

    if(fileu.locate_file(nitrogen_file)):
        prnt.prnt( '-s', 'Located your nitrogen configuration file')
        if 'wallpaper' in json_file:
            wallpaper = json_file['wallpaper']
            wallpaper_file = configuration['nitrogen'] + "/" + wallpaper
            prnt.prnt( '-s', 'Found the wallpaper info in the JSON file')
            rl.replace_line(nitrogen_file, 'file', 'file= '+ wallpaper_file)
    else:
        prnt.prnt( '-f', 'Failed to locate your nitrogen configuration file')
