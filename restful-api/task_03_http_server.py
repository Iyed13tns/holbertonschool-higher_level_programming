import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):

        if self.path == '/':
            self.handle_root()
        elif self.path == '/data':
            self.handle_data()
        elif self.path == '/status':
            self.handle_status()
        else:
            self.handle_not_found()
    
    def handle_root(self):

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")
    
    def handle_data(self):

        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
    
    def handle_status(self):

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK")
    
    def handle_not_found(self):

        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Endpoint not found")

def run_server():

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
