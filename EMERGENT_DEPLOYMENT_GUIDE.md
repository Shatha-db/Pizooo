# 🚀 Emergent Deployment Guide - Pizoo App

**Date:** November 7, 2025, 18:00 UTC  
**Status:** ✅ DEPLOYMENT READY  
**Platform:** Emergent Native Kubernetes Deployments

---

## ✅ Deployment Readiness Status

### Overall: **READY TO DEPLOY**

All critical issues resolved. Application is configured for Kubernetes deployment with environment variable injection.

---

## 🔧 Issues Fixed

### ✅ Issue 1: Hardcoded Fallback URL (RESOLVED)

**File:** `frontend/src/components/LiveKitCall.jsx`

**Before:**
```javascript
const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || 'https://datemaps.emergent.host';
```

**After:**
```javascript
const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
```

**Why:** Hardcoded fallback could cause production issues. Now requires environment variable to be set (which Emergent provides).

---

## 📋 Deployment Checklist

### ✅ Application Configuration

- [x] ✅ **No `.env` files in repository** (security best practice)
- [x] ✅ **`.env.example` present** for reference
- [x] ✅ **Backend reads from environment variables** only
- [x] ✅ **Frontend uses `REACT_APP_BACKEND_URL`**
- [x] ✅ **No hardcoded URLs** (removed fallback)
- [x] ✅ **MongoDB support** (compatible with Emergent)
- [x] ✅ **CORS configured** via environment variables

---

## 🔐 Required Environment Variables

### Backend Variables (Set in Emergent Deployment):

```bash
# Database (MongoDB Atlas)
MONGO_URL=mongodb+srv://<user>:<password>@<cluster>.mongodb.net/<database>?retryWrites=true&w=majority
DB_NAME=pizoo_production
MONGODB_URI=<same-as-MONGO_URL>
MONGODB_DB_NAME=pizoo_production

# Application URLs
FRONTEND_URL=https://your-app.emergent.host
CORS_ORIGINS=https://your-app.emergent.host,https://pizoo.ch

# LiveKit (Video/Audio)
LIVEKIT_URL=wss://your-livekit-url.livekit.cloud
LIVEKIT_API_KEY=<your-key>
LIVEKIT_API_SECRET=<your-secret>

# Cloudinary (Image Storage)
CLOUDINARY_CLOUD_NAME=<your-cloud>
CLOUDINARY_API_KEY=<your-key>
CLOUDINARY_API_SECRET=<your-secret>
CLOUDINARY_URL=cloudinary://<key>:<secret>@<cloud>

# Email (SMTP)
EMAIL_FROM="info Pizoo <support@pizoo.ch>"
EMAIL_FROM_NAME=info Pizoo
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=<your-email>
SMTP_PASS=<your-smtp-password>
EMAIL_MODE=smtp

# Security
SECRET_KEY=<generate-secure-random-64-char-string>
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
JWT_REFRESH_TOKEN_EXPIRE_DAYS=7

# reCAPTCHA (Optional)
RECAPTCHA_SITE_KEY=<your-site-key>
RECAPTCHA_SECRET_KEY=<your-secret-key>

# Feature Flags
ENABLE_EMAIL_VERIFICATION=true
ENABLE_VIDEO_CALLS=true

# Port (Emergent provides this)
PORT=8001
```

---

### Frontend Variables (Set in Emergent Deployment):

```bash
# Backend API URL (CRITICAL - must be set)
REACT_APP_BACKEND_URL=https://your-app.emergent.host

# Sentry (Optional)
REACT_APP_SENTRY_DSN=<your-sentry-dsn>
REACT_APP_SENTRY_TRACES_SAMPLE=0.2
REACT_APP_ENVIRONMENT=production
```

---

## 🎯 Deployment Steps

### 1. Prepare Environment Variables

Create a file with all required environment variables (use `.env.example` as reference).

**For Backend:**
- Copy values from `/app/backend/.env.example`
- Replace placeholder values with actual production credentials

**For Frontend:**
- Set `REACT_APP_BACKEND_URL` to your Emergent deployment URL
- Add any optional variables (Sentry, etc.)

---

### 2. Deploy to Emergent

#### Via Emergent Dashboard:

