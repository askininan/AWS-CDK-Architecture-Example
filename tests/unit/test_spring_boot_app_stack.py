import aws_cdk as core
import aws_cdk.assertions as assertions

from spring_boot_app.spring_boot_app_stack import SpringBootAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in spring_boot_app/spring_boot_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SpringBootAppStack(app, "spring-boot-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
