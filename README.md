# My Email Agent API

A Vercel serverless function API built with Python.

## Project Structure

```
my-email-agent/
├── api/
│   ├── index.py          # Main API handler (accessible at /api/)
│   └── handler.py        # Alternative handler implementation
├── vercel.json           # Vercel configuration
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## API Endpoints

### GET /api/
- Returns a welcome message with request details
- Query parameters are parsed and included in response

Example:
```bash
curl https://your-app.vercel.app/api/?name=John&age=30
```

### POST /api/
- Accepts JSON data in request body
- Returns the received data along with request details

Example:
```bash
curl -X POST https://your-app.vercel.app/api/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello World", "user": "John"}'
```

## Local Development

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Run locally:
```bash
vercel dev
```

3. Your API will be available at `http://localhost:3000/api/`

## Deployment

1. Login to Vercel:
```bash
vercel login
```

2. Deploy:
```bash
vercel
```

3. Follow the prompts to deploy your function

## Features

- ✅ GET and POST request handling
- ✅ Query parameter parsing
- ✅ JSON request/response handling
- ✅ CORS headers for browser compatibility
- ✅ Error handling
- ✅ Timestamp tracking
- ✅ Request headers inspection

## Response Format

All responses follow this structure:
```json
{
  "message": "Status message",
  "method": "HTTP_METHOD",
  "path": "/api/path",
  "timestamp": "2025-09-07T...",
  "headers": {...},
  "query_params": {...},  // GET requests
  "received_data": {...}  // POST requests
}
```
