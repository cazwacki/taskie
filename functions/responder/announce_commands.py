# Python 3.10.12
# One-time -- announce your slash commands to Discord

import requests
import os

app_id = os.environ.get('APP_ID')
bot_token = os.environ.get('BOT_TOKEN')

url = f'https://discord.com/api/v10/applications/{app_id}/commands'

response = requests.put(url, headers={
    'Authorization': f'Bot {bot_token}'
}, json=[
    {
        'name': 'taskie',
        'description': 'Prints the Taskie Management Site',
        'options': []
    }
])

print(response.json())