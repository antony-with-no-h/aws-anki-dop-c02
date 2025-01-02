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
    Note(
        model=Basic,
        fields=[
            'List the <strong>three</strong> CodePipeline execution modes',
            'SUPERSEDED<br>QUEUED<br>PARALLEL',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'CodePipeline can deploy to which <strong>three</strong> services',
            'EC2 using CodeDeploy<br>Elastic Beanstalk<br>ECS',
        ]
    ),
    Note(
        model=CLOZE_MODEL,
        fields=[
            'Pipeline stages are {{c1:locked}} when using {{c1:SUPERSEDED}} and {{c1:QUEUED}} execution modes',
            '',
        ]
    ),
    Note(
        model=BasicTITA,
        fields=[
            'Trigger a pipeline from an S3 source using:',
            'EventBridge',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'CodePipeline can deploy to which <strong>three</strong> services',
            'EC2 using CodeDeploy<br>Elastic Beanstalk<br>ECS',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'In SUPERSEDED execution mode a more recent execution can overtake an older one, but only when?',
            'Between stages',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'The <strong>four</strong> types of conditional stages for CodePipeline:',
            'DeploymentWindow (cron)<br>Lambda<br>CloudwatchAlarm<br>Variable Check',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'Detail the behaviour of a Canary deployment configuration, Canary10Percent5Minutes',
            'Shifts 10% of traffic first, the remainder 5 minutes later',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'Detail the behaviour of a Linear deployment configuration, Linear10PercentEvery3Minutes',
            'Shift 10% of traffic every 3 minutes, until all traffic is shifted',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'List the three CodeDeploy strategies for a Blue/Green Deployment',
            'Canary<br>Linear<br>AllAtonce',
        ]
    ),
    Note(
        model=BasicTITA,
        fields=[
            'CodeDeply rolls back deployments by:',
            'Deploying a previous version as a new deployment',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            '<strong>Two</strong> lifecycle hooks common to ECS, EC2 and Lambda?',
            'BeforeAllowTraffic<br>AfterAllowTraffic',
        ]
    ),
    Note(
        model=BasicTITA,
        fields=[
            'Lifecycle hook only available to ECS and EC2/On-prem',
            'BeforeInstall',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'Usage of <strong>ECS<strong> BeforeInstall hook',
            'Use to run tasks before the replacement task set is created.',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'Usage of <strong>EC2/On-Premises<strong> BeforeInstall hook',
            'Preinstall tasks, e.g. decrypting files or backups',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'BeforeAllowTraffic hook for <strong>ECS</strong> usage?',
            'Run tasks after the 2nd target group is associated with the replacement task set, but before traffic is shifted to the replacement task set.<br><ul><li>The replacement task set (green) has been associated with one or more target groups (e.g. An ALB)</li><li>After association you can run validation tests or custom scripts</li></ul>',
        ]
    ),
    Note(
        model=BasicTITA,
        fields=[
            'AWS EC2/On-prem lifecycle hook used to <strong>run tasks before</strong> being registered with a load balancer?',
            'BeforeAllowTraffic',
        ]
    ),
    Note(
        model=CLOZE_MODEL,
        fields=[
            'AWS Lambda BeforeAllowTraffic - {{c1:Use to run tasks before traffic is shifted to the deployed Lambda function version}}',
            '',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'ECS lifecycle hook that runs after the 2nd target group services traffic to the replacement task set?',
            'AfterAllowTraffic',
        ]
    ),
    Note(
        model=BasicTITA,
        fields=[
            'AWS Lambda AfterAllowTraffic - Use to run tasks ...',
            'after all traffic is shifted',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'Which EC2/On-prem lifecycle hook to use after instances are registered with a load balancer?',
            'AfterAllowTraffic',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'The hooks section of the AppSpec file for ECS or Lambda specifies?',
            'Lambda validation functions run during lifecycle events',
        ]
    ),
    Note(
        model=Basic,
        fields=[
            'The hooks section of the AppSpec file for EC2/On-prem is?',
            'Mapping lifecycle event to one or more scripts',
        ]
    ),
]
