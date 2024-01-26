#!/usr/bin/env python3
import subprocess
import requests
import re
from time import sleep

command = 'arp -a'
response = subprocess.check_output(command , shell=True)


response = str(response).split('\\n?')

for line in response:
    ip_text = ''
    mac_text = ''
    vendor_text = ''
    try:
        ip = re.search(r'(\d{1,3}\.){3}\d{1,3}', line)
        ip_text = ip.group()
        ip_text = ip_text.replace('(', '')
        ip_text = ip_text.replace(')', '')
    except:
        pass
    
    try:
        mac = re.search(r'([0-9A-Fa-f]{1,2}[:-]){5}[0-9A-Fa-f]{1,2}', line)
        mac_text = mac.group()
        url = f'https://www.macvendorlookup.com/api/v2/{mac_text}'
        try:
           vendor = requests.get(url).json()
           vendor_text = vendor[0]['company']
        except:
            pass
    except:
        pass

    print(f'Record:\t{ip_text}\t{mac_text}\t{vendor_text}')

    sleep(2)
    
