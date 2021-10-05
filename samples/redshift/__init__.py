from aws_cdk import core as cdk
# For consistency with other languages, 
# `cdk` is the preferred import name for the CDK's core module.
from aws_cdk import (
    aws_ec2,
    aws_redshift,
)

VPC_CIDR="192.168.192.0/20"

class RedshiftStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        sample_vpc = aws_ec2.Vpc(self, "redshift-vpc", 
            cidr=VPC_CIDR,
            max_azs=2,
            subnet_configuration=[
                aws_ec2.SubnetConfiguration(
                    name= 'isolated',
                    subnet_type=aws_ec2.SubnetType.ISOLATED,
                    cidr_mask=24
                )
            ]
        )

        aws_redshift.Cluster(self, 'sample-redshift',
            master_user=aws_redshift.Login(master_username="admin_user"),
            vpc=sample_vpc,
            vpc_subnets=aws_ec2.SubnetSelection(subnet_type=aws_ec2.SubnetType.ISOLATED),
            removal_policy=cdk.RemovalPolicy.DESTROY,
            # AQUA is available on clusters with ra3.xlplus, ra3.4xlarge, and ra3.16xlarge node types.
            # https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-aqua.html
            node_type=aws_redshift.NodeType.RA3_4XLARGE,
            number_of_nodes=2,
        )
