**capitalizr** - It's a utility that lets you change the case *(lowercase to
uppercase the letter of the words)* words in a file, leaving the words which
have 3 or less letters. The file looks pretty if it has all words in
capitalcase in it.

why not sed?
------------

- because capitalizr is easy to use, just damn simple
- sed doesn't takes input from stdin, it just works on piping.

Install
-------

The one and only requirement is Python, if you are on any variant of UNIX 
*(e.g. Linux, *BSD, Mac etc)* then you have a good luck, else `download <http://www.python.org/download/>`__ it.
The simplest installation (for UNIX) is `download <https://github.com/santosh/capitalizr/archive/master.zip>`__/clone the archive, extract
it ``cd`` to it and run the setup::

    $ python setup.py install

Refer to `INSTALL`_ file for more instruction related to installation.

Usages
------

After following the instructions in `INSTALL`_ file, you should be able
to type ``capitalizr`` in terminal. Type capitalizr followed by the filename
and the output will be on the screen::
    $ capitalizr inputfile.txt

Pipe input to it::

    $ cat inputfile.txt | capitalizr -

Input from **stdin**::

    $ capitalizr -
    the quick brown fox jumps over the lazy dog
    ^D
    the Quick Brown fox Jumps Over the Lazy dog

You can write the output into file by passing ``-o`` followed by output filename,
and the output will be on a file named outputfile.txt::

    $ capitalizr inputfile.txt -o outputfile.txt

Override the default length of words to be escaped. The default it 3::

    $ capitalizr -t 1 inputfile.txt

Bugs? Suggestions? Questions?
-----------------------------

Questions approaching in your mind? Found any bugs? Have any suggestions?
Don't hesitate to post it at: https://github.com/santosh/capitalizr/issues

To do
-----

These might seem silly ;) Here are implementation I want, priority wise:

- Android App
- Implement GUI
- Put it in repository list of Ubuntu, Fedora etc.
- Deployment with Debian package and Windows installer.
- ~~Manual page (And the installation of it)~~ ✔

See also the ``sandbox`` branch of the repository.

Contributors
------------

Feel free to contribute, just fork, clone, do your changes, push and send me
a pull request.

Here are the contributors:

- `santosh <https://github.com/santosh>`__

.. _`INSTALL`: https://github.com/santosh/capitalizr/blob/master/INSTALL.rst

.. image:: https://travis-ci.org/santosh/capitalizr.png
        :target: https://travis-ci.org/santosh/capitalizr
.. image:: https://img.shields.io/pypi/v/capitalizr.svg
        :target: https://crate.io/packages/capitalizr
.. image:: https://img.shields.io/pypi/dm/capitalizr.svg
        :target: https://crate.io/packages/capitalizr
