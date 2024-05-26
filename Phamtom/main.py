#OTNIAaJU1v5WUaPpP1eVczz1A87gNwvjJoXsflrN914
#AQEDAU3oYQ4BTCukAAABj4bz4ykAAAGPqwBnKU4AzHRFjtqlo7k_vus48MpkU0ByjNoW7vnH_GgvAwUkwh2JPfHvO246oUdvTokf5V5p3Fs4XLRZyIUS81oFXev3vjUaiYjl_q_wMPCJWdehobou9_sP
import requests
import time
import pandas as pd
import json
from io import StringIO

api_key = 'OTNIAaJU1v5WUaPpP1eVczz1A87gNwvjJoXsflrN914'
phantom_id = '3012120196923511'

headers = {
    'Content-Type': 'application/json',
    'x-phantombuster-key': api_key,
}
data = '{"id":"3012120196923511"}'

def insert_leads():
    url = 'https://api.phantombuster.com/api/v2/org-storage/leads/save-many'
    headers = {
        'X-Phantombuster-Key': 'OTNIAaJU1v5WUaPpP1eVczz1A87gNwvjJoXsflrN914',
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    data = {
        "leads": [
            {
                "linkedinProfileUrl": "https://www.linkedin.com/in/johnghu/"
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())

def launch_phantom():
    url = 'https://api.phantombuster.com/api/v2/agents/launch'
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print('Phantom launched successfully:', response.json()['containerId'])
        return response.json()['containerId']
    else:
        print('Error launching Phantom:', response.text)
        return None

def fetch_and_save_csv(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        csv_data = response.text

        data = pd.read_csv(StringIO(csv_data))
        
        data.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the CSV data: {e}")


url = 'https://phantombuster.s3.amazonaws.com/nq0csDlO940/rb5P49DzKCq9nLoTMhpX6Q/result.csv'
output_file = 'dev.csv'


leads_id = insert_leads()
execution_id = launch_phantom()

if execution_id:
    print("Waiting for the Phantom to complete...")
    #time.sleep(60)
    csv_data = fetch_and_save_csv(url, output_file)
    if csv_data is not None:
        print(csv_data)
        
'''
csv_data = fetch_and_save_csv(url, output_file)
if csv_data is not None:
    print(csv_data)
'''