1. **Go to Emergent Deployments:**
   - Navigate to your Emergent dashboard
   - Select "New Deployment" or "Deploy App"

2. **Connect Repository:**
   - Repository: `Shatha-db/Pizooo`
   - Branch: `main`

3. **Configure Build:**
   - **Backend:**
     - Framework: FastAPI
     - Build Command: (auto-detected)
     - Port: 8001 (or as specified)
   
   - **Frontend:**
     - Framework: Create React App
     - Build Command: `cd frontend && yarn build`
     - Output Directory: `frontend/build`

4. **Add Environment Variables:**
   - Paste all backend variables
   - Paste all frontend variables
   - Verify all required variables are present

5. **Deploy:**
   - Click "Deploy"
   - Wait for build to complete (2-5 minutes)
   - Monitor build logs for any errors

---

### 3. Verify Deployment

#### A. Check Deployment Status:

```bash
# Check if deployment is live
curl -I https://your-app.emergent.host

# Expected: HTTP/2 200 OK
```

#### B. Test Backend Health:

```bash
# Health endpoint
curl https://your-app.emergent.host/api/health

# Expected: {"status":"healthy","database":"connected"}
```

#### C. Test Frontend:

Visit in browser:
- `https://your-app.emergent.host/` (should load app)
- `https://your-app.emergent.host/login` (should show login page)
- `https://your-app.emergent.host/register` (should show register page)

**Verify:**
- ✅ New PiZOO branding visible (Classic Orange on auth pages)
- ✅ No 404 errors
- ✅ SPA routing works
- ✅ No console errors

---

## 🔍 Troubleshooting

### Issue: "REACT_APP_BACKEND_URL is undefined"

**Symptom:**
- Frontend can't connect to backend
- Console shows: `TypeError: Cannot read property 'REACT_APP_BACKEND_URL' of undefined`

**Solution:**
1. Verify `REACT_APP_BACKEND_URL` is set in Emergent environment variables
2. Ensure it's set for **frontend** service (not backend)
3. Rebuild deployment after adding variable

---

### Issue: "Database connection failed"

**Symptom:**
- Backend logs show: `Failed to connect to MongoDB`
- API returns 500 errors

**Solution:**
1. Verify `MONGO_URL` is correct MongoDB Atlas connection string
2. Ensure MongoDB Atlas allows connections from Emergent IPs
3. Check username/password in connection string
4. Verify database name exists

**MongoDB Atlas Setup:**
1. Go to MongoDB Atlas Dashboard
2. Network Access → Add IP Address
3. Add `0.0.0.0/0` (allow from anywhere) or specific Emergent IPs
4. Database Access → Ensure user has read/write permissions

---

### Issue: "CORS errors in browser"

**Symptom:**
- Frontend loaded but API calls fail
- Console shows: `Access to fetch blocked by CORS policy`

**Solution:**
1. Verify `CORS_ORIGINS` environment variable includes your Emergent URL
2. Format: `https://your-app.emergent.host` (no trailing slash)
3. If using custom domain, add it too: `https://your-app.emergent.host,https://pizoo.ch`
4. Redeploy after updating

---

### Issue: "Build fails with missing dependencies"

**Symptom:**
- Build logs show: `Module not found` or `Command not found`

**Solutions:**

**Backend:**
1. Verify `requirements.txt` is present
2. Ensure all imports in code are in requirements.txt
3. Check Python version compatibility (3.11 recommended)

**Frontend:**
1. Verify `package.json` has all dependencies
2. Ensure `yarn.lock` or `package-lock.json` is present
3. Check Node.js version (20.x recommended)

---

### Issue: "Environment variable not loading"

**Symptom:**
- Logs show: `KeyError: 'SOME_VAR'` or undefined variable

**Solution:**
1. Check variable name spelling (case-sensitive)
2. Ensure variable is set in correct service (backend vs frontend)
3. Frontend vars must start with `REACT_APP_`
4. Rebuild/redeploy after adding variables

---

## 📊 Expected Build Output

### Successful Backend Build:
```
[BUILD] Installing dependencies from requirements.txt
[BUILD] Collecting fastapi...
[BUILD] Successfully installed fastapi pymongo motor...
[BUILD] Starting application on port 8001
[DEPLOY] Backend deployed successfully
[DEPLOY] URL: https://your-app.emergent.host
```

