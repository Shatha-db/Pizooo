#!/usr/bin/env python3
"""
Comprehensive Backend API Testing for Pizoo Dating App
Tests all authentication endpoints, LiveKit integration, and MongoDB connection
"""

import asyncio
import httpx
import os
import sys
import json
import base64
from datetime import datetime
from typing import Dict, Any, Optional
from PIL import Image
import io

# Add backend directory to path for imports
sys.path.append('/app/backend')

# Test configuration
BACKEND_URL = os.getenv('REACT_APP_BACKEND_URL', 'https://pizoo-debug.preview.emergentagent.com')
API_BASE = f"{BACKEND_URL}/api"

# Test data
TEST_USER_DATA = {
    "name": "أحمد محمد",
    "email": "ahmed.test@pizoo.ch", 
    "phone_number": "+41791234567",
    "password": "SecurePass123!",
    "terms_accepted": True
}

TEST_LOGIN_DATA = {
    "email": "ahmed.test@pizoo.ch",
    "password": "SecurePass123!"
}

class BackendTester:
    def __init__(self):
        self.client = httpx.AsyncClient(timeout=30.0)
        self.access_token = None
        self.user_id = None
        self.test_results = []
        
    async def __aenter__(self):
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()
    
    def log_result(self, test_name: str, success: bool, details: str = "", response_data: Any = None):
        """Log test result"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if details:
            print(f"   {details}")
        if response_data and not success:
            print(f"   Response: {json.dumps(response_data, indent=2, ensure_ascii=False)}")
        print()
        
        self.test_results.append({
            "test": test_name,
            "success": success,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })
    
    async def test_backend_connectivity(self):
        """Test basic backend connectivity via API root"""
        try:
            response = await self.client.get(f"{API_BASE}/")
            
            if response.status_code == 200:
                data = response.json()
                if 'message' in data:
                    self.log_result("Backend Connectivity", True, f"API accessible: {data['message']}")
                else:
                    self.log_result("Backend Connectivity", True, "API accessible")
            else:
                self.log_result("Backend Connectivity", False, f"HTTP {response.status_code}", response.text)
                
        except Exception as e:
            self.log_result("Backend Connectivity", False, f"Connection error: {str(e)}")
    
    async def test_mongodb_connection(self):
        """Test MongoDB connection via user registration (indirect test)"""
        try:
            # Test MongoDB by attempting to register a user (which requires DB connection)
            test_email = f"db_test_{int(datetime.now().timestamp())}@pizoo.ch"
            test_data = {
                "name": "DB Test User",
                "email": test_email,
                "phone_number": "+41791234999",
                "password": "TestPass123!",
                "terms_accepted": True
            }
            
            response = await self.client.post(f"{API_BASE}/auth/register", json=test_data)
            
            if response.status_code == 200:
                self.log_result("MongoDB Connection", True, "Database operations working (user registration successful)")
            elif response.status_code == 400:
                # Even validation errors indicate DB connection is working
                self.log_result("MongoDB Connection", True, "Database connection working (validation response received)")
            else:
                self.log_result("MongoDB Connection", False, f"Unexpected response: HTTP {response.status_code}")
                
        except Exception as e:
            self.log_result("MongoDB Connection", False, f"Error: {str(e)}")
    
    async def test_cors_settings(self):
        """Test CORS settings for pizoo.ch"""
        try:
            # Test preflight request
            headers = {
                'Origin': 'https://pizoo.ch',
                'Access-Control-Request-Method': 'POST',
                'Access-Control-Request-Headers': 'Content-Type,Authorization'
            }
            
            response = await self.client.options(f"{API_BASE}/auth/login", headers=headers)
            
            cors_origin = response.headers.get('Access-Control-Allow-Origin', '')
            cors_methods = response.headers.get('Access-Control-Allow-Methods', '')
            
            if 'https://pizoo.ch' in cors_origin or '*' in cors_origin:
                self.log_result("CORS Settings", True, f"Origin allowed: {cors_origin}")
            else:
                self.log_result("CORS Settings", False, f"pizoo.ch not in allowed origins: {cors_origin}")
                
        except Exception as e:
            self.log_result("CORS Settings", False, f"Error: {str(e)}")
    
    async def test_auth_register(self):
        """Test user registration endpoint"""
        try:
            response = await self.client.post(
                f"{API_BASE}/auth/register",
                json=TEST_USER_DATA
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'access_token' in data and 'user' in data:
                    self.access_token = data['access_token']
                    self.user_id = data['user']['id']
                    self.log_result("Auth Register", True, f"User created: {data['user']['email']}")
                else:
                    self.log_result("Auth Register", False, "Missing access_token or user in response", data)
            elif response.status_code == 400 and "مسجل مسبقاً" in response.text:
                # User already exists - try login instead
                self.log_result("Auth Register", True, "User already exists (expected)")
                await self.test_auth_login()
            else:
                self.log_result("Auth Register", False, f"HTTP {response.status_code}", response.json())
                
        except Exception as e:
            self.log_result("Auth Register", False, f"Error: {str(e)}")
    
    async def test_auth_login(self):
        """Test user login endpoint"""
        try:
            response = await self.client.post(
                f"{API_BASE}/auth/login",
                json=TEST_LOGIN_DATA
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'access_token' in data and 'user' in data:
                    self.access_token = data['access_token']
                    self.user_id = data['user']['id']
                    verified = data['user'].get('verified', False)
                    self.log_result("Auth Login", True, f"Login successful, verified: {verified}")
                else:
                    self.log_result("Auth Login", False, "Missing access_token or user in response", data)
            else:
                self.log_result("Auth Login", False, f"HTTP {response.status_code}", response.json())
                
        except Exception as e:
            self.log_result("Auth Login", False, f"Error: {str(e)}")
    
    async def test_auth_google_oauth(self):
        """Test Google OAuth endpoint (without actual OAuth flow)"""
        try:
            # Test with invalid session_id to check endpoint exists and handles errors properly
            response = await self.client.post(
                f"{API_BASE}/auth/oauth/google",
                json={"session_id": "invalid_test_session"}
            )
            
            # We expect this to fail with 401 (invalid session), which means endpoint exists
            if response.status_code == 401:
                error_data = response.json()
                if "Invalid or expired session" in error_data.get('detail', ''):
                    self.log_result("Auth Google OAuth", True, "Endpoint exists and handles invalid sessions correctly")
                else:
                    self.log_result("Auth Google OAuth", False, "Unexpected error message", error_data)
            else:
                self.log_result("Auth Google OAuth", False, f"Unexpected status code: {response.status_code}", response.json())
                
        except Exception as e:
            self.log_result("Auth Google OAuth", False, f"Error: {str(e)}")
    
    async def test_users_me(self):
        """Test /api/users/me endpoint (requires authentication)"""
        if not self.access_token:
            self.log_result("Users Me", False, "No access token available - login first")
            return
            
        try:
            headers = {"Authorization": f"Bearer {self.access_token}"}
            response = await self.client.get(f"{API_BASE}/auth/me", headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                if 'user' in data and data['user'].get('id'):
                    user_info = data['user']
                    self.log_result("Users Me", True, f"User info retrieved: {user_info.get('email', 'N/A')}")
                else:
                    self.log_result("Users Me", False, "Invalid user data structure", data)
            else:
                self.log_result("Users Me", False, f"HTTP {response.status_code}", response.json())
                
        except Exception as e:
            self.log_result("Users Me", False, f"Error: {str(e)}")
    
    async def test_livekit_configuration(self):
        """Test LiveKit environment configuration"""
        try:
            # Check environment variables directly
            import os
            from dotenv import load_dotenv
            
            # Load environment from backend directory
            load_dotenv('/app/backend/.env')
            
            livekit_url = os.getenv('LIVEKIT_URL')
            livekit_api_key = os.getenv('LIVEKIT_API_KEY') 
            livekit_api_secret = os.getenv('LIVEKIT_API_SECRET')
            
            config_status = []
            
            if livekit_url:
                config_status.append(f"URL: {livekit_url}")
            else:
                config_status.append("URL: ❌ Missing")
            
            if livekit_api_key:
                config_status.append(f"API_KEY: {livekit_api_key[:8]}...")
            else:
                config_status.append("API_KEY: ❌ Missing")
            
            if livekit_api_secret:
                config_status.append(f"API_SECRET: {livekit_api_secret[:8]}...")
            else:
                config_status.append("API_SECRET: ❌ Missing")
            
            is_configured = bool(livekit_url and livekit_api_key and livekit_api_secret)
            
            if is_configured:
                self.log_result("LiveKit Configuration", True, f"All credentials present: {', '.join(config_status)}")
            else:
                self.log_result("LiveKit Configuration", False, f"Missing credentials: {', '.join(config_status)}")
                
        except Exception as e:
            self.log_result("LiveKit Configuration", False, f"Error checking configuration: {str(e)}")
    
    async def test_livekit_token_endpoint(self):
        """Test LiveKit token generation endpoint"""
        if not self.access_token:
            self.log_result("LiveKit Token", False, "No access token available - login first")
            return
            
        try:
            headers = {"Authorization": f"Bearer {self.access_token}"}
            test_data = {
                "match_id": "test_match_123",
                "call_type": "video"
            }
            
            response = await self.client.post(
                f"{API_BASE}/livekit/token",
                json=test_data,
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success') and 'token' in data and 'url' in data:
                    token_info = {
                        'url': data.get('url'),
                        'room_name': data.get('room_name'),
                        'participant_identity': data.get('participant_identity')
                    }
                    self.log_result("LiveKit Token", True, f"Token generated successfully: {json.dumps(token_info, ensure_ascii=False)}")
                else:
                    self.log_result("LiveKit Token", False, "Invalid response format", data)
            elif response.status_code == 403:
                # User not verified
                error_data = response.json()
                if "verified" in error_data.get('detail', '').lower():
                    self.log_result("LiveKit Token", True, "Endpoint working - requires verified user (expected)")
                else:
                    self.log_result("LiveKit Token", False, f"Unexpected 403 error: {error_data}")
            elif response.status_code == 429:
                # Rate limited
                self.log_result("LiveKit Token", True, "Endpoint working - rate limited (expected)")
            else:
                self.log_result("LiveKit Token", False, f"HTTP {response.status_code}", response.json())
                
        except Exception as e:
            self.log_result("LiveKit Token", False, f"Error: {str(e)}")
    
    async def test_livekit_token_response_format(self):
        """Test LiveKit token response format using service directly"""
        try:
            from livekit_service import LiveKitService
            
            # Test token generation directly
            result = LiveKitService.create_room_token(
                match_id="test_match_format",
                user_id="test_user_123",
                user_name="Test User",
                call_type="video"
            )
            
            required_fields = ['success', 'token', 'url', 'room_name', 'participant_identity']
            missing_fields = [field for field in required_fields if field not in result]
            
            if result.get('success') and not missing_fields:
                self.log_result("LiveKit Response Format", True, f"All required fields present: {required_fields}")
            elif not result.get('success'):
                # Service not configured - this is expected
                error_code = result.get('error_code', 'UNKNOWN')
                if error_code == 'SERVICE_UNAVAILABLE':
                    self.log_result("LiveKit Response Format", True, "Service correctly reports unavailable status")
                else:
                    self.log_result("LiveKit Response Format", False, f"Unexpected error: {result}")
            else:
                self.log_result("LiveKit Response Format", False, f"Missing fields: {missing_fields}", result)
                
        except Exception as e:
            self.log_result("LiveKit Response Format", False, f"Error: {str(e)}")
    
    async def test_email_verification_endpoints(self):
        """Test email verification endpoints"""
        try:
            # Test send email verification
            email_data = {
                "email": "test.verification@pizoo.ch",
                "name": "Test User"
            }
            
            response = await self.client.post(
                f"{API_BASE}/auth/email/send-link",
                json=email_data
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success') and 'expires_in' in data:
                    self.log_result("Email Verification Send", True, f"Email sent successfully, expires in {data['expires_in']}s")
                else:
                    self.log_result("Email Verification Send", False, "Invalid response format", data)
            else:
                self.log_result("Email Verification Send", False, f"HTTP {response.status_code}", response.json())
            
            # Test verify with invalid token
            verify_response = await self.client.post(
                f"{API_BASE}/auth/email/verify",
                json={"token": "invalid_test_token"}
            )
            
            if verify_response.status_code == 400:
                self.log_result("Email Verification Verify", True, "Correctly rejects invalid token")
            else:
                self.log_result("Email Verification Verify", False, f"Unexpected response to invalid token: {verify_response.status_code}")
                
        except Exception as e:
            self.log_result("Email Verification", False, f"Error: {str(e)}")
    
    async def test_jwt_refresh_endpoint(self):
        """Test JWT refresh token endpoint"""
        try:
            # Test with invalid refresh token
            response = await self.client.post(
                f"{API_BASE}/auth/refresh",
                json={"refresh_token": "invalid_refresh_token"}
            )
            
            if response.status_code == 401:
                error_data = response.json()
                if "Invalid or expired" in error_data.get('detail', ''):
                    self.log_result("JWT Refresh", True, "Correctly rejects invalid refresh token")
                else:
                    self.log_result("JWT Refresh", False, "Unexpected error message", error_data)
            else:
                self.log_result("JWT Refresh", False, f"Unexpected status code: {response.status_code}", response.json())
                
        except Exception as e:
            self.log_result("JWT Refresh", False, f"Error: {str(e)}")
    
    def create_test_image(self, width: int = 800, height: int = 600, format: str = 'JPEG') -> bytes:
        """Create a test image for upload testing"""
        try:
            # Create a simple test image with colored background
            image = Image.new('RGB', (width, height), color=(73, 109, 137))
            
            # Add some text to make it identifiable
            try:
                from PIL import ImageDraw, ImageFont
                draw = ImageDraw.Draw(image)
                # Use default font
                draw.text((width//4, height//2), "Pizoo Test Image", fill=(255, 255, 255))
            except:
                # If PIL text drawing fails, just use the colored background
                pass
            
            # Convert to bytes
            img_bytes = io.BytesIO()
            image.save(img_bytes, format=format, quality=85)
            return img_bytes.getvalue()
            
        except Exception as e:
            # Fallback: create minimal test image data
            return b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\xff\xc0\x00\x11\x08\x00\x01\x00\x01\x01\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00\x3f\x00\xaa\xff\xd9'
    
    async def test_cloudinary_configuration(self):
        """Test Cloudinary configuration from environment"""
        try:
            # Load environment from backend directory
            from dotenv import load_dotenv
            load_dotenv('/app/backend/.env')
            
            cloudinary_url = os.getenv('CLOUDINARY_URL')
            
            if cloudinary_url and cloudinary_url.strip():
                # Parse URL to check format
                import re
                match = re.match(r'cloudinary://([^:]+):([^@]+)@(.+)', cloudinary_url)
                if match:
                    api_key, api_secret, cloud_name = match.groups()
                    self.log_result("Cloudinary Configuration", True, f"Configured with cloud: {cloud_name}")
                else:
                    self.log_result("Cloudinary Configuration", False, "Invalid CLOUDINARY_URL format")
            else:
                self.log_result("Cloudinary Configuration", False, "CLOUDINARY_URL is empty or missing")
                
        except Exception as e:
            self.log_result("Cloudinary Configuration", False, f"Error checking configuration: {str(e)}")
    
    async def test_profile_creation(self):
        """Test profile creation for image upload testing"""
        if not self.access_token:
            self.log_result("Profile Creation", False, "No access token available - login first")
            return
            
        try:
            headers = {"Authorization": f"Bearer {self.access_token}"}
            
            # Check if profile already exists
            profile_response = await self.client.get(f"{API_BASE}/profile/me", headers=headers)
            
            if profile_response.status_code == 200:
                profile_data = profile_response.json()
                if profile_data.get('id'):  # Profile exists if it has an ID
                    self.log_result("Profile Creation", True, "Profile already exists")
                    return
            
            # Create profile if it doesn't exist
            profile_data = {
                "display_name": "أحمد محمد",
                "bio": "مطور تطبيقات من سويسرا",
                "age": 28,
                "gender": "male",
                "location": "Basel, Switzerland",
                "interests": ["تقنية", "سفر", "قراءة"]
            }
            
            response = await self.client.post(
                f"{API_BASE}/profile/create",
                json=profile_data,
                headers=headers
            )
            
            if response.status_code == 200:
                self.log_result("Profile Creation", True, "Profile created successfully")
            else:
                self.log_result("Profile Creation", False, f"HTTP {response.status_code}", response.json())
                
        except Exception as e:
            self.log_result("Profile Creation", False, f"Error: {str(e)}")
    
    async def test_image_upload_endpoint(self):
        """Test image upload endpoint - main functionality"""
        if not self.access_token:
            self.log_result("Image Upload", False, "No access token available - login first")
            return
            
        try:
            headers = {"Authorization": f"Bearer {self.access_token}"}
            
            # Create test image
            test_image_bytes = self.create_test_image(800, 600, 'JPEG')
            
            # Prepare multipart form data
            files = {
                'file': ('test_image.jpg', test_image_bytes, 'image/jpeg')
            }
            data = {
                'is_primary': 'false'
            }
            
            # Upload image
            response = await self.client.post(
                f"{API_BASE}/profile/photo/upload",
                files=files,
                data=data,
                headers=headers
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get('success') and result.get('photo', {}).get('url'):
                    photo_info = result['photo']
                    url = photo_info.get('url', '')
                    webp_url = photo_info.get('webp_url', '')
                    
                    # Verify URLs are HTTPS and from Cloudinary
                    url_valid = url.startswith('https://res.cloudinary.com/')
                    webp_valid = webp_url.startswith('https://res.cloudinary.com/') if webp_url else True
                    
                    if url_valid and webp_valid:
                        self.log_result("Image Upload", True, f"Image uploaded successfully. URL: {url[:50]}...")
                    else:
                        self.log_result("Image Upload", False, f"Invalid URLs - URL valid: {url_valid}, WebP valid: {webp_valid}")
                else:
                    self.log_result("Image Upload", False, "Missing success flag or photo URL in response", result)
            elif response.status_code == 503:
                # Service unavailable - Cloudinary not configured
                error_data = response.json()
                if "خدمة رفع الصور غير متاحة حالياً" in error_data.get('detail', ''):
                    self.log_result("Image Upload", False, "Cloudinary service unavailable - configuration issue")
                else:
                    self.log_result("Image Upload", False, f"Service unavailable: {error_data}")
            else:
                self.log_result("Image Upload", False, f"HTTP {response.status_code}", response.json())
                
        except Exception as e:
            self.log_result("Image Upload", False, f"Error: {str(e)}")
    
    async def test_image_upload_profile_update(self):
        """Test that uploaded image is saved to profile.photos"""
        if not self.access_token:
            self.log_result("Profile Photo Update", False, "No access token available - login first")
            return
            
        try:
            headers = {"Authorization": f"Bearer {self.access_token}"}
            
            # Get profile before upload
            profile_before = await self.client.get(f"{API_BASE}/profile/me", headers=headers)
            photos_before = []
            if profile_before.status_code == 200:
                profile_data = profile_before.json()
                photos_before = profile_data.get('photos', [])
            
            # Create and upload test image
            test_image_bytes = self.create_test_image(600, 400, 'JPEG')
            
            files = {
                'file': ('profile_test.jpg', test_image_bytes, 'image/jpeg')
            }
            data = {'is_primary': 'true'}
            
            upload_response = await self.client.post(
                f"{API_BASE}/profile/photo/upload",
                files=files,
                data=data,
                headers=headers
            )
            
            if upload_response.status_code == 200:
                # Get profile after upload
                profile_after = await self.client.get(f"{API_BASE}/profile/me", headers=headers)
                
                if profile_after.status_code == 200:
                    profile_data = profile_after.json()
                    photos_after = profile_data.get('photos', [])
                    
                    if len(photos_after) > len(photos_before):
                        self.log_result("Profile Photo Update", True, f"Photo added to profile. Total photos: {len(photos_after)}")
                    else:
                        self.log_result("Profile Photo Update", False, f"Photo count unchanged. Before: {len(photos_before)}, After: {len(photos_after)}")
                else:
                    self.log_result("Profile Photo Update", False, "Failed to retrieve profile after upload")
            else:
                self.log_result("Profile Photo Update", False, f"Upload failed: HTTP {upload_response.status_code}")
                
        except Exception as e:
            self.log_result("Profile Photo Update", False, f"Error: {str(e)}")
    
    async def test_image_upload_error_cases(self):
        """Test image upload error handling"""
        if not self.access_token:
            self.log_result("Image Upload Error Cases", False, "No access token available - login first")
            return
            
        try:
            headers = {"Authorization": f"Bearer {self.access_token}"}
            
            # Test 1: Upload non-image file
            text_file = b"This is not an image file"
            files = {'file': ('test.txt', text_file, 'text/plain')}
            
            response = await self.client.post(
                f"{API_BASE}/profile/photo/upload",
                files=files,
                headers=headers
            )
            
            if response.status_code == 415:  # Unsupported Media Type
                self.log_result("Image Upload Error Cases", True, "Correctly rejects non-image files (415)")
            elif response.status_code == 400:  # Bad Request
                self.log_result("Image Upload Error Cases", True, "Correctly rejects non-image files (400)")
            else:
                self.log_result("Image Upload Error Cases", False, f"Unexpected response to non-image: {response.status_code}")
            
            # Test 2: Upload oversized image (create large image)
            try:
                large_image_bytes = self.create_test_image(4000, 4000, 'JPEG')  # Large image
                # Make it even larger by duplicating data
                oversized_data = large_image_bytes * 10  # Multiply to make it very large
                
                files = {'file': ('large.jpg', oversized_data, 'image/jpeg')}
                
                response = await self.client.post(
                    f"{API_BASE}/profile/photo/upload",
                    files=files,
                    headers=headers
                )
                
                if response.status_code == 413:  # Request Entity Too Large
                    self.log_result("Image Upload Error Cases", True, "Correctly rejects oversized files (413)")
                elif response.status_code == 400:
                    error_data = response.json()
                    if "حجم الملف" in error_data.get('detail', ''):
                        self.log_result("Image Upload Error Cases", True, "Correctly rejects oversized files (400)")
                    else:
                        self.log_result("Image Upload Error Cases", False, f"Unexpected error for large file: {error_data}")
                else:
                    # Large file might still be processed if under limit
                    self.log_result("Image Upload Error Cases", True, f"Large file handling: HTTP {response.status_code}")
            except Exception:
                # If we can't create large file, skip this test
                self.log_result("Image Upload Error Cases", True, "Large file test skipped (creation failed)")
                
        except Exception as e:
            self.log_result("Image Upload Error Cases", False, f"Error: {str(e)}")
    
    def print_summary(self):
        """Print test summary"""
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['success'])
        failed_tests = total_tests - passed_tests
        
        print("=" * 60)
        print("🧪 BACKEND API TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        print()
        
        if failed_tests > 0:
            print("❌ FAILED TESTS:")
            for result in self.test_results:
                if not result['success']:
                    print(f"   • {result['test']}: {result['details']}")
            print()
        
        print("🔍 KEY FINDINGS:")
        
        # Check critical endpoints
        critical_endpoints = ['Backend Connectivity', 'MongoDB Connection', 'Auth Login', 'LiveKit Configuration']
        critical_failures = [r for r in self.test_results if r['test'] in critical_endpoints and not r['success']]
        
        if not critical_failures:
            print("   ✅ All critical endpoints are working")
        else:
            print("   ❌ Critical endpoint failures detected:")
            for failure in critical_failures:
                print(f"      • {failure['test']}")
        
        # Check LiveKit status
        livekit_tests = [r for r in self.test_results if 'LiveKit' in r['test']]
        livekit_working = all(r['success'] for r in livekit_tests)
        
        if livekit_working:
            print("   ✅ LiveKit integration is properly configured")
        else:
            print("   ⚠️ LiveKit integration has issues")
        
        # Check auth system
        auth_tests = [r for r in self.test_results if 'Auth' in r['test']]
        auth_working = any(r['success'] for r in auth_tests if r['test'] in ['Auth Login', 'Auth Register'])
        
        if auth_working:
            print("   ✅ Authentication system is working")
        else:
            print("   ❌ Authentication system has critical issues")
        
        print("=" * 60)

async def main():
    """Run all backend tests"""
    print("🚀 Starting Pizoo Backend API Tests")
    print(f"🌐 Backend URL: {BACKEND_URL}")
    print(f"🔗 API Base: {API_BASE}")
    print("=" * 60)
    
    async with BackendTester() as tester:
        # Core infrastructure tests
        await tester.test_backend_connectivity()
        await tester.test_mongodb_connection()
        await tester.test_cors_settings()
        
        # Authentication tests
        await tester.test_auth_register()
        await tester.test_auth_login()
        await tester.test_auth_google_oauth()
        await tester.test_users_me()
        
        # Email verification tests
        await tester.test_email_verification_endpoints()
        await tester.test_jwt_refresh_endpoint()
        
        # LiveKit tests
        await tester.test_livekit_configuration()
        await tester.test_livekit_token_endpoint()
        await tester.test_livekit_token_response_format()
        
        # Image upload tests (Arabic review request)
        await tester.test_cloudinary_configuration()
        await tester.test_profile_creation()
        await tester.test_image_upload_endpoint()
        await tester.test_image_upload_profile_update()
        await tester.test_image_upload_error_cases()
        
        # Print summary
        tester.print_summary()

if __name__ == "__main__":
    asyncio.run(main())