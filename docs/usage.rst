========
Usage
========

libratorcard
------------

Librator provides two command line tools the first will create an empty card
file.::
  libratorcard mycard.crd

The filename of a ``.crd`` file doesn't really matter however the next utility
will name card files after their code.

librator
--------

The ``librator`` command line tool needs a directory for the card files and a
path for th library database.::
  librator ./cards allcards.lbr

This will pack all the .crd files into the card library call ``allcards.lbr``
ready for later use via **Librarian**.

The same process can be reversed and the cards in a library database can be
extracted to their own ``.crd`` files by providing the ``-u`` or ``--unpack``
switch at the command line like so.::
  librator -u ./cards allcards.lbr

In unpacking the ``librator`` command will work fine for partial
updates. However when packing a library only the cards in the specified card
directory will be packaged.
