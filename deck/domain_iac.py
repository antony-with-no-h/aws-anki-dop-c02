# Domain 2: Configuration Management and Infrastructure as Code
from genanki import Note, CLOZE_MODEL
from .models import Basic, BasicTITA

notes = [
    Note(
        model=Basic,
        fields=[
            'Summary of AWS CloudFormation?',
            'Use <strong>templates</strong> to declare resources (any AWS service)<br>Deployment is known as a stack - a collection of AWS resources<br>Stacks can separate concerns (VPC Stack, Network Stack, App Stack)',
        ]
    ),
]
