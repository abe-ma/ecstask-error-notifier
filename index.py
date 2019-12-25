import os
import json
from urllib.parse import urljoin, urlencode
import urllib.request as urlrequest

def slack_notify(webhook, channel, username, text):
    postToSlackPayload = {
            'channel': channel,
            'username': username,
            'text': text
        }
    encode = urlencode({"payload": json.dumps(postToSlackPayload)})
    request = urlrequest.Request(webhook)
    response = urlrequest.build_opener(urlrequest.HTTPHandler()).open(request, encode.encode('utf-8')).read()
    print(response)
    return response.decode('utf-8')

def lambda_handler(event, context):
    WEBHOOK = os.environ['WEBHOOK']
    CHANNEL = os.environ['CHANNEL']

    taskExitCode = event['detail']['containers'][0]['exitCode']
    taskArn = event['detail']['containers'][0]['taskArn']

    if taskExitCode == 1:
        slack_notify(
            webhook=WEBHOOK,
            channel=CHANNEL,
            username='Fargate Task Error',
            text='>>>TaskArn: ' + taskArn
        )
