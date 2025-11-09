# Deployment Quick Reference Card

## 🎯 Quick Setup (15 minutes)

### 1️⃣ GitHub (2 min)
```
✓ Save to GitHub → Shatha-db/Pizooo → main
✓ Commit: "chore(backend): remove emergentintegrations pkg and update CORS"
```

### 2️⃣ Render Backend (8 min)

**A. Environment Variables:**
```bash
PYTHON_VERSION=3.11.0
CORS_ORIGINS=https://pizoo.com,https://pizoo.ch,https://www.pizoo.ch,https://pizooo-backend.onrender.com
MONGO_URL=<your_mongodb_connection>
DB_NAME=pizoo_database
SECRET_KEY=<your_secret>
```

**B. Build Settings:**
```
Root: backend
Build: pip install --upgrade pip && pip install -r requirements.txt
Start: uvicorn server:app --host 0.0.0.0 --port 10000
```

**C. Deploy:**
```
Clear cache → Deploy → Wait ~5 min
```

### 3️⃣ Vercel Frontend (3 min)

**A. Environment Variable:**
```bash
REACT_APP_BACKEND_URL=https://pizooo-backend.onrender.com
# Apply to: Production, Preview, Development
```

**B. Deploy:**
```
Redeploy → Clear cache → Wait ~2 min
```

### 4️⃣ Verify (2 min)

**Backend:**
```bash
curl https://pizooo-backend.onrender.com/docs
# Expected: HTML (200 OK)
```

**Frontend:**
```bash
curl -I https://pizoo.ch/login
# Expected: 200 OK
```

**Integration:**
```
1. Open https://pizoo.ch/login
2. Try to sign in
3. Check Network tab → POST to pizooo-backend.onrender.com
4. No CORS errors in Console
```

---

## 🔍 Quick Tests

### Backend Health
```bash
# Swagger UI
open https://pizooo-backend.onrender.com/docs

# CORS
curl -I https://pizooo-backend.onrender.com/api/auth/login \
  -H "Origin: https://pizoo.ch"
```

### Frontend Health
```bash
# Homepage
open https://pizoo.ch

# Login
open https://pizoo.ch/login
```

### Network Check
```javascript
// In browser console on pizoo.ch:
fetch('https://pizooo-backend.onrender.com/api/auth/login', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({email:'test@test.com',password:'test'})
}).then(r => console.log('Status:', r.status))
```

---

## ⚠️ Common Issues

| Issue | Solution |
|-------|----------|
| Package not found | ✅ Fixed - already removed |
| CORS error | Check CORS_ORIGINS (no spaces!) |
| Wrong backend URL | Check REACT_APP_BACKEND_URL |
| Double slash | ✅ Fixed - centralized config |
| 502 Gateway | Check Render logs, verify MONGO_URL |

---

## 📋 Checklist

**Backend:**
- [ ] Code pushed to GitHub
- [ ] PYTHON_VERSION=3.11.0 set
- [ ] CORS_ORIGINS set (4 domains)
- [ ] MONGO_URL configured
- [ ] Build cache cleared
- [ ] Deploy triggered
- [ ] Status: Live ✅
- [ ] /docs returns 200

**Frontend:**
- [ ] REACT_APP_BACKEND_URL set
- [ ] Applied to all environments
- [ ] Redeployed
- [ ] Status: Ready ✅
- [ ] Homepage loads
- [ ] No CORS errors

**Integration:**
- [ ] Sign up form works
- [ ] Sign in form works
- [ ] Network shows correct URL
- [ ] No console errors

---

## 🎯 Success Indicators

✅ Backend: https://pizooo-backend.onrender.com/docs (200 OK)  
✅ Frontend: https://pizoo.ch (200 OK)  
✅ API calls: Backend URL correct in Network tab  
✅ CORS: No errors in Console  
✅ Auth: Forms submit successfully  

---

**Total Time:** ~15 minutes  
**Full Guide:** `/app/FINAL_DEPLOYMENT_GUIDE.md`
