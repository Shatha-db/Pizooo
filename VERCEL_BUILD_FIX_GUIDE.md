# 🔧 Vercel Build Configuration Fix Guide

**Project:** Pizooo  
**Repository:** Shatha-db/Pizooo  
**Branch:** main  
**Date:** November 7, 2025, 17:20 UTC

---

## ✅ STEP 1: Project Structure Verified

### Frontend Location:
```
/app/frontend/
├── package.json ✅ (3.8 KB)
├── src/
├── public/
└── (build/ will be created during deployment)
```

### Package.json Scripts:
```json
{
  "scripts": {
    "start": "craco start",
    "build": "craco build",  ✅
    "test": "craco test"
  }
}
```

✅ **Build script exists and uses CRACO (Create React App Configuration Override)**

### Build Configuration Files:
- ✅ `/vercel.json` - Present with correct settings
- ✅ `/.vercelignore` - Present (with minor optimization needed)
- ✅ `/frontend/package.json` - Present with dependencies
- ✅ `/.gitignore` - Present and correct

---

## 🎯 STEP 2: Correct Vercel Configuration

### ⚠️ IMPORTANT: You Must Update Settings Manually

I cannot access Vercel Dashboard, so **YOU** must apply these settings.

---

### **Option A: Root Directory at Repository Root (Recommended)**

This matches your current `vercel.json` configuration.

**Settings to Apply in Vercel Dashboard:**

1. **Go to:** https://vercel.com/dashboard
2. **Select project:** `pizoo` (or `Pizooo`)
3. **Go to:** Settings → General

**Configure as follows:**

```
Framework Preset: Create React App
Root Directory: (leave EMPTY or set to "/")
Build Command: cd frontend && yarn install && yarn build
Output Directory: frontend/build
Install Command: cd frontend && yarn install
Node.js Version: 20.x (recommended)
```

**Why this works:**
- Root directory is repository root
- Build command navigates to `frontend/` folder
- Output is at `frontend/build/` relative to root
- Matches `vercel.json` configuration

---

### **Option B: Root Directory Set to Frontend (Alternative)**

If you prefer to set frontend as root (simpler commands):

**Settings to Apply:**

```
Framework Preset: Create React App
Root Directory: frontend
Build Command: yarn build
Output Directory: build
Install Command: yarn install
Node.js Version: 20.x
```

**Why this works:**
- Vercel operates inside `frontend/` folder
- Simpler build command (just `yarn build`)
- Output is at `build/` relative to frontend folder
- More standard CRA setup

**⚠️ Note:** If you choose Option B, you may need to update `vercel.json` to match, or delete it.

---

## 📋 STEP 3: Apply Settings in Vercel Dashboard

### Detailed Instructions:

1. **Log in to Vercel:**
   - https://vercel.com/dashboard

2. **Select Your Project:**
   - Find `pizoo` in your project list
   - Click to open

3. **Navigate to Settings:**
   - Click **"Settings"** tab at top

4. **Update General Settings:**
   - Click **"General"** in left sidebar

5. **Update Build Settings:**
   - Scroll to **"Build & Development Settings"**
   - Update each field as per Option A or B above
   - Click **"Save"** after each change

6. **Verify Git Connection:**
   - Click **"Git"** in left sidebar
   - Verify: Repository = `Shatha-db/Pizooo`
   - Verify: Production Branch = `main`
   - If wrong, disconnect and reconnect

7. **Check Environment Variables:**
   - Click **"Environment Variables"** in left sidebar
   - Ensure all required variables are present (see list below)

---

## 🔐 STEP 4: Environment Variables Checklist

### Required Variables (Add if Missing):

**Backend/Database:**
```
MONGO_URL=<your-mongodb-connection-string>
DB_NAME=pizoo_database
MONGODB_URI=<your-mongodb-uri>
MONGODB_DB_NAME=pizoo_database
```

**LiveKit (Video/Audio):**
```
LIVEKIT_URL=wss://your-livekit-url.livekit.cloud
LIVEKIT_API_KEY=<your-key>
LIVEKIT_API_SECRET=<your-secret>
```

**Cloudinary (Images):**
```
CLOUDINARY_CLOUD_NAME=<your-cloud-name>
CLOUDINARY_API_KEY=<your-key>
CLOUDINARY_API_SECRET=<your-secret>
CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
```

**Application URLs:**
```
FRONTEND_URL=https://pizoo.ch
CORS_ORIGINS=https://pizoo.ch,https://www.pizoo.ch
```

**Email Configuration:**
```
EMAIL_FROM="info Pizoo <support@pizoo.ch>"
EMAIL_FROM_NAME=info Pizoo
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=<your-email>
SMTP_PASS=<your-smtp-password>
EMAIL_MODE=smtp
```

**Security:**
```
SECRET_KEY=<generate-secure-random-key>
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
JWT_REFRESH_TOKEN_EXPIRE_DAYS=7
```

