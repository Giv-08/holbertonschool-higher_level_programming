#!/usr/bin/python3
"""This module handles a method to fetch posts
from JSONPlaceholder using requests.get()
"""
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/data':
            res_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        else:
            self.send_error(404)
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
