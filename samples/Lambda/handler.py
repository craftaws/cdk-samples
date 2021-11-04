'Sample python handler for aws-lambda container runtime environment'
import sys

def handle(event, context):
    '''
    Entry point of aws-lambda runtime
    To perform this lambda function with aws-lambda emulator in local:
      docker run -p 9000:8080 [IMAGE]
      curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
    '''
    print(f"# Event: {event}")
    print(f"# Contect: {context}")
    return 'Hello from AWS Lambda using Python' + sys.version + '!'
