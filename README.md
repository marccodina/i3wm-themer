<h1>i3wm-themer</h1>
<ul>
Personal collection of themes and scripts for <a href="https://www.i3wm.org">i3wm</a>.

![](workflow/workflow.gif?raw=true)
</ul>

<h3>Update [April 4, 2018]</h3>
<ul>
Due to the high amount of requests to update this repository, I took the time to *completely* rework
it from the ground up. The old script is gone, the old configs are long gone. There is a <a
href="src/i3wm-themer.py">new script</a> used to apply/modify the themes for i3wm, polybar and .Xresources, all the old themes have been
reworked and a few new added. The script now uses a <a href="src/config.yaml">configuration file</a> used to locate your configs
more accurately and the themes are now presented in a <a href="src/themes">JSON</a> format to make them easier to read/modify/add your own.
This time I decided to add a few <a href="src/defaults">default configuration files</a> for you to use, to avoid the "oh my dots are now 
messed up" complains. With all that said, I hope you enjoy the fully reworked repo, I put a lot of
effort to make it meet everyone's needs/likings.
</ul>

<h1>Why?</h1>
<ul>
<li>You like CLI tools too much</li>
<li>You like simple and minimalistic desktop themes</li>
<li>You always wanted to use i3wm but can't figure it out on your own</li>
<li>You want to change themes on the go</li>
<li><a href="https://www.i3wm.org">i3wm</a> is awesome</li>
<li>Satan > Jesus</li>
</ul>

<h1>What you will need</h1>
<ul>
<li>Python 3</li>
<li><a href="https://github.com/Airblader/i3">i3-gaps</a></li>
<li><a href="https://github.com/jaagr/polybar">Polybar</a></li>
<li><a href="https://github.com/DaveDavenport/rofi">Rofi</a></li>
<li><a href="https://fontawesome.com">Font-Awesome-5</a></li>
<li><a href="https://aur.archlinux.org/packages/nitrogen-git/">Nitrogen</a></li>
<li><a href="https://aur.archlinux.org/packages/nerd-fonts-complete/">nerd-fonts-complete</a></li>
<li><a href="https://github.com/adobe-fonts/source-code-pro">Adobe Source Code Pro font</a></li>
<li><a href="https://wiki.archlinux.org/index.php/Rxvt-unicode">rxvt-unicode</a></li>
<li><a href="https://archlinux.org/packages/extra/x86_64/alsa-utils">alsa-utils</a></li>
<li><a href="https://archlinux.org/packages/community/x86_64/mate-power-manager">mate-power-manager</a></li>
</ul>

<h2>Using the script</h2>
<ul>
Clone this repository and install the requirements for the script.

    git clone https://github.com/unix121/i3wm-themer
    cd i3wm-themer/
    sudo pip install -r requirements.txt

Install all the requirements from the 'What you will need' section.
Either manually or use one of the scripts created for some distros:

    # For Arch, ArchLabs or Manjaro Linux
    ./install_arch.sh

    # For Debian
    ./install_debian.sh

    # For Ubuntu
    ./install_ubuntu.sh

If you are not on one of the above, install them using your Package manager.

Make sure you have the requirements mentioned earlier installed.
Edit the <a href="src/config.yaml">config.yaml</a> file and add your full path of i3wm config, polybar config and .Xresources
files. In the end it should look something like this:

    i3-config: /home/[USER]/.i3/config
    polybar-config: /home/[USER]/.config/polybar/config
    xresources: /home/[USER]/.Xresources

Where `[USER]` is your `$USER`.

All further commands are to be executed from the /src directory.

Copy the script in the <a href="scripts/">scripts</a> folder to your polybar directory:

    cp -r ../scripts/* /home/$USER/.config/polybar/

Backup your files:

    mkdir ~/Backups
    python i3wm-themer.py --config config.yaml --backup /home/[USER]/Backups

This step will copy the files that you set in the `config.yaml` for safekeeping in case things go
wrong.

Install:

    python i3wm-themer.py --config config.yaml --load <theme_id>


<h2>Available Themes</h2>
<ul>
ice
</ul>

