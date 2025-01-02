from genanki import Deck, Package
from .models import Basic, BasicTITA

from . import skillbuilder
from . import domain_sdlc

DECKID = 1347655101

def generate():
    deck = Deck(
        DECKID,
        'AWS DOP-C02'
    )

    notes = []
    notes.extend(skillbuilder.notes)
    notes.extend(domain_sdlc.notes)

    for note in notes:
        deck.add_note(note)

    Package(deck).write_to_file('build/aws-dop-c02.apkg')
