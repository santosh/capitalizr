#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import shutil

# Quit if not run as root/sudo
if os.getuid() != 0:
    sys.exit("can't proceed, sudo privileges needed")


# {{ Definition of variables and functions
installManto = '/usr/share/man/man1/'
installBinTo = '/usr/local/bin/'
capsLoc = '/usr/local/bin/capitalizr'
mansLoc = '/usr/share/man/man1/capitalizr.1.gz'


def install():
    shutil.copy2('doc/capitalizr.1.gz', installManto)
    shutil.copy2('capitalizr', installBinTo)


def uninstall():
    os.remove(capsLoc)
    os.remove(mansLoc)


def update():
    uninstall()
    install()

usage = """usage: setup.py [install | uninstall]

installer for capitalizr

arguments:
  install        installs capitalizr, updates if already installed
  uninstall      uninstalls capitalizr
""".rstrip('\n')
# }}

try:
    if sys.argv[1] == 'install':
        if os.path.isfile(capsLoc) or os.path.isfile(mansLoc):
            print("the files exists, updating..")
            update()
            print("done")
        else:
            print("running the initial setup...")
            install()
            print("installed; see 'man capitalizr' for more info")
    elif sys.argv[1] == 'uninstall':
        if os.path.isfile(capsLoc) or os.path.isfile(mansLoc):
            print("uninstalling..")
            uninstall()
            print("cleaned..")
        else:
            print("already uninstalled..")
    else:
        print(usage)
except IndexError:
    print(usage)
