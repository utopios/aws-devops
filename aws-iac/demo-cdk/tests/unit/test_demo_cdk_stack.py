import aws_cdk as core
import aws_cdk.assertions as assertions

from demo_cdk.demo_cdk_stack import DemoCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in demo_cdk/demo_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DemoCdkStack(app, "demo-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
