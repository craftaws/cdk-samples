#!/usr/bin/env python3
from aws_cdk import core as cdk
from samples.Lambda import LambdaContainerStack

app = cdk.App()
LambdaContainerStack(app, "LambdaContainerStack")

app.synth()