import rs_handler
from http.server import HTTPServer

class http_server:

    # Run the server with our custom handler.
    def run_server():
        server_class = HTTPServer
        httpd = server_class((rs_handler.HOST_ADDR, rs_handler.PORT), rs_handler.HTTPHandler)
        try:
            print(f'[!] Server is running on: {rs_handler.HOST_ADDR}:{rs_handler.PORT}!')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('[!] Server is terminated.')
            httpd.server_close()


if __name__ == '__main__':
    http_server.run_server()
        

