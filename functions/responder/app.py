# Python 3.10.12

# docs
# https://discord.com/developers/docs/interactions/receiving-and-responding

import boto3
import botocore
import json

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

def valid_request(event, public_key):
    print('valid_request: invoked')

    signature = event['headers']['x-signature-ed25519']
    timestamp = event['headers']['x-signature-timestamp']

    verify_key = VerifyKey(bytes.fromhex(public_key))

    message = timestamp + event['body']

    try:
        verify_key.verify(message.encode(), signature=bytes.fromhex(signature))
        print('valid_request: request validated successfully')
        return True
    except BadSignatureError:
        print('valid_request: request has bad signature')
        return False

def handle_ping():
    print('handle_ping: invoked')
    return {
        'statusCode': 200,
        'body': json.dumps({
            'type': 1
        })
    }

def handle_application_command(body, site_host):
    print('handle_application_command: invoked')
    command = body['data']['name']
    match command:
        case 'taskie':
            print('handle_application_command: returning message')
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'type': 4,
                    'data': {
                        'content': f'Visit {site_host} to manage your taskies!',
                    }
                })
            }
        case _:
            print(f'handle_application_command: unsupported command "{command}" invoked')
            return {
                'statusCode': 400,
                'body': 'unsupported command'
            }

def handle_message_component(body):
    print('handle_message_component invoked')
    # TODO: delete eventbridge schedule for phone call, if applicable
    return {
        'statusCode': 400,
        'body': 'unsupported command'
    }

def lambda_handler(event, context):
    print('lambda_handler: invoked')
    print(event)
    ssm_client = boto3.client('ssm')
    try:
        public_key = ssm_client.get_parameter(Name='DISCORD_PUBLIC_KEY', WithDecryption=True)['Parameter']['Value']
        site_host = ssm_client.get_parameter(Name='SITE_HOST')['Parameter']['Value']
    except botocore.exceptions.ClientError as error:
        print(f'lambda_handler: ssm client error - {error.response["Error"]["Code"]}')
        return {
            'statusCode': 500,
            'body': f'{error.response["Error"]["Code"]}; failed to retrieve parameters'
        }

    if(not valid_request(event, public_key)):
        print(f'lambda_handler: invalid request signature')
        return {
            'statusCode': 401,
            'body': 'invalid request signature'
        }

    body = json.loads(event['body'])
    interaction_type = body['type']
    match interaction_type:
        case 1:
            return handle_ping()
        case 2:
            return handle_application_command(body, site_host)
        case 3:
            return handle_message_component(body)
        case _:
            print(f'lambda_handler: unsupported interaction; type {interaction_type}')
            return {
                'statusCode': 400,
                'body': 'unsupported interaction'
            }