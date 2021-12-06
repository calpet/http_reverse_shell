from http.server import BaseHTTPRequestHandler

#   Required constants
HOST_ADDR = '0.0.0.0'
PORT = 80

class HTTPHandler(BaseHTTPRequestHandler):

    def do_GET(input):
        command = input("Shell> ")
        
    def do_POST(input):
        input.send_response(200)
