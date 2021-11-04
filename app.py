#!/usr/bin/env python3
import glob

from aws_cdk import core as cdk

app = cdk.App()
app.synth()

app_list = glob.glob("app_*.py")
USAGE="cdk -app \"<app specification>\" COMMAND"

print(f"Usage: {USAGE}")
print()
print(f"In case of synth command: ")
for app in app_list:
    print(f"\tcdk -a \"python3 {app}\" synth")
