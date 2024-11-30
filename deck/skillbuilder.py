from genanki import Note
from .models import Basic, BasicTITA

notes = [
    Note(
        model=BasicTITA,
        fields=[
            'Aurora maintains how many copies of a database?',
            '6',
        ]
    ),
    Note(
        model=BasicTITA,
        fields=[
            'Name the serverless analytics service that uses SQL',
            'Athena',
        ]
    ),
    Note(
        model=BasicTITA,
        fields=[
            'Athena tightly integrates what SQL engine into the AWS ecosystem?',
            'Presto',
        ]
    ),
]
