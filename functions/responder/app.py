# Python 3.10.12

# docs
# https://discord.com/developers/docs/interactions/receiving-and-responding

import boto3
import botocore
import json

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

def valid_request(event, public_key):
    body = json.loads(event['body'])

    signature = event['headers']['x-signature-ed25519']
    timestamp = event['headers']['x-signature-timestamp']

    if public_key is None:
        return False
    verify_key = VerifyKey(bytes.fromhex(public_key))

    message = timestamp + json.dumps(body, separators=(',', ':'))

    try:
        verify_key.verify(message.encode(), signature=bytes.fromhex(signature))
        return True
    except BadSignatureError:
        return False

def handle_ping():
    return {
        'statusCode': 200,
        'body': json.dumps({
            'type': 1
        })
    }

def handle_application_command(body, site_host):
    command = body['name']
    print(f'{command} invoked')
    match command:
        case 'help':
            if site_host is None:
                return {
                    'statusCode': 503,
                    'body': 'site host not configured'
                }
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'type': 4,
                    'data': {
                        'content': site_host,
                    }
                })
            }
        case _:
            return {
                'statusCode': 400,
                'body': 'unsupported command'
            }

def handle_message_component(body):
    # TODO: delete eventbridge schedule for phone call, if applicable
    return {
        'statusCode': 400,
        'body': 'unsupported command'
    }

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm')
    try:
        public_key = ssm_client.get_parameter(Name='DISCORD_PUBLIC_KEY', WithDecryption=True)['Parameter']['Value']
        site_host = ssm_client.get_parameter(Name='SITE_HOST')['Parameter']['Value']
    except botocore.exceptions.ClientError as error:
        return {
            'statusCode': 500,
            'body': f'{error.response["Error"]["Code"]}; failed to retrieve parameters'
        }

    if(not valid_request(event, public_key)):
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
            return {
                'statusCode': 400,
                'body': 'unsupported interaction'
            }