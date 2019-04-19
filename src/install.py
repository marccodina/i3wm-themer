import os.path
from shutil import copyfile

import fileutils as fileu
import msgfunc as prnt

def _install_file(new_file, path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    if(fileu.locate_file(new_file)):
        prnt.prnt( '-s', 'Located '+path+' file!')
        try:
            copyfile(new_file, path)
            prnt.prnt( '-s', 'Installed the new file successfully!')
            return True
        except:
            prnt.prnt( '-f', 'Failed to install the new file!')
            return False
    else:
        prnt.prnt( '-f', 'Could not locate '+path+' file!')
        return False


def install_defaults(temp_folder, configuration):
    prnt.prnt( '-n', 'Intalling the files from '+temp_folder+' file.')

    if(fileu.locate_folder(temp_folder)):
        prnt.prnt( '-n', 'Located the folder.')

        for config_key, template_path in configuration.items():
            if os.path.isdir(template_path):
                for file in os.listdir(template_path):
                    if(_install_file(temp_folder + os.path.basename(template_path) + '/' + file, configuration[config_key] + "/"+ file)):
                       prnt.prnt( '-s', 'Success!')
                    else:
                        prnt.prnt( '-f', 'Failed!')
            else:
                if(_install_file(temp_folder + os.path.basename(template_path), template_path)):
                   prnt.prnt( '-s', 'Success!')
                else:
                    prnt.prnt( '-f', 'Failed!')


        # Install default i3 file
        # if 'i3-config' in configuration:
        #     if(_install_file(temp_folder+'i3.template', configuration['i3-config'])):
        #        prnt.prnt( '-s', 'Success!')
        #     else:
        #         prnt.prnt( '-f', 'Failed!')

        # Install default polybar file
        # if 'polybar' in configuration:
        #     for file in ["config", "power.sh", "spotify.py"]:
        #         if(_install_file(temp_folder+'polybar/' + file, configuration['polybar'] + file)):
        #            prnt.prnt( '-s', 'Success!')
        #         else:
        #             prnt.prnt( '-f', 'Failed!')


        # Install default Xresources file
        # if 'xresources' in configuration:
        #     if(_install_file(temp_folder+'xresources.template', configuration['xresources'])):
        #         prnt.prnt( '-s', 'Success!')
        #     else:
        #         prnt.prnt( '-f', 'Failed!')

        # Install default nitrogen file
        # if 'nitrogen-config' in configuration:
        #     if(_install_file(temp_folder+'bg-saved.template', configuration['nitrogen-config'])):
        #         prnt.prnt( '-s', 'Success!')
        #     else:
        #         prnt.prnt( '-f', 'Failed!')
    else:
        prnt.prnt( '-f', 'Failed to locate the folder.')
        exit(9)
