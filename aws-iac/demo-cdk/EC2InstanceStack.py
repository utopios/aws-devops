from aws_cdk import Stack, aws_ec2
from constructs import Construct


class EC2InstanceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        # Création de notre infra
        self.createInstance()

    def createInstance(self):
        self.linux_instance = aws_ec2.Instance(self, "mon_instance",
                                               instance_type=aws_ec2.InstanceType('t2.micro')
                                               )
