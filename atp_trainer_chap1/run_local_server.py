import http.server
import socketserver
from pathlib import Path

PORT = 8000
DIRECTORY = Path(__file__).resolve().parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor listo en http://localhost:{PORT}")
    httpd.serve_forever()
