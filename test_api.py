"""
Test script for the Vercel API handler
Run this locally to test your API before deployment
"""

import json
import urllib.parse
from datetime import datetime

# Mock request object for testing
class MockRequest:
    def __init__(self, method='GET', url='http://localhost:3000/api/', body=None, headers=None):
        self.method = method
        self.url = url
        self.body = body
        self.headers = headers or {}

# Import our handler
from api.index import handler

def test_get_request():
    """Test GET request"""
    print("Testing GET request...")
    
    request = MockRequest(
        method='GET',
        url='http://localhost:3000/api/?name=John&age=30&city=NewYork',
        headers={'User-Agent': 'Test-Client/1.0'}
    )
    
    response = handler(request)
    print(f"Status Code: {response['statusCode']}")
    print(f"Response Body:\n{response['body']}")
    print("-" * 50)

def test_post_request():
    """Test POST request"""
    print("Testing POST request...")
    
    test_data = {
        "message": "Hello from test",
        "user": "TestUser",
        "timestamp": datetime.now().isoformat()
    }
    
    request = MockRequest(
        method='POST',
        url='http://localhost:3000/api/',
        body=json.dumps(test_data),
        headers={
            'Content-Type': 'application/json',
            'User-Agent': 'Test-Client/1.0'
        }
    )
    
    response = handler(request)
    print(f"Status Code: {response['statusCode']}")
    print(f"Response Body:\n{response['body']}")
    print("-" * 50)

def test_unsupported_method():
    """Test unsupported method"""
    print("Testing unsupported method (PUT)...")
    
    request = MockRequest(
        method='PUT',
        url='http://localhost:3000/api/',
        headers={'User-Agent': 'Test-Client/1.0'}
    )
    
    response = handler(request)
    print(f"Status Code: {response['statusCode']}")
    print(f"Response Body:\n{response['body']}")
    print("-" * 50)

if __name__ == "__main__":
    print("Running API Handler Tests\n")
    print("=" * 50)
    
    test_get_request()
    test_post_request()
    test_unsupported_method()
    
    print("Tests completed!")
