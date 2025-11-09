# Render Backend Deployment Fix - pizooo-backend

**Service:** pizooo-backend  
**Repository:** Shatha-db/Pizooo  
**Branch:** main  
**Status:** ✅ Code fixes applied, ready for deployment

---

## ✅ Fixes Applied

### 1. Removed Invalid Package
**File:** `/app/backend/requirements.txt`  
**Change:** Removed line 97: `emergentintegrations==0.1.0`  
**Reason:** Package not available in PyPI, causing build failures

**Status:** ✅ Fixed - package removed from requirements.txt

### 2. Verified Entry Point
**Entry Point:** `server:app`  
**File:** `/app/backend/server.py` (line 174: `app = FastAPI()`)  
**Status:** ✅ Correct - no changes needed

---

## 🚀 Deployment Steps (Manual - You Must Do These)

### Step 1: Push Code Changes to GitHub

1. Use Emergent **"Save to GitHub"** feature
2. **Repository:** `Shatha-db/Pizooo`
3. **Branch:** `main`
4. **Commit Message:**
   ```
   chore(backend): remove unavailable package emergentintegrations
   ```

### Step 2: Configure Render Service

#### A. Go to Render Dashboard

1. Navigate to: https://dashboard.render.com/
2. Select service: **`pizooo-backend`**

#### B. Verify/Update Build Settings

**Settings → Build & Deploy:**

| Setting | Value |
|---------|-------|
| **Root Directory** | `backend` |
| **Build Command** | `pip install -U pip && pip install -r requirements.txt` |
| **Start Command** | `uvicorn server:app --host 0.0.0.0 --port 10000` |

