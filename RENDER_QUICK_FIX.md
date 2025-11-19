# Render Backend - Quick Fix Checklist

## ✅ What I've Done (Automated)

1. **✅ Removed Invalid Package**
   - File: `backend/requirements.txt`
   - Removed: `emergentintegrations==0.1.0` (line 97)
   - Verified: No code references to this package

2. **✅ Verified Entry Point**
   - Entry: `server:app` ✅ Correct
   - File: `backend/server.py` (line 174: `app = FastAPI()`)

3. **✅ Created Documentation**
   - Full guide: `/app/RENDER_DEPLOYMENT_FIX.md`
   - This checklist: `/app/RENDER_QUICK_FIX.md`

---

## 🎯 What You Must Do (Manual - 10 minutes)

### Step 1: Push to GitHub (2 min)
```
1. Click "Save to GitHub" in Emergent
2. Repository: Shatha-db/Pizooo
3. Branch: main
4. Commit: "chore(backend): remove unavailable package emergentintegrations"
```

### Step 2: Configure Render (5 min)

**A. Build Settings (verify/update):**
- Root Directory: `backend`
- Build Command: `pip install -U pip && pip install -r requirements.txt`
- Start Command: `uvicorn server:app --host 0.0.0.0 --port 10000`

**B. Environment Variables (add if missing):**
```
PYTHON_VERSION=3.11.0
CORS_ORIGINS=https://pizoo.ch,https://www.pizoo.ch,https://pizooo.vercel.app
MONGO_URL=<your_mongodb_connection>
DB_NAME=pizoo_database
SECRET_KEY=<your_secret>
```

### Step 3: Deploy (3 min)
```
1. Go to Render Dashboard → pizooo-backend
2. Click "Clear build cache & deploy"
3. Wait for "Live" status (~5 min)
```

### Step 4: Verify (1 min)
```bash
# Test Swagger UI
curl https://pizooo-backend.onrender.com/docs
# Should return HTML

# Test CORS
curl -I https://pizooo-backend.onrender.com/api/auth/login \
  -H "Origin: https://pizoo.ch"
# Should show Access-Control-Allow-Origin header
```

---

## ⚠️ Common Issues

### Issue: "Package not found"
✅ Fixed - package removed from requirements.txt

### Issue: Wrong entry point
✅ Correct - use `server:app` (NOT `app.main:app`)

### Issue: CORS errors
✅ Add CORS_ORIGINS environment variable with all domains

### Issue: Python version
✅ Add PYTHON_VERSION=3.11.0 environment variable

---

## 🎯 Expected Result

**Build Logs:**
```
==> Installing dependencies
Successfully installed 96 packages
==> Build succeeded 🎉
==> Starting service
INFO: Uvicorn running on http://0.0.0.0:10000
```

**Service Status:**
- Status: Live ✅
- URL: https://pizooo-backend.onrender.com
- Swagger: https://pizooo-backend.onrender.com/docs

---

## 📞 Need Help?

**Full Guide:** `/app/RENDER_DEPLOYMENT_FIX.md`  
**Render Dashboard:** https://dashboard.render.com/  
**Service:** pizooo-backend

---

**Total Time:** ~10 minutes  
**Status:** Ready to deploy 🚀
