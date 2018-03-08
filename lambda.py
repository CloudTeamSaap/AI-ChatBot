import json
def lambda_handler(event, context):
    if event['messages'][0]['unstructured']['text'] == 'hi':
        return 'Hello! how can i help you?'
    if event['messages'][0]['unstructured']['text'] == 'hello':
        return 'Hi! what can i do for you?'
    return 'Type in a message so that I know how to help you!'