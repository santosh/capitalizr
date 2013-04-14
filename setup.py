#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, sys, shutil
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='capitalizr',
    version='1.02.00',
    author='Santosh Kumar',
    author_email='sntshkmr60@gmail.com',
    packages=['capitalizr'],
    scripts=['bin/capitalizr'],
    url='https://github.com/santosh/capitalizr',
    zip_safe=False,
    include_package_data=True,
    license=open('LICENSE').read(),
    description='capitalizr changes the case of first letter of any word (lowercase to uppercase)'
    )

if 'install' in sys.argv:
    man_path = '/usr/share/man/man1/'
    if os.path.exists(man_path):
        man_page = "doc/capitalizr.1.gz"
        shutil.copy2(man_page, man_path)
        os.chmod(man_path + 'capitalizr.1.gz', int('444', 8))
        print("see manual page: man capitalizr")
