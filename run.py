"""
Convenience launcher for the Auth Security Microservice.
Run with: python run.py
"""
import sys
import os

# Ensure the root of auth_security_service is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import uvicorn

if __name__ == "__main__":
    print("=" * 70)
    print("Starting Password Protection & Management Microservice")
    print("Access Interactive Dashboard: http://localhost:8000")
    print("Access OpenAPI / Swagger Docs: http://localhost:8000/docs")
    print("=" * 70)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
