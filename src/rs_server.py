from rs_handler import rs_handler
from http.server import HTTPServer
from config import App

class rs_server:

    # Run the server with our custom handler.
    def run_server():
        server_class = HTTPServer
        httpd = server_class((App.config('IP_ADDR'), App.config('PORT')), rs_handler)
        try:
            print(f'[!] Server is running on: {App.config("IP_ADDR")}:{App.config("PORT")}!')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('[!] Server is terminated.')
            httpd.server_close()

if __name__ == '__main__':
    rs_server.run_server()
