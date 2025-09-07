import urllib.parse
import json
from datetime import datetime

def handler(request):
    """
    Vercel serverless function handler.
    This function will be called for each HTTP request.
    """
    
    # Parse the URL and query parameters
    url = request.url
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    
    # Get request method
    method = request.method
    
    # Common response headers
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    }
    
    if method == 'GET':
        return handle_get(request, parsed_url, query_params, headers)
    elif method == 'POST':
        return handle_post(request, parsed_url, headers)
    elif method == 'OPTIONS':
        # Handle CORS preflight
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    else:
        return {
            'statusCode': 405,
            'headers': headers,
            'body': json.dumps({
                'error': f'Method {method} not allowed',
                'allowed_methods': ['GET', 'POST', 'OPTIONS']
            })
        }

def handle_get(request, parsed_url, query_params, headers):
    """Handle GET requests"""
    
    response_data = {
        'message': 'Hello from Vercel!',
        'method': 'GET',
        'path': parsed_url.path,
        'query_params': query_params,
        'timestamp': datetime.now().isoformat(),
        'headers': dict(request.headers) if hasattr(request, 'headers') else {}
    }
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(response_data, indent=2)
    }

def handle_post(request, parsed_url, headers):
    """Handle POST requests"""
    
    # Get request body
    try:
        if hasattr(request, 'body'):
            body_data = request.body
            if isinstance(body_data, bytes):
                body_data = body_data.decode('utf-8')
            
            # Try to parse as JSON
            try:
                json_data = json.loads(body_data) if body_data else {}
            except json.JSONDecodeError:
                json_data = {'raw_data': body_data}
        else:
            json_data = {}
    except Exception as e:
        json_data = {'error': f'Failed to parse body: {str(e)}'}
    
    response_data = {
        'message': 'POST request received successfully',
        'method': 'POST',
        'path': parsed_url.path,
        'received_data': json_data,
        'timestamp': datetime.now().isoformat(),
        'headers': dict(request.headers) if hasattr(request, 'headers') else {}
    }
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(response_data, indent=2)
    }
