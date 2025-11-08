# Deployment Verification Checklist

After deploying to Vercel, verify these items:

## 1. Visual Check
- [ ] Visit: https://pizoo.ch/login
- [ ] Logo displays: Classic Orange PiZOO (no white background)
- [ ] Page loads without errors

## 2. Network Check (Browser DevTools)
Open Developer Tools (F12) → Network tab:

- [ ] Try to login or register
- [ ] API calls show: `https://pizooo-backend.onrender.com/api/auth/login`
- [ ] NO double slashes: `//api/` ❌
- [ ] Single slash only: `/api/` ✅

## 3. CORS Check
In Browser Console (F12):

- [ ] NO CORS errors showing
- [ ] Authentication requests succeed
- [ ] Response headers include: `Access-Control-Allow-Origin: https://pizoo.ch`

## 4. Backend Health Check
Test backend CORS directly:

```bash
curl -I https://pizooo-backend.onrender.com/api/auth/login \
  -H "Origin: https://pizoo.ch"
```

Should return:
```
Access-Control-Allow-Origin: https://pizoo.ch
Access-Control-Allow-Credentials: true
```

## 5. Functional Test
- [ ] Register new account → Should work without CORS errors
- [ ] Login with existing account → Should work without CORS errors
- [ ] Navigation between pages → No console errors

## Troubleshooting

### If CORS errors persist:
1. Check Render backend environment variables include:
   ```
   CORS_ORIGINS=https://pizoo.ch,https://www.pizoo.ch,https://pizooo.vercel.app
   ```
2. Redeploy Render backend with "Clear build cache"

### If double-slash persists:
1. Check Vercel environment variable has NO trailing slash:
   ```
   REACT_APP_BACKEND_URL=https://pizooo-backend.onrender.com
   ```
   NOT: `https://pizooo-backend.onrender.com/` ❌
2. Redeploy Vercel with cache cleared

### If old logo shows:
1. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. Clear browser cache
3. Check Vercel deployment timestamp matches your latest commit

## Success Criteria
✅ All checkboxes marked
✅ No CORS errors in console
✅ Login/Register working
✅ New PiZOO branding visible
✅ API URLs have single slash only
