from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "192.168.1.101"
PORT = 9000

class TemplateServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Hello world!</h1></body></html>", "utf-8"))
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date +'"}', "utf-8"))

server = HTTPServer((HOST, PORT), TemplateServer)
print("Server is running...")
server.serve_forever()
server.server_close()
print("Server is closed...")
