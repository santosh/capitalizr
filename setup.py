#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import shutil

# Quit if not run as root/sudo
if os.getuid() != 0:
    sys.exit("can't proceed, sudo privileges needed")

# Definitions
installManto = '/usr/share/man/man1/'
installBinTo = '/usr/local/bin/'
capsLoc = '/usr/local/bin/capitalizr'
mansLoc = '/usr/share/man/man1/capitalizr.1.gz'

def install():
    shutil.copy2('doc/capitalizr.1.gz', installManto)
    shutil.copy2('capitalizr', installBinTo)

def update():
    os.remove(capsLoc)
    os.remove(mansLoc)
    install()


# Do stuffs
if os.path.isfile(capsLoc) or os.path.isfile(mansLoc):
    print("The files exists, getting ready to update.")
    update()
else:
    print("Running the initial setup...")
    install()