**reCAPTCHA (if used):**
```
RECAPTCHA_SITE_KEY=<your-site-key>
RECAPTCHA_SECRET_KEY=<your-secret-key>
```

**Feature Flags:**
```
ENABLE_EMAIL_VERIFICATION=true
ENABLE_VIDEO_CALLS=true
```

---

## 🚀 STEP 5: Trigger Fresh Redeploy

### Method 1: Via Dashboard (Recommended)

1. **Go to Deployments Tab:**
   - In your Vercel project, click **"Deployments"**

2. **Find Latest Deployment:**
   - Should be at the top of the list

3. **Click "..." Menu:**
   - On the right side of the deployment

4. **Select "Redeploy"**

5. **⚠️ IMPORTANT - Uncheck Cache:**
   - **Uncheck** "Use existing Build Cache"
   - This forces a fresh build from new repository

6. **Click "Redeploy"**

7. **Monitor Build:**
   - Click on the new deployment
   - Watch build logs in real-time
   - Look for: "Building from Shatha-db/Pizooo@main"

---

### Method 2: Via Deploy Hook (Alternative)

If you prefer using the deploy hook:

```bash
curl -X POST "https://api.vercel.com/v1/integrations/deploy/prj_8ZKPw4z3kOreyIVPywFD4OE3EdxJ/U5PhQBkXIx"
```

**Note:** This will use existing cache. For fresh build, use Dashboard method.

---

## 🔍 STEP 6: Verify Deployment Success

### A. Monitor Build Logs

1. **While deployment is running:**
   - Click on the deployment in progress
   - Watch "Building" tab

2. **Look for these indicators:**
   ```
   ✅ "Building from Shatha-db/Pizooo@main"
   ✅ "Installing dependencies: cd frontend && yarn install"
   ✅ "Building: cd frontend && yarn install && yarn build"
   ✅ "Compiled successfully"
   ✅ "Uploading build outputs..."
   ✅ "Deployment ready"
   ```

3. **Check for errors:**
   - Any red error messages
   - Build failures
   - Missing dependencies

---

### B. Verify Build Output

**In build logs, verify these files are included:**

```
frontend/build/
├── index.html ✅
├── static/
│   ├── css/
│   │   └── main.*.css ✅
│   ├── js/
│   │   └── main.*.js ✅
│   └── media/
│       ├── pizoo-classic.*.png ✅
│       └── pizoo-golden.*.png ✅
├── manifest.json ✅
└── favicon.ico ✅
```

---

### C. Test Production URLs

**After deployment shows "Ready":**

1. **Test main domain:**
   ```bash
   curl -I https://pizoo.ch
   ```
   - Expected: `HTTP/2 200 OK`
   - Check: `last-modified` header should be RECENT (after 17:20 UTC)

2. **Test WWW:**
   ```bash
   curl -I https://www.pizoo.ch
   ```
   - Expected: `HTTP/2 307` (redirect) or `200 OK`

3. **Test Vercel default:**
   ```bash
   curl -I https://pizoo.vercel.app
   ```
   - Expected: `HTTP/2 200 OK`

---

### D. Visual Verification

**Visit these URLs in browser:**

1. **Login Page:**
   - https://pizoo.ch/login
   - ✅ Should show NEW "PiZOO" Classic Orange logo
   - ❌ Should NOT show old yellow heart logo

2. **Register Page:**
   - https://pizoo.ch/register
   - ✅ Should show NEW "PiZOO" Classic Orange logo

3. **Home Page (after login):**
   - https://pizoo.ch/
   - ✅ Should show NEW "PiZOO" Golden Glow logo in navbar

4. **Test SPA routes:**
   - /terms
   - /privacy
   - /safety
   - All should load without 404 errors

---

## 📊 Expected Build Output

### Successful Build Log Example:

```
[Build]   > Building from Shatha-db/Pizooo@main
[Build]   Running build in /vercel/path0/frontend
[Build]   
[Build]   Installing dependencies: cd frontend && yarn install
[Build]   yarn install v1.22.22
[Build]   [1/4] Resolving packages...
[Build]   [2/4] Fetching packages...
[Build]   [3/4] Linking dependencies...
[Build]   [4/4] Building fresh packages...
[Build]   Done in 45.23s.
[Build]   
[Build]   Building: cd frontend && yarn install && yarn build
[Build]   yarn run v1.22.22
[Build]   $ craco build
[Build]   Creating an optimized production build...
[Build]   Compiled successfully.
[Build]   
[Build]   File sizes after gzip:
[Build]     421.56 kB  build/static/js/main.c9df4bfc.js
[Build]     25.72 kB   build/static/css/main.588aa498.css
[Build]   
[Build]   Done in 89.45s.
[Build]   
[Upload]  Uploading build outputs...
[Upload]  Uploaded 234 files (3.2 MB)
[Deploy]  Deployment complete
[Deploy]  URL: https://pizoo-abc123.vercel.app
```

