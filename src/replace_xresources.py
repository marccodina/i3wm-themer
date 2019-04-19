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
            rl.replace_line(configuration['.Xresources'], '*background:', '*background: '+xresources['background'])
            rl.replace_line(configuration['.Xresources'], '*foreground:', '*foreground: '+xresources['foreground'])
            rl.replace_line(configuration['.Xresources'], '*cursorColor:', '*cursorColor: '+xresources['cursorcolor'])
            for i in range(15):
                rl.replace_line( configuration['.Xresources'], '*color'+str(i)+':', '*color'+str(i)+': '+xresources['color'+str(i)])
            rl.replace_line( configuration['.Xresources'], 'rofi.color-window:', 'rofi.color-window: '+xresources['rofi.color-window'])
            rl.replace_line( configuration['.Xresources'], 'rofi.color-normal:', 'rofi.color-normal: '+xresources['rofi.color-normal'])
            rl.replace_line( configuration['.Xresources'], 'rofi.color-active:', 'rofi.color-active: '+xresources['rofi.color-active'])
            rl.replace_line( configuration['.Xresources'], 'rofi.color-urgent:', 'rofi.color-urgent: '+xresources['rofi.color-urgent'])

        else:
            prnt.prnt( '-f', 'Failed to locate the Xresources info in the JSON file')
    else:
        prnt.prnt( '-f', 'Failed to locate your .Xresources file')
