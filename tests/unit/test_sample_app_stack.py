import json
import pytest

from aws_cdk import core
from sample-lambda-cdk-app.sample_app_stack import SampleAppStack


def get_template():
    app = core.App()
    SampleAppStack(app, "sample-app")
    return json.dumps(app.synth().get_stack("sample-app").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