**Important Notes:**
- ✅ Entry point is `server:app` (verified in `/app/backend/server.py`)
- ❌ Do NOT use `app.main:app` (that's for different project structures)

#### C. Add/Verify Environment Variables

**Settings → Environment:**

| Key | Value | Required |
|-----|-------|----------|
| `PYTHON_VERSION` | `3.11.0` | ✅ Yes |
| `CORS_ORIGINS` | `https://pizoo.ch,https://www.pizoo.ch,https://pizooo.vercel.app` | ✅ Yes |
| `MONGO_URL` | `<your_mongodb_connection_string>` | ✅ Yes |
| `DB_NAME` | `pizoo_database` | ✅ Yes |
| `SECRET_KEY` | `<your_secret_key>` | ✅ Yes |
| `LIVEKIT_URL` | `<your_livekit_url>` | ⚠️ Optional |
| `LIVEKIT_API_KEY` | `<your_api_key>` | ⚠️ Optional |
| `LIVEKIT_API_SECRET` | `<your_api_secret>` | ⚠️ Optional |
| `CLOUDINARY_URL` | `<your_cloudinary_url>` | ⚠️ Optional |
| `EMAIL_MODE` | `mock` | ⚠️ Optional |
| `EMAIL_FROM` | `"info Pizoo <support@pizoo.ch>"` | ⚠️ Optional |
| `FRONTEND_URL` | `https://pizoo.ch` | ⚠️ Optional |

**Critical Variables:**
1. **`PYTHON_VERSION=3.11.0`** - Ensures correct Python version
2. **`CORS_ORIGINS`** - Allows frontend domains to access backend
3. **`MONGO_URL`** - Database connection (required)
4. **`SECRET_KEY`** - JWT token signing (required)

**How to Add:**
1. Click **"Add Environment Variable"**
2. Enter Key and Value
3. Click **"Save"**
4. Repeat for all required variables

### Step 3: Clear Build Cache & Deploy

1. Go to **Manual Deploy** section
2. Click **"Clear build cache & deploy"**
3. Wait for deployment (typically 3-5 minutes)

**Monitor Progress:**
- Click on the deployment to see live logs
- Watch for "Build succeeded" message
- Then watch for "Starting service"

### Step 4: Verify Deployment

Once deployment shows **"Live"**, verify:

#### A. Test Swagger UI (API Documentation)

```bash
# Open in browser or curl:
curl https://pizooo-backend.onrender.com/docs
```

**Expected:** Swagger UI loads with FastAPI documentation

#### B. Test Health Endpoint (if available)

```bash
curl https://pizooo-backend.onrender.com/
```

**Expected:** Returns welcome message or 200 OK

#### C. Test CORS Headers

```bash
curl -I https://pizooo-backend.onrender.com/api/auth/login \
  -H "Origin: https://pizoo.ch"
```

**Expected Headers:**
```
Access-Control-Allow-Origin: https://pizoo.ch
Access-Control-Allow-Credentials: true
```

#### D. Test Basic Auth Endpoint

```bash
curl -X POST https://pizooo-backend.onrender.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

**Expected:** Returns JSON response (401 if user doesn't exist, which is normal)

---

## 🔍 Troubleshooting

### Issue 1: Build Fails with "Package not found"

**Error:** `ERROR: Could not find a version that satisfies the requirement emergentintegrations`

**Solution:**
1. ✅ Already fixed - package removed from requirements.txt
2. If error persists, ensure GitHub has the updated requirements.txt
3. Clear build cache in Render and redeploy

### Issue 2: Import Error on Startup

**Error:** `ModuleNotFoundError: No module named 'emergentintegrations'`

**Check:**
```bash
# Search for imports in backend code
grep -r "from emergentintegrations" /app/backend/
grep -r "import emergentintegrations" /app/backend/
```

**Solution:**
- ✅ Already verified - no code references found
- If found, remove those import statements

### Issue 3: Python Version Mismatch

**Error:** `Python version X.X not supported`

**Solution:**
1. Add environment variable: `PYTHON_VERSION=3.11.0`
2. Redeploy

### Issue 4: CORS Errors from Frontend

**Error:** `Access to XMLHttpRequest blocked by CORS policy`

**Solution:**
1. Verify `CORS_ORIGINS` environment variable includes:
   ```
   https://pizoo.ch,https://www.pizoo.ch,https://pizooo.vercel.app
   ```
2. No spaces after commas
3. Redeploy after adding

### Issue 5: Database Connection Failed

**Error:** `ServerSelectionTimeoutError: No servers found`

**Solution:**
1. Check `MONGO_URL` is correct
2. Verify MongoDB allows connections from Render IP addresses
3. Check MongoDB Atlas → Network Access → Add Render IPs

### Issue 6: Wrong Entry Point

**Error:** `Error loading ASGI app. Import string "app.main:app" doesn't match pattern`

**Solution:**
- ✅ Entry point verified: `server:app` is correct
- Do NOT change to `app.main:app`
- File structure: `/app/backend/server.py` contains `app = FastAPI()`

---

## 📋 Pre-Deployment Checklist

- [x] Removed `emergentintegrations==0.1.0` from requirements.txt
- [ ] Pushed changes to GitHub repository `Shatha-db/Pizooo`
- [ ] Verified Render service name: `pizooo-backend`
- [ ] Set Root Directory: `backend`
- [ ] Set Build Command: `pip install -U pip && pip install -r requirements.txt`
- [ ] Set Start Command: `uvicorn server:app --host 0.0.0.0 --port 10000`
- [ ] Added `PYTHON_VERSION=3.11.0` environment variable
- [ ] Added `CORS_ORIGINS` environment variable
- [ ] Verified `MONGO_URL` is set
- [ ] Verified `SECRET_KEY` is set
- [ ] Cleared build cache
- [ ] Triggered manual deploy

---

## 📊 Expected Deployment Timeline

| Step | Duration | Status |
|------|----------|--------|
| Code push to GitHub | 1 minute | ⏳ Pending |
| Render detects changes | 1 minute | ⏳ Pending |
| Build starts | Immediate | ⏳ Pending |
| Dependencies install | 2-3 minutes | ⏳ Pending |
| Service starts | 30 seconds | ⏳ Pending |
| Health check passes | 30 seconds | ⏳ Pending |
| **Total** | **5-6 minutes** | ⏳ Pending |

---

## ✅ Success Indicators

### Build Logs Should Show:

```bash
==> Building...
==> Installing dependencies
Successfully installed fastapi-0.110.1 uvicorn-0.25.0 ...
==> Build succeeded 🎉

==> Starting service with 'uvicorn server:app --host 0.0.0.0 --port 10000'
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:10000
```

### Service Status:
- **Status:** Live ✅
- **Health Check:** Passing ✅
- **Last Deploy:** [Current timestamp]
- **Deploy Time:** ~5 minutes

### Backend URL:
- **Swagger UI:** https://pizooo-backend.onrender.com/docs (200 OK)
- **API Endpoints:** https://pizooo-backend.onrender.com/api/* (Responding)

---

## 🔗 Integration with Frontend

### Vercel Frontend Configuration

After backend is live, ensure Vercel has correct environment variable:

**Vercel Project:** `pizooo`  
**Environment Variable:**
```
REACT_APP_BACKEND_URL=https://pizooo-backend.onrender.com
```

**Important:** NO trailing slash!

### Test Frontend → Backend Connection

1. Deploy frontend to Vercel
2. Open: https://pizoo.ch/login
3. Try to login (should get response from backend, even if 401)
4. Check DevTools Console - no CORS errors

---

## 📞 Support Resources

### Render Documentation
- **Python Deployment:** https://render.com/docs/deploy-python
- **Environment Variables:** https://render.com/docs/environment-variables
- **Build & Deploy:** https://render.com/docs/deploys

### Render Dashboard
- **Service URL:** https://dashboard.render.com/web/pizooo-backend
- **Logs:** Click on service → Logs tab
- **Events:** Click on service → Events tab

### Local Files
- **Requirements:** `/app/backend/requirements.txt` (97 lines, updated)
- **Server Entry:** `/app/backend/server.py` (line 174: `app = FastAPI()`)
- **This Guide:** `/app/RENDER_DEPLOYMENT_FIX.md`

---

## 🎯 Quick Command Reference

### Test Backend After Deploy

```bash
# Test Swagger UI
curl https://pizooo-backend.onrender.com/docs

# Test CORS
curl -I https://pizooo-backend.onrender.com/api/auth/login \
  -H "Origin: https://pizoo.ch"

# Test Auth Endpoint
curl -X POST https://pizooo-backend.onrender.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"test123"}'

# Check Health (if endpoint exists)
curl https://pizooo-backend.onrender.com/
```

### Monitor Logs

```bash
# In Render Dashboard:
# Service → Logs → View live logs
```

---

## 📈 Deployment History

| Date | Change | Status |
|------|--------|--------|
| 2025-11-09 | Removed emergentintegrations package | ✅ Fixed |
| 2025-11-09 | Verified entry point server:app | ✅ Correct |
| 2025-11-09 | Documented environment variables | ✅ Complete |

---

**Status:** ✅ Code fixes complete - Ready for manual deployment on Render  
**Next Action:** Push to GitHub → Configure Render → Deploy  
**ETA:** 5-6 minutes after triggering deploy
