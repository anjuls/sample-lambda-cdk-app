from aws_cdk import (
    core,
    aws_lambda as _lambda,
)


class SampleAppStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code = _lambda.Code.asset('lambda'),
            handler='hello.handler',
        )