**Key Metrics:**
- Install time: ~45 seconds
- Build time: ~90 seconds
- Total time: ~2-3 minutes
- Output size: ~3-4 MB

---

## ⚠️ Common Issues & Solutions

### Issue 1: "Command not found: yarn"

**Error in logs:**
```
sh: yarn: command not found
```

**Solution:**
- Install Command should be: `yarn install`
- Or change to: `npm install`
- Update build command to use `npm run build` if using npm

---

### Issue 2: "Cannot find module 'craco'"

**Error in logs:**
```
Error: Cannot find module '@craco/craco'
```

**Solution:**
- Ensure `@craco/craco` is in `package.json` dependencies
- Clear cache and rebuild
- Or update build command to use `react-scripts build`

---

### Issue 3: "Output directory not found"

**Error:**
```
Error: Could not find output directory "frontend/build"
```

**Solution:**
- Verify build command creates `frontend/build/` folder
- Check build logs for actual output location
- Update Output Directory setting to match

---

### Issue 4: "404 on all routes"

**Symptom:**
- Home page loads
- But /login, /register show 404

**Solution:**
- Verify `vercel.json` has rewrites:
  ```json
  {
    "rewrites": [
      { "source": "/(.*)", "destination": "/index.html" }
    ]
  }
  ```
- Or add in Vercel Dashboard under "Rewrites and Redirects"

---

### Issue 5: "Old branding still showing"

**Symptom:**
- Deployment succeeds
- But old yellow heart logo still visible

**Solutions:**
1. **Clear browser cache:**
   - Ctrl+Shift+R (hard refresh)
   - Or test in incognito mode

2. **Verify new repo:**
   - Check build logs: "Building from Shatha-db/Pizooo"
   - NOT from old repo

3. **Check build output:**
   - Search logs for "pizoo-classic.png"
   - Should be included in build

4. **Verify files deployed:**
   - Check deployment files in Vercel
   - `static/media/` should have new logos

---

## 📝 Configuration Comparison

### ❌ WRONG Configuration (Old):

```
Framework: Other
Root: (empty)
Build Command: yarn build
Output: build
```

**Problem:** Looking for build in wrong location (repo root instead of frontend/)

---

### ✅ CORRECT Configuration (Option A):

```
Framework: Create React App
Root: (empty or /)
Build Command: cd frontend && yarn install && yarn build
Output: frontend/build
Install: cd frontend && yarn install
```

**Why it works:** Commands navigate to frontend folder, output matches location

---

### ✅ CORRECT Configuration (Option B):

```
Framework: Create React App
Root: frontend
Build Command: yarn build
Output: build
Install: yarn install
```

**Why it works:** Root is frontend, so all commands run there

---

## 🎯 Post-Deployment Checklist

After deployment completes, verify:

- [ ] Build logs show "Shatha-db/Pizooo@main"
- [ ] Build completed successfully (no errors)
- [ ] `https://pizoo.ch` returns 200 OK
- [ ] `last-modified` header is recent (after config changes)
- [ ] Login page shows NEW PiZOO Classic Orange logo
- [ ] NO old yellow heart logo visible
- [ ] Register page shows NEW logo
- [ ] SPA routes work (/login, /register, /terms, etc.)
- [ ] No 404 errors on navigation
- [ ] Console has no critical errors
- [ ] Images load correctly

---

## 📞 What to Tell AI Agent After Deployment

Once you complete all steps and deployment is successful:

**Message:** "Vercel reconfigured and deployed successfully"

**AI Agent will then:**
1. ✅ Verify deployment timestamp
2. ✅ Test all domains
3. ✅ Take screenshots of new branding
4. ✅ Verify SPA routes
5. ✅ Generate final success report

---

## 🔗 Quick Links

- **Vercel Dashboard:** https://vercel.com/dashboard
- **GitHub Repo:** https://github.com/Shatha-db/Pizooo
- **Production URL:** https://pizoo.ch
- **WWW URL:** https://www.pizoo.ch
- **Vercel Default:** https://pizoo.vercel.app

---

## 📊 Summary

### Current Status:
- ✅ GitHub repo ready (Shatha-db/Pizooo)
- ✅ Frontend code in `/frontend` folder
- ✅ `vercel.json` configured correctly
- ⏳ Vercel Dashboard settings need update (manual)
- ⏳ Fresh redeploy needed (manual)

### Required Actions:
1. Update Vercel build settings (Option A or B)
2. Verify Git connection to new repo
3. Add/verify environment variables
4. Trigger fresh redeploy without cache
5. Verify new branding appears

### Expected Outcome:
- New PiZOO branding visible
- All domains working
- SPA routes functional
- No 404 errors
- Production-ready

---

**Guide Status:** ✅ COMPLETE  
**Next Action:** Apply settings in Vercel Dashboard and redeploy

---

*End of Guide*
