import urllib.parse
from http.server import BaseHTTPRequestHandler
import json

class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL and query parameters
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        # Set response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Create response data
        response_data = {
            "message": "Hello from Vercel!",
            "method": "GET",
            "path": parsed_path.path,
            "query_params": query_params,
            "timestamp": "2025-09-07"
        }
        
        # Send JSON response
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
        
    def do_POST(self):
        # Get content length and read the request body
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        # Parse JSON data if present
        try:
            json_data = json.loads(post_data.decode('utf-8')) if post_data else {}
        except json.JSONDecodeError:
            json_data = {"raw_data": post_data.decode('utf-8', errors='ignore')}
        
        # Set response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Create response data
        response_data = {
            "message": "POST request received",
            "method": "POST",
            "received_data": json_data,
            "timestamp": "2025-09-07"
        }
        
        # Send JSON response
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

# Vercel handler function
def handler(request, response):
    """
    This is the main entry point for Vercel serverless function.
    Vercel expects a function that takes request and response objects.
    """
    # Import required modules for Vercel
    from http.server import HTTPServer
    import io
    import sys
    
    # Create a mock server and handler
    class MockServer:
        def __init__(self):
            self.server_address = ('localhost', 8000)
            
    # Create an instance of our API handler
    api_handler = APIHandler(request, MockServer())
    
    # Set up the handler with the request
    api_handler.setup()
    
    # Route based on HTTP method
    if request.method == 'GET':
        api_handler.do_GET()
    elif request.method == 'POST':
        api_handler.do_POST()
    else:
        # Handle other methods
        api_handler.send_response(405)
        api_handler.send_header('Content-type', 'application/json')
        api_handler.end_headers()
        error_response = {"error": f"Method {request.method} not allowed"}
        api_handler.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    return api_handler.wfile.getvalue()
