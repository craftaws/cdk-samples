#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from samples.redshift import RedshiftStack

app = cdk.App()
RedshiftStack(app, "SampleRedshift")

app.synth()