### Successful Frontend Build:
```
[BUILD] Installing dependencies: yarn install
[BUILD] Building: yarn build
[BUILD] Creating optimized production build...
[BUILD] Compiled successfully.
[BUILD] File sizes after gzip:
[BUILD]   421.56 kB  static/js/main.c9df4bfc.js
[BUILD]   25.72 kB   static/css/main.588aa498.css
[UPLOAD] Uploading build outputs...
[DEPLOY] Frontend deployed successfully
```

---

## 🎯 Post-Deployment Checklist

After successful deployment, verify:

- [ ] ✅ Backend health endpoint returns 200 OK
- [ ] ✅ Frontend loads without errors
- [ ] ✅ Login/Register pages display correctly
- [ ] ✅ New PiZOO branding visible (Classic Orange logo)
- [ ] ✅ SPA routes work (no 404s)
- [ ] ✅ API calls succeed (check Network tab)
- [ ] ✅ Database queries work (test login/register)
- [ ] ✅ LiveKit video calls work (if enabled)
- [ ] ✅ Image uploads work (Cloudinary)
- [ ] ✅ Email sending works (SMTP)
- [ ] ✅ No console errors
- [ ] ✅ No server errors in logs

---

## 🔗 Important Links

### Repository:
- **GitHub:** https://github.com/Shatha-db/Pizooo

### Documentation:
- **Backend .env.example:** `/app/backend/.env.example`
- **Frontend .env.example:** `/app/frontend/.env.example`
- **Deployment Guide:** This file

### Support:
- **Emergent Docs:** https://docs.emergent.sh
- **MongoDB Atlas:** https://cloud.mongodb.com
- **LiveKit Docs:** https://docs.livekit.io

---

## 🔐 Security Notes

### ✅ Security Best Practices Implemented:

1. **No secrets in repository:**
   - All `.env` files excluded via `.gitignore`
   - Only `.env.example` files with placeholders

2. **Environment variable injection:**
   - All secrets loaded from deployment platform
   - No hardcoded credentials

3. **CORS protection:**
   - Configured to allow only specific origins
   - Set via `CORS_ORIGINS` environment variable

4. **MongoDB Atlas:**
   - Connection string in environment only
   - IP whitelist configured in Atlas

5. **API keys:**
   - LiveKit, Cloudinary, SMTP keys in environment
   - Never committed to repository

---

## 📞 Next Steps

### After First Successful Deployment:

1. **Test thoroughly:**
   - All user flows (signup, login, profile, calls)
   - All API endpoints
   - All integrations (LiveKit, Cloudinary, Email)

2. **Monitor logs:**
   - Check for any errors or warnings
   - Monitor performance metrics
   - Watch database connection status

3. **Set up custom domain (optional):**
   - Configure DNS to point to Emergent deployment
   - Update `CORS_ORIGINS` and `FRONTEND_URL`
   - Redeploy with new settings

4. **Enable monitoring:**
   - Set up Sentry for error tracking
   - Configure uptime monitoring
   - Set up alerts for failures

5. **Optimize:**
   - Review and optimize database queries
   - Configure CDN for static assets
   - Enable caching where appropriate

---

## 📊 Summary

### What Was Fixed:
- ✅ Removed hardcoded fallback URL in `LiveKitCall.jsx`
- ✅ Ensured all configuration comes from environment variables
- ✅ Verified no `.env` files in repository (security)
- ✅ Confirmed MongoDB compatibility
- ✅ Verified CORS configuration

### Deployment Status:
- ✅ **Backend:** Ready (FastAPI + MongoDB)
- ✅ **Frontend:** Ready (React + Environment vars)
- ✅ **Database:** Ready (MongoDB Atlas compatible)
- ✅ **Integrations:** Ready (LiveKit, Cloudinary, SMTP)

### Required Actions:
1. Set all environment variables in Emergent dashboard
2. Deploy to Emergent platform
3. Verify deployment success
4. Test all functionality

---

**Guide Status:** ✅ COMPLETE  
**Application Status:** ✅ DEPLOYMENT READY  
**Next Action:** Deploy to Emergent with environment variables

---

*End of Guide*
