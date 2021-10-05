#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from samples.aurora_mysql import AuroraMysqlStack


app = cdk.App()
AuroraMysqlStack(app, "AuroraMySQL")

app.synth()