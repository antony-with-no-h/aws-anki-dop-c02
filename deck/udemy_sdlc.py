from genanki import Note, CLOZE_MODEL
from .models import Basic, BasicTITA

notes = [
    Note(
        model=BasicTITA,
        fields=[
            '<strong>Two</strong> IAM User Permissions needed for Manual Approval in CodePipeline',
            'GetPipeline PutApprovalResult',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'One example use case for CodeBuild Service Role',
            'Fetch parameters from SSM parameter store<br>Upload to S3 bucket<br>Fetch secrets from Secrets Managers<br>Store logs in CloudWatch',
        ]
    ),
    Note(
        model=BasicTITA,
        fields=[
            'Name the CodeBuild instructions file which should be in the repository root',
            'buildspec.yml',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'Four top level blocks of the buildspec.yml file',
            'env<br>phases<br>artifacts<br>cache',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'List the <strong>three</strong> Lambda CodeDeploy strategies',
            'Linear<br>Canary<br>AllAtonce',
        ]
    ),
    Note(
        model=CLOZE_MODEL,
        fields=[
            'CodeDeploy requires {{c1::an ALB}} when performing {{c1::a Blue/Green deployment}} to ECS',
            '',
        ]
    ),
]
