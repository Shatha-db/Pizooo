# ⚡ خطوات النشر السريعة - نظام Pizoo

## 🎯 الهدف النهائي

```
pizoo.ch         → موقع التسويق ✨
app.pizoo.ch     → التطبيق الرئيسي 📱
```

---

## 📦 المشروع 1: موقع التسويق (15 دقيقة)

### الخيار A: رفع ZIP (الأسرع)

1. **حمّل الملف:**
   ```
   https://pizoo-landing.preview.emergentagent.com/api/download/marketing-website
   ```

2. **في Vercel:**
   - اذهب: https://vercel.com
   - "Add New" → "Project"
   - ارفع ZIP
   - Project Name: `pizoo-marketing`
   - Framework: Create React App
   - Output Directory: `build`
   - Deploy! ✅

3. **أضف النطاق:**
   - Settings → Domains
   - أضف: `pizoo.ch`

---

### الخيار B: عبر GitHub

1. **ربط Repository:**
   - "Add New" → "Project"
   - اختر: `Shatha-db/Pizooo`
   - Root Directory: `marketing-website`

2. **إعدادات:**
   ```
   Build: yarn build
   Output: build
   Install: yarn install
   ```

3. **أضف النطاق:**
   - Settings → Domains
   - أضف: `pizoo.ch`

---

## 📱 المشروع 2: التطبيق الرئيسي (15 دقيقة)

### عبر GitHub (فقط)

1. **في Vercel:**
   - "Add New" → "Project"
   - اختر: `Shatha-db/Pizooo`
   - Root Directory: `frontend`

2. **إعدادات:**
   ```
   Project Name: pizoo-app
   Build: yarn build
   Output: build
   Install: yarn install
   ```

3. **⚠️ Environment Variable (مهم!):**
   ```
   REACT_APP_BACKEND_URL=https://pizoo-landing.preview.emergentagent.com
   ```
   - أضفها في: Settings → Environment Variables

4. **أضف النطاق:**
   - Settings → Domains
   - أضف: `app.pizoo.ch`

---

## 🌐 إعداد DNS (15-30 دقيقة)

### في مزود النطاق الخاص بك:

**الطريقة الموصى بها:**
غيّر Nameservers إلى:
```
ns1.vercel-dns.com
ns2.vercel-dns.com
```

✅ **الميزة:** Vercel تدير كل شيء تلقائياً

---

## ⏳ الانتظار

- عادةً: 15-30 دقيقة
- تحقق من: https://dnschecker.org

---

## ✅ الاختبار النهائي

```
1. افتح: https://pizoo.ch
   → يجب أن ترى: موقع التسويق ✨

2. افتح: https://app.pizoo.ch
   → يجب أن ترى: صفحة Login 📱

3. تحقق من القفل 🔒 في كلاهما
```

---

## 🆘 مساعدة سريعة

**Build فشل؟**
→ تحقق من Logs في Vercel

**النطاق لا يعمل؟**
→ انتظر 24 ساعة أو تحقق من DNS

**SSL لا يعمل؟**
→ انتظر 10 دقائق أو انقر "Renew Certificate"

---

## 📞 أحتاج مساعدة!

أخبرني:
- في أي خطوة أنت؟
- ما الخطأ المحدد؟

سأساعدك فوراً! 😊
