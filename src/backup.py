import os.path
from shutil import copyfile, copytree

import fileutils as fileu
import msgfunc as prnt

def backup_file(config, back_file, destination):
    if(os.path.exists(config[back_file])):
        prnt.prnt( '-s', 'Located your '+config[back_file]+' file!')
        try:
            if os.path.isdir(config[back_file]):
                copytree(config[back_file], destination)
            elif os.path.isfile(config[back_file]):
                copyfile(config[back_file], destination)
            else:
                raise Exception('TypeError: not a directory nor a file')
            prnt.prnt( '-s', 'Backed it up successfully!')
            return True
        except Exception as e:
            print(e)
            prnt.prnt( '-f', 'Failed to back it up!')
            return False
    else:
        prnt.prnt( '-f', 'Could not locate '+config[back_file]+' file!')
        return False

def backup_config( backup_folder, configuration):
    prnt.prnt( '-n', 'Backing up your files.')

    if( fileu.locate_folder(backup_folder) ):
        prnt.prnt( '-s', 'Located the backup folder.')

        for key, value in configuration.items():
            if(backup_file(configuration, key, backup_folder+ '/' +key)):
                prnt.prnt( '-s', 'Success!')
            else:
                prnt.prnt( '-f', 'Failed!')


    else:
       prnt.prnt( '-f', 'Failed to locate the backup folder.')
       exit(9)
