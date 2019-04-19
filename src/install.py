import os.path
from shutil import copyfile
import stat

import fileutils as fileu
import msgfunc as prnt

def _install_file(new_file, path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    if(fileu.locate_file(new_file)):
        prnt.prnt( '-s', 'Located '+path+' file!')
        try:
            copyfile(new_file, path)
            if path.endswith('sh') or path.endswith('py'):
                st = os.stat(path)
                os.chmod(path, st.st_mode | stat.S_IEXEC)
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

    if(os.path.isdir(temp_folder)):
        prnt.prnt( '-n', 'Located the folder.')

        for config_key, template_path in configuration.items():
            tmp_path = temp_folder + os.path.basename(template_path)
            if os.path.isdir(tmp_path):
                for file in os.listdir(tmp_path):
                    tmp_file = tmp_path + '/' + file
                    final_file = configuration[config_key] + "/"+ file
                    if(_install_file(tmp_file, final_file)):
                       prnt.prnt( '-s', 'Success!')
                    else:
                        prnt.prnt( '-f', 'Failed!')
            else:
                if(_install_file(tmp_path, template_path)):
                   prnt.prnt( '-s', 'Success!')
                else:
                    prnt.prnt( '-f', 'Failed!')
    else:
        prnt.prnt( '-f', 'Failed to locate the folder.')
        exit(9)
