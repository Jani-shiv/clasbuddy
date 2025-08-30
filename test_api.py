#!/usr/bin/env python3
"""
Test script to demonstrate ClassBuddy API functionality
"""
import requests
import json
import time
import sys

def test_api():
    base_url = "http://localhost:8000"
    
    print("🚀 ClassBuddy API Test Results")
    print("=" * 50)
    
    # Test endpoints
    endpoints = [
        ("/", "Root endpoint"),
        ("/health", "Health check"),
        ("/academics/courses", "Academic courses"),
        ("/campus-map/buildings", "Campus buildings"),
        ("/events", "Events list"),
        ("/community/posts", "Community posts")
    ]
    
    for endpoint, description in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=5)
            status = "✅ SUCCESS" if response.status_code == 200 else f"❌ ERROR ({response.status_code})"
            print(f"{status} - {description} ({endpoint})")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    if isinstance(data, dict) and 'message' in data:
                        print(f"   Response: {data['message']}")
                    elif isinstance(data, list):
                        print(f"   Items count: {len(data)}")
                    else:
                        print(f"   Response type: {type(data).__name__}")
                except:
                    print(f"   Response: {response.text[:100]}...")
            
        except requests.exceptions.RequestException as e:
            print(f"❌ FAILED - {description} ({endpoint})")
            print(f"   Error: {str(e)}")
        
        time.sleep(0.1)  # Small delay between requests
    
    print("\n" + "=" * 50)
    print("🎉 ClassBuddy API Test Complete!")
    
    # Test API info
    try:
        response = requests.get(f"{base_url}/docs")
        if response.status_code == 200:
            print(f"📚 API Documentation available at: {base_url}/docs")
        
        response = requests.get(f"{base_url}/openapi.json")
        if response.status_code == 200:
            openapi_data = response.json()
            print(f"📋 API Info: {openapi_data.get('info', {}).get('title', 'ClassBuddy')} v{openapi_data.get('info', {}).get('version', '1.0.0')}")
    except:
        pass

if __name__ == "__main__":
    test_api()
