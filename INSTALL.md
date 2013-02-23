#Installation Instruction:#

##On UNIX##
All you need to do is to [download][3] this file and place it in one of your
bin directory. I would suggest to make `bin` directory in you home
directory for this.

Make sure that ~/bin is in your PATH variable of your system. I have
following in my PATH variable. If you are not sure then add this line
into your ~/.bashrc file:

    export PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/home/<user>/bin

where `<user>` should be your username.

Since version [1.01.00][1] you can simply download the archive and do:

    $ python setup.py install

##On Windows##
As like in Unix, this script needs to be in PATH of your PC. You can do
three things, first one is to drop this script in your windows directory.
The another one is to add the location of your script to the PATH of
your PC. The third one is to open a command prompt, cd to the script and
run `python capitalizr`.

You need to install [Python][1] for
Windows if you already didn't have. Then add Python's executable to
system's PATH variable.

  [1]: https://github.com/santosh/capitalizr/tree/v1.01.00
  [2]: http://www.python.org/download/
  [3]: https://github.com/santosh/capitalizr/archive/master.zip
