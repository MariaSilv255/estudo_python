import http.server

class MeuServidor(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"<h2>Hello world</h2>")
servidor = http.server.HTTPServer(('localhost',8000),MeuServidor)
servidor.serve_forever()