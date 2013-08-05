import yaml
from glob import glob
from os.path import pjoin
from librarian.card import Card
from librarian.library import Library


def pack(library, carddir):
    """Pack all ``.crd`` card files in the carddir into the given library."""
    lib = Library(Library)

    for cardpath in glob(pjoin(carddir, "*.crd")):
        # Open card file and load it with yaml
        with open(cardpath) as cardfile:
            carddict = yaml.safe_load(cardfile)
        # Load the card dict from file into a card object
        card = Card().load(carddict)
        # Save the card object to the library
        lib.save_card(card)
