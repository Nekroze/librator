from argparse import ArgumentParser
from os.path import splitext


def main(clargs=None):
    """The primary entry point, can pack or unpack a **Librarian** library."""
    parser = ArgumentParser(
        description="Handles Librarian card database packaging.")
    parser.add_argument("cards", type=str,
                        help="Directory of single .crd card files")
    parser.add_argument("library", type=str,
                        help="Library database file")
    parser.add_argument("-u", "--unpack", action="store_true",
                        help="Unpack existing library")
    args = parser.parse_args(clargs)


CARDTEMPLATE = """
name: card
code: 0
attributes:
- alive
abilities:
  open:
  - attack
info:
  art:
  - ""
"""


def cardmain(clargs=None):
    """Generate a blank card file."""
    parser = ArgumentParser(
        description="Create a black card file template.")
    parser.add_argument("cardfile", type=str,
                        help="Card filename")
    args = parser.parse_args(clargs)

    filename, _ = splitext(args.cardfile)
    filename += ".crd"

    with open(filename, "w") as cardfile:
        cardfile.write(CARDTEMPLATE.strip())
