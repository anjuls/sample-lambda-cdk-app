#!/usr/bin/env python3

from aws_cdk import core

from sample_app.sample_app_stack import SampleAppStack


app = core.App()
SampleAppStack(app, "sample-app", env={'region': 'ap-south-1'})

app.synth()
