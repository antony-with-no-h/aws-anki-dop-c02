from genanki import Deck, Package, Note 
from .models import SimpleCard

DECKID = 1347655101

def generate():
    deck = Deck(
        DECKID,
        'AWS DOP-C02'
    )

    notes = [
        Note(
            model=SimpleCard,
            fields=[
                'What is CloudWatch, and what are it\'s primary use cases?',
                'Performance Monitoring<br>Log Management<br>Alerting<br>Application Insights<br>Automated Actions'
            ]
        ),
        Note(
            model=SimpleCard,
            fields=[
                '<strong>Five</strong design principles of <strong>Operational Excellence</strong>',
                'Ops. as Code<br/>Frequent small reversible changes<br>Refine operations procedures frequently<br>Anticipate failure<br>Learn from all operational failures'
            ]
        ),
    ]

    for note in notes:
        deck.add_note(note)

    Package(deck).write_to_file('build/aws-dop-c02.apkg')
