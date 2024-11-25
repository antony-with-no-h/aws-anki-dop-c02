from genanki import Model

ID = 1637254653

SimpleCard = Model(
    ID,
    'What is this',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ]
)
