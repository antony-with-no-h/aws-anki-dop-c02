from genanki import Model

Basic = Model(
    1637254653,
    'Basic',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Front}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Back}}',
        },
    ]
)

# Type in the Answer
BasicTITA = Model(
    1545173770,
    'Basic (type in the answer)',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Front}}\n{{type:Back}}',
            'afmt': '{{Front}}<hr id=answer>{{type:Back}}',
        },
    ]
)
