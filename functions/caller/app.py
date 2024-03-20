# Python 3.10.12

import boto3
import botocore

def lambda_handler(event, context):
    taskie_id = event.get('taskie_id', None)
    message = event.get('message', None)
    destination_phone_number = event.get('destination_phone_number', None)

    if(None in [taskie_id, message, destination_phone_number]):
        print(f'lambda_handler: improperly formatted event input; taskie_id = {taskie_id}, message = {message}, destination_phone_number = {destination_phone_number}')
        return {
            'statusCode': 400,
            'body': 'inputs "taskie_id", "message", "destination_phone_number" required'
        }

    ssm_client = boto3.client('ssm')
    try:
        contact_flow_id = ssm_client.get_parameter(Name='CONTACT_FLOW_ID')['Parameter']['Value']
        instance_id = ssm_client.get_parameter(Name='INSTANCE_ID')['Parameter']['Value']
        source_phone_number = ssm_client.get_parameter(Name='SOURCE_PHONE_NUMBER')['Parameter']['Value']
    except botocore.exceptions.ClientError as error:
        print('lambda_handler: failed to retrieve parameters from ssm')
        return {
            'statusCode': 500,
            'body': f'{error.response["Error"]["Code"]}; failed to retrieve parameters from ssm'
        }

    if(None in [contact_flow_id, instance_id, source_phone_number]):
        print(f'lambda_handler: improper ssm parameters; contact_flow_id = {contact_flow_id}, instance_id = {instance_id}, source_phone_number = {source_phone_number}')
        return {
            'statusCode': 503,
            'body': 'parameters "CONTACT_FLOW_ID", "INSTANCE_ID", "SOURCE_PHONE_NUMBER" required'
        }

    connect_client = boto3.client('connect')
    try:
        response = connect_client.start_outbound_voice_contact(
            ContactFlowId=contact_flow_id,
            InstanceId=instance_id,
            SourcePhoneNumber=source_phone_number,
            DestinationPhoneNumber=destination_phone_number,
            Attributes={
                'message': f'Taskie here with the following message: {message}. Goodbye!'
            }
        )
    except botocore.exceptions.ClientError as error:
        print(f'{error.response["Error"]["Code"]}; failed to start outbound call')
        return {
            'statusCode': 500,
            'body': f'{error.response["Error"]["Code"]}; failed to start outbound call'
        }

    contact_id = response.get('ContactId', 'not provided')
    print(f'sent taskie {taskie_id} to {destination_phone_number}; contact id is {contact_id}')
    return {
        'statusCode': 200,
        'body': f'sent taskie {taskie_id} to {destination_phone_number}; contact id is {contact_id}'
    }