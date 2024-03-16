# Python 3.10.12

import boto3
import botocore
import os

def lambda_handler(event, context):

    contact_flow_id = os.environ.get('CONTACT_FLOW_ID')
    instance_id = os.environ.get('INSTANCE_ID')
    source_phone_number = os.environ.get('SOURCE_PHONE_NUMBER')

    if(None in [contact_flow_id, instance_id, source_phone_number]):
        return {
            'statusCode': 503,
            'body': 'environment variables "CONTACT_FLOW_ID", "INSTANCE_ID", "SOURCE_PHONE_NUMBER required'
        }

    taskie_id = event.get('taskie_id', None)
    message = event.get('message', None)
    destination_phone_number = event.get('destination_phone_number', None)

    if(None in [taskie_id, message, destination_phone_number]):
        return {
            'statusCode': 400,
            'body': 'inputs "taskie_id", "message", "destination_phone_number" required'
        }

    client = boto3.client('connect')
    try:
        response = client.start_outbound_voice_contact(
            ContactFlowId=contact_flow_id,
            InstanceId=instance_id,
            SourcePhoneNumber=source_phone_number,
            DestinationPhoneNumber=destination_phone_number,
            Attributes={
                'message': f'Taskie here with the following message: {message}. Goodbye!'
            }
        )
    except botocore.exceptions.ClientError as error:
        return {
            'statusCode': 500,
            'body': error.response['Error']['Code']
        }

    contact_id = response.get('ContactId', 'not provided')
    return {
        'statusCode': 200,
        'body': f'sent taskie {taskie_id} to {destination_phone_number}; contact id is {contact_id}'
    }