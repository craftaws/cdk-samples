from aws_cdk import core as cdk
# For consistency with other languages, 
# `cdk` is the preferred import name for the CDK's core module.
from aws_cdk import (
    aws_rds,
    aws_ec2,
)

VPC_CIDR="192.168.128.0/20"

class AuroraMysqlStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = aws_ec2.Vpc(self, "aurora-mysql-vpc", 
            cidr=VPC_CIDR,
            max_azs=2,
            subnet_configuration=[
                aws_ec2.SubnetConfiguration(
                    name= 'public',
                    subnet_type=aws_ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                aws_ec2.SubnetConfiguration(
                    name= 'isolated',
                    subnet_type=aws_ec2.SubnetType.ISOLATED,
                    cidr_mask=24
                )
            ]
        )

        db_subnet_group = aws_rds.SubnetGroup(self, 'db-subnet-group',
            description='db subnet group',
            vpc=vpc,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            vpc_subnets=aws_ec2.SubnetSelection(subnets=vpc.isolated_subnets)
        )

        db_security_group = aws_ec2.SecurityGroup(self, 'db-security-greoup',
            vpc=vpc
        )

        db_security_group.add_ingress_rule(
            peer=aws_ec2.Peer.ipv4(VPC_CIDR),
            connection=aws_ec2.Port(
                protocol=aws_ec2.Protocol.TCP,
                string_representation="to allow from the vpc internal",
                from_port=3306,
                to_port=3306
            )
        )

        db_param_group = aws_rds.ParameterGroup(self, 'aurora-mysql-param',
            engine=aws_rds.DatabaseClusterEngine.AURORA_MYSQL
        )
        db_param_group.add_parameter("performance_schema", "1")

        db_cluster= aws_rds.DatabaseCluster(self, 'sample-aurora-mysql',
            engine=aws_rds.DatabaseClusterEngine.aurora_mysql(version=aws_rds.AuroraMysqlEngineVersion.VER_2_07_1),
            instance_props=aws_rds.InstanceProps(
                vpc=vpc,
                instance_type=aws_ec2.InstanceType.of(instance_class=aws_ec2.InstanceClass.BURSTABLE3, instance_size=aws_ec2.InstanceSize.MEDIUM),
                security_groups=[db_security_group]
            ),
            instances=1,
            subnet_group=db_subnet_group,
            parameter_group=db_param_group,
            removal_policy=cdk.RemovalPolicy.DESTROY
        )
