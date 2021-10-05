#!/usr/bin/env python3
import os
import glob

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

app = core.App()
app.synth()

app_list = glob.glob("app_*.py")
USAGE="cdk -app \"<app specification>\" COMMAND"

print(f"Usage: {USAGE}")
print()
print(f"In case of synth command: ")
for app in app_list:
    print(f"\tcdk -a \"python3 {app}\" synth")
