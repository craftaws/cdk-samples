from aws_cdk import core as cdk
# Sample Code to build lambda function with container image which is building
from aws_cdk import (
    aws_ecr,
    aws_ecr_assets,
    aws_lambda,
)

class LambdaContainerStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_lambda.DockerImageFunction(self, "load_data_lambda",
            code=aws_lambda.DockerImageCode.from_image_asset(
                directory="samples/Lambda",
            )
        )
