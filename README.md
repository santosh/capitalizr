
**capitalizr** - It's a utility that lets you change the case *(lowercase to
uppercase the letter of the words)* words in a file, leaving the words which
have 3 or less letters. The file looks pretty if it has all words in
capitalcase in it.

##why not sed?##
 * Because capitalizr is easy to use
 * sed doesn't takes input from stdin, it just works on piping.

##How to Install:##
The one and only requirement is Python, if you are on any variant of UNIX 
(e.g. Linux, \*BSD, Mac etc) then you have a good luck, else [download][4] it.
The simplest installation (for UNIX) is [download][3]/clone the archive, extract
it `cd` to it and run the setup:

    $ python setup.py install

Refer to [INSTALL][1] file for more instruction related to installation.

##Usages##
After following the instructions in [INSTALL][1] file, you should be able
to type `capitalizr` in terminal. Type capitalizr followed by the filename
and the output will be on the screen:

    $ capitalizr inputfile.txt


Pipe input to it

    $ cat inputfile.txt | capitalizr -

Input from **stdin**

    $ capitalizr
    the quick brown fox jumps over the lazy dog
    ^D
    the Quick Brown fox Jumps Over the Lazy dog

You can write the output into file by passing `-o` followed by output filename

    $ capitalizr inputfile.txt -o outputfile.txt

And the output will be on a file named outputfile.txt


##Bugs##
Bugs and suggestions should be reported at: https://github.com/santosh/capitalizr/issues

##To do##
These might seem silly ;) Here are implementation I want, priority wise:

 * Android App
 * Implement GUI
 * Put it in repository list of Ubuntu, Fedora etc.
 * Deployment with Debian package and Windows installer.
 * ~~Manual page (And the installation of it)~~ ✔

See also the `sandbox` branch of the repository.

##Contributors##
Feel free to contribute, just fork, clone, do your changes, push and send me
a pull request.

Here are the contributors:

<!-- only add yourself if you think you really contributed :) -->

 * [santosh][2]

  [1]: https://github.com/santosh/capitalizr/blob/master/INSTALL.md
  [2]: https://github.com/santosh
  [3]: https://github.com/santosh/capitalizr/archive/master.zip
  [4]: http://www.python.org/download/
