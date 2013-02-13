**capitalizr** - It's a utility that lets you change the case *(lowercase to
uppercase the letter of the words)* words in a file, leaving the words which
have 3 or less letters. The file looks pretty if it has all words in
capitalcase in it.

##Requirements:##
 * Unix/Linux
 * Python

You will probably have Python installed if you are using UNIX :)

##How to Install:##
Refer to [INSTALL][1] file for more instruction related to installation.


##How to Use:##
###Basic###
After following the instructions in [INSTALL][1] file, you should be able
to type `capitalizr` in terminal. Type capitalizr followed by the filename
and the output will be on the screen. E.g. `capitalizr inputfile.txt`

###Saving Output###
You can write the output into file by doing appending `> outputfile.txt`.
Like this: `capitalizr inputfile.txt > outputfile.txt`. And the output will
be on a file named outputfile.txt

###Piping###
capitalizr also supports UNIX piping. So you can do
`cat inputfile.txt | capitalizr -` and it will work.

##To do:##
These might seem silly ;) Here are implementation I want, priority wise:

 * Manual page (And the installation of it)
 * Put it in repository list of Ubuntu, Fedora etc.
 * Deployment with Debian package and Windows installer.
 * Implement GUI
 * Android App
 * Internationalization

See also the `sandbox` branch of the repository.

##Contributors:##

 * [santosh][2]

  [1]: https://github.com/santosh/capitalizr/blob/master/INSTALL.md
  [2]: https://github.com/santosh
