import requests
import json
import subprocess
import re

def get_ssid():
    try:
        output = subprocess.check_output(["iwgetid", "-r"]).decode('utf-8').strip()
        return output
    except:
        return "SSID not found"

def get_private_ip():
    try:
        output = subprocess.check_output(["hostname", "-I"]).decode('utf-8').strip()
        return output.split()[0]  # Get IP
    except:
        return "IP not found"

def send_discord_webhook(webhook_url, message):
    headers = {
        'Content-Type': 'application/json'
    }
    
    payload = {
        'content': message
    }
    
    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 204:
        print("Webhook sent successfully")
    else:
        print(f"Failed to send webhook. Status code: {response.status_code}")

# Webhook URL
webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'

ssid = get_ssid()
private_ip = get_private_ip()
message = f"Raspberry Pi5 was open \n SSID: {ssid}\n Private IP Address: {private_ip}"
send_discord_webhook(webhook_url, message)
