# http_reverse_shell
A http reverse shell/tool I made in Python for my CyberSecurity specialization project.

## Setup:
You must first install & run the rs_client.py on the victim's machine. It's recommended that you change the config variables beforehand, so you know what IP the webserver runs on, and where the output file for the keylogger is stored. You can find the variables in `config.py`. You want to change the following variables: 
```
URL
IP_ADDRESS
OUTPUTFILEPATH
```
## How to use:
After you've managed to "infect" the victim, you have to turn on `rs_server.py`. Then, the client will connect to the server immediately. Once the connection has been made, you can see `Shell>` in the terminal window, where you can use the normal console commands used by Windows (not tested on Mac OS/Linux). There are also custom commands: 
```
stop
grab#filename
logger
```
