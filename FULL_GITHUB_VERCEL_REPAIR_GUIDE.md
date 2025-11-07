# 🔧 FULL GITHUB + VERCEL REPAIR & CONSOLIDATION GUIDE
**Repository:** Shatha-db/pizoo-dating-app  
**Goal:** ONE unified app, ONE repo, ONE branch (main), ONE Vercel project  
**Date:** November 7, 2025, 15:37 UTC

---

## 🎯 MISSION OBJECTIVE

**Consolidate everything under:**
- ✅ **Repository:** `Shatha-db/pizoo-dating-app`
- ✅ **Branch:** `main` (single source of truth)
- ✅ **Vercel Project:** `pizoo`
- ✅ **Domains:** pizoo.ch, www.pizoo.ch, pizoo.vercel.app

**Remove/Archive:**
- 🗑️ Old repos: `pizoo`, `pizoo-subscription`, `pizoo-dating-app-final`
- 🗑️ Old branches: All `conflict_*`, `chore/*` (after backup)
- 🗑️ Duplicate Vercel projects (if any)

---

## ⚠️ SYSTEM LIMITATIONS

### AI Agent CANNOT Do:
- ❌ Git push to GitHub
- ❌ Create/merge pull requests on GitHub
- ❌ Delete remote branches
- ❌ Archive GitHub repositories
- ❌ Modify GitHub Actions permissions
- ❌ Access Vercel Dashboard
- ❌ Change DNS records

### AI Agent CAN Do:
- ✅ Read GitHub status (API)
- ✅ Create local backups
- ✅ Analyze code and configs
- ✅ Trigger Vercel deploy hooks
- ✅ Verify domains (curl)
- ✅ Generate comprehensive reports
- ✅ **Provide step-by-step commands for YOU to execute**

---

## 📋 PRECHECKS STATUS

| Check | Status | Notes |
|-------|--------|-------|
| **GitHub API Access** | ✅ Working | Rate limit: 58/60 |
| **Default Branch** | ✅ `main` | Correct |
| **Branch Protection** | ✅ Disabled | Easy to merge |
| **Open PRs** | ✅ None | Clean state |
| **Total Branches** | ⚠️ 12 | Need cleanup |
| **Repos to Archive** | ⚠️ 3 found | pizoo, pizoo-subscription, pizoo-dating-app-final |
| **Local Backup** | ✅ Created | backup/pre-consolidation-20251107-1537-main |

---

## 🚀 PHASE 1: GITHUB REPO AUDIT & MERGE

### Current Branch Status on GitHub:

#### Active Branches (12 total):
1. ✅ **main** - Target production branch
2. 🧹 `chore/monorepo-merge` - Can be deleted after review
3. 🧹 `chore/test-vercel-deploy` - Can be deleted after review
4. 🗑️ `conflict_021125_1024` - Old, to delete
5. 🗑️ `conflict_041125_1150` - Old, to delete
6. 🗑️ `conflict_041125_1944` - Old, to delete
7. ⚠️ **`conflict_071125_1347`** - **LATEST updates! Must merge first**
8. 🗑️ `conflict_311025_1520` - Old, to delete
9. 🗑️ `conflict_311025_2149` - Old, to delete
10. 🗑️ `conflict_311025_2340` - Old, to delete
11. 🔧 `fix/eslint-webpack-compat` - Keep if work in progress
12. 🔧 `fix/urls-cors-env` - Keep if work in progress

### ⚠️ **CRITICAL: Latest Updates Location**

**Branch `conflict_071125_1347` contains:**
- ✅ New PiZOO branding (Classic Orange + Golden logos)
- ✅ vercel.json configuration
- ✅ PizooLogo React components
- ✅ Email standardization (support@pizoo.ch)
- ✅ All recent fixes

**This MUST be merged to `main` before anything else!**

---

### 🔴 **STEP 1.1: Create Backup Tags on GitHub**

**Why:** Prevent data loss before merging

**You Must Do:**
```bash
# On your local machine with GitHub access:
git clone https://github.com/Shatha-db/pizoo-dating-app.git
cd pizoo-dating-app

# Create backup tags for important branches
UTC_NOW=$(date -u +"%Y%m%d-%H%M")

git checkout main
git tag "backup/main-${UTC_NOW}"

git checkout conflict_071125_1347
git tag "backup/conflict_071125_1347-${UTC_NOW}"

# Push tags to GitHub
git push origin --tags

# Verify
git tag | grep backup
```

**Expected Output:**
```
backup/main-20251107-1537
backup/conflict_071125_1347-20251107-1537
```

---

### 🔴 **STEP 1.2: Merge Latest Branch to Main**

**Option A: Via GitHub UI (Recommended)**

1. Go to: https://github.com/Shatha-db/pizoo-dating-app/compare/main...conflict_071125_1347

2. Click **"Create pull request"**

3. Title: `Merge latest updates from conflict_071125_1347`

4. Review changes (should show):
   - ✅ vercel.json
   - ✅ New logo files (pizoo-classic.png, pizoo-golden.png)
   - ✅ PizooLogo.jsx, Wordmark.jsx, GoldenLogo.jsx
   - ✅ Email updates in backend

5. Click **"Create pull request"** → **"Merge pull request"**

6. Choose **"Create a merge commit"** (preserve history)

7. Click **"Confirm merge"**

8. ✅ **Done!** Main now has latest code

**Option B: Via Git CLI**

```bash
cd pizoo-dating-app
git checkout main
git pull origin main

# Merge with history preservation
git merge conflict_071125_1347 --no-ff -m "Merge: Consolidate latest branding and config"

# If conflicts occur:
# 1. Resolve them manually (prioritize conflict_071125_1347 content)
# 2. git add .
# 3. git commit -m "Resolve merge conflicts"

# Push to GitHub
git push origin main
```

**Verification:**
```bash
# Check that vercel.json exists
curl -s "https://api.github.com/repos/Shatha-db/pizoo-dating-app/contents/vercel.json?ref=main" | grep '"name"'

# Should output: "name": "vercel.json"
```

---

### 🔴 **STEP 1.3: Push Local Workspace to Main (Alternative)**

If merge is too complex, use Emergent's "Save to GitHub":

1. In Emergent chat interface, click **"Save to GitHub"**
2. Select:
   - Repository: `Shatha-db/pizoo-dating-app`
   - Branch: Try `main` (or create new branch then merge via GitHub UI)
3. Click **"PUSH TO GITHUB"**

---

### 🔴 **STEP 1.4: Delete Obsolete Branches**

**⚠️ Only after Step 1.2 is complete and verified!**

Go to: https://github.com/Shatha-db/pizoo-dating-app/branches

Delete these branches (click 🗑️ icon):

**Safe to delete immediately:**
```
conflict_021125_1024
conflict_041125_1150
conflict_041125_1944
conflict_311025_1520
conflict_311025_2149
conflict_311025_2340
```

**Delete after confirming merge:**
```
conflict_071125_1347  (⚠️ Only AFTER confirming it's merged to main!)
```

**Review before deleting:**
```
chore/monorepo-merge        (check if work is complete)
chore/test-vercel-deploy    (likely obsolete)
```

**Keep for now (if active work):**
```
fix/eslint-webpack-compat
fix/urls-cors-env
```

**Final state:** Only `main` (+ any active dev branches)

---

## 🗄️ PHASE 2: CLEANUP OLD REPOS (Archive)

### Repositories to Archive:

1. **Shatha-db/pizoo**
2. **Shatha-db/pizoo-subscription**
3. **Shatha-db/pizoo-dating-app-final**

### 🔴 **STEP 2.1: Add Deprecation Notice**

For each old repo, create a README:

**Example: Shatha-db/pizoo**

1. Go to: https://github.com/Shatha-db/pizoo
2. Edit `README.md` (or create new)
3. Add at the top:

```markdown
# ⚠️ DEPRECATED - This Repository is Archived

**This project has been consolidated into:**

👉 **[Shatha-db/pizoo-dating-app](https://github.com/Shatha-db/pizoo-dating-app)**

All active development, issues, and contributions should go to the unified repository above.

**Status:** Archived on November 7, 2025  
**Reason:** Project consolidation to single source of truth

---

*Historical content preserved below for reference only.*
```

4. Commit changes

**Repeat for:**
- `Shatha-db/pizoo-subscription`
- `Shatha-db/pizoo-dating-app-final`

---

### 🔴 **STEP 2.2: Archive Repositories**

For each old repo:

1. Go to repository **Settings**
2. Scroll to bottom → **Danger Zone**
3. Click **"Archive this repository"**
4. Confirm by typing repository name
5. Click **"I understand the consequences, archive this repository"**

**Effects of archiving:**
- ✅ Repository becomes read-only
- ✅ No new commits, issues, or PRs
- ✅ Preserves all history and releases
- ✅ Can be unarchived later if needed
- ✅ Reduces confusion about active repos

---

## ⚙️ PHASE 3: CI/ACTIONS REPAIR

### Current Issues:
- GitHub Actions may be failing (needs verification)
- Workflows might be outdated or misconfigured

### 🔴 **STEP 3.1: Check GitHub Actions Status**

1. Go to: https://github.com/Shatha-db/pizoo-dating-app/actions

2. Check recent workflow runs:
   - ✅ Green = passing
   - ❌ Red = failing
   - ⚪ Gray = not running

3. Identify failing workflows:
   - `.github/workflows/lint.yml`
   - `.github/workflows/test.yml`
   - `.github/workflows/build.yml`
   - `.github/workflows/deploy.yml`

---

### 🔴 **STEP 3.2: Fix Workflow Configurations**

**Common fixes needed:**

#### **A. Update Node.js Version**

Edit: `.github/workflows/*.yml`

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20.x'  # ← Update to 20.x
          cache: 'yarn'
```

#### **B. Fix Working Directory**

```yaml
- name: Install frontend dependencies
  working-directory: ./frontend  # ← Add this
  run: yarn install

- name: Build frontend
  working-directory: ./frontend  # ← Add this
  run: yarn build
```

#### **C. Backend Python Setup**

```yaml
- name: Setup Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'  # ← Match your backend

- name: Install backend dependencies
  working-directory: ./backend  # ← Adjust path
  run: |
    pip install --upgrade pip
    pip install -r requirements.txt
```

---

### 🔴 **STEP 3.3: Enable Actions Permissions**

1. Go to: https://github.com/Shatha-db/pizoo-dating-app/settings/actions

2. Under **"Actions permissions"**:
   - Select: ✅ **"Allow all actions and reusable workflows"**

3. Under **"Workflow permissions"**:
   - Select: ✅ **"Read and write permissions"**
   - Enable: ✅ **"Allow GitHub Actions to create and approve pull requests"**

4. Click **"Save"**

---

### 🔴 **STEP 3.4: Temporarily Disable Strict Checks (Optional)**

If CI is blocking merges but not critical:

1. Go to: https://github.com/Shatha-db/pizoo-dating-app/settings/branches

2. Edit `main` branch protection

3. Under **"Require status checks to pass before merging"**:
   - Uncheck problematic workflows temporarily
   - OR disable branch protection entirely during consolidation

4. **Remember to re-enable after fixes!**

---

## 🚀 PHASE 4: VERCEL RE-LINK & DEPLOY

### Current State:
- Vercel project exists: `pizoo`
- May be connected to old repo or outdated branch
- Missing `vercel.json` on `main` branch

---

### 🔴 **STEP 4.1: Verify vercel.json on Main**

After Step 1.2 (merge), verify:

```bash
curl -s "https://api.github.com/repos/Shatha-db/pizoo-dating-app/contents/vercel.json?ref=main" | python3 -c "import sys, json; print(json.load(sys.stdin).get('name', 'NOT FOUND'))"
```

**Expected:** `vercel.json`

**If missing, create it:**

File: `/vercel.json` (repo root)
```json
{
  "version": 2,
  "buildCommand": "cd frontend && yarn install && yarn build",
  "outputDirectory": "frontend/build",
  "installCommand": "cd frontend && yarn install",
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

Commit and push to `main`.

---

### 🔴 **STEP 4.2: Reconnect Vercel to Correct Repo**

1. Go to: https://vercel.com/dashboard

2. Click on your project: **`pizoo`**

3. Go to: **Settings** → **Git**

4. **Disconnect** current Git integration:
   - Click **"Disconnect"**
   - Confirm

5. **Connect** to correct repo:
   - Click **"Connect Git Repository"**
   - Select: **GitHub**
   - Choose: **`Shatha-db/pizoo-dating-app`**
   - Branch: **`main`** (set as Production Branch)
   - Click **"Connect"**

6. ✅ Vercel now tracks `main` branch

---

### 🔴 **STEP 4.3: Configure Vercel Build Settings**

In Vercel project **Settings** → **General**:

1. **Framework Preset:**
   - Select: **"Other"** or **"Create React App"**

2. **Build & Development Settings:**
   ```
   Build Command: cd frontend && yarn install && yarn build
   Output Directory: frontend/build
   Install Command: yarn install
   ```

3. **Root Directory:**
   - Leave empty (if vercel.json is at root)
   - OR set to `frontend/` if needed

4. Click **"Save"**

---

### 🔴 **STEP 4.4: Environment Variables (if needed)**

In Vercel **Settings** → **Environment Variables**:

Add any required variables:
```
NODE_ENV=production
REACT_APP_BACKEND_URL=https://pizoo.ch/api
```

---

### 🔴 **STEP 4.5: Deploy to Production**

**Option A: Trigger Deploy Manually**

1. In Vercel Dashboard → **Deployments**
2. Click **"Redeploy"** on latest deployment
3. Select: **"Use existing Build Cache"** → No
4. Click **"Redeploy"**

**Option B: Use Deploy Hook**

```bash
curl -X POST "https://api.vercel.com/v1/integrations/deploy/prj_8ZKPw4z3kOreyIVPywFD4OE3EdxJ/2im8oZHyQW"
```

**Expected Response:**
```json
{"job":{"id":"...","state":"PENDING","createdAt":...}}
```

---

### 🔴 **STEP 4.6: Monitor Build**

1. Watch build logs in Vercel Dashboard
2. Wait for **"Ready"** status (usually 1-2 minutes)
3. Check for errors:
   - ✅ Build Command succeeded
   - ✅ Output Directory correct
   - ✅ Deployment successful

---

### 🔴 **STEP 4.7: Verify Production Domains**

**Test each domain:**

```bash
# Primary domain
curl -I https://pizoo.ch

# WWW subdomain
curl -I https://www.pizoo.ch

# Vercel default
curl -I https://pizoo.vercel.app
```

**Expected:**
- All return `HTTP/2 200` (or `307` redirect for www)
- `last-modified` header shows recent timestamp
- No 404 errors

---

### 🔴 **STEP 4.8: Test SPA Routing**

Visit in browser:
- https://pizoo.ch/login
- https://pizoo.ch/register
- https://pizoo.ch/terms
- https://pizoo.ch/privacy

**Expected:**
- ✅ Pages load (no 404)
- ✅ React app renders
- ✅ Rewrites working correctly

---

## 🌐 PHASE 5: DNS & DOMAINS

### Current DNS Provider: Hostpoint

---

### 🔴 **STEP 5.1: Get Vercel DNS Records**

1. In Vercel Dashboard → **Settings** → **Domains**

2. Click on **`pizoo.ch`**

3. Copy the required DNS records:
   ```
   Type: A
   Name: @
   Value: 76.76.21.21 (or current Vercel IP)

   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   ```

4. Note: Vercel may show different values - use those!

---

### 🔴 **STEP 5.2: Update Hostpoint DNS**

1. Log in to: https://www.hostpoint.ch/

2. Go to: **My Hostpoint** → **Domains** → **pizoo.ch**

3. Click: **DNS Zone Editor** or **Manage DNS**

4. **Update A Record (root domain):**
   ```
   Type: A
   Host: @ (or blank)
   Value: [Vercel IP from Step 5.1]
   TTL: 3600 (or Auto)
   ```

5. **Update CNAME Record (www):**
   ```
   Type: CNAME
   Host: www
   Value: [Vercel CNAME from Step 5.1]
   TTL: 3600 (or Auto)
   ```

6. **Remove conflicting records:**
   - Delete old A records for @ or www
   - Delete old CNAME records that conflict

7. Click **"Save Changes"**

---

### 🔴 **STEP 5.3: Wait for DNS Propagation**

- DNS updates can take 5 minutes to 48 hours
- Usually completes within 30 minutes

**Check propagation:**
```bash
dig pizoo.ch
dig www.pizoo.ch

# Or use online tools:
# https://www.whatsmydns.net/#A/pizoo.ch
```

---

### 🔴 **STEP 5.4: Verify in Vercel**

1. Go to Vercel **Settings** → **Domains**

2. Check status of `pizoo.ch` and `www.pizoo.ch`:
   - ✅ **Valid** = DNS configured correctly
   - ⚠️ **Invalid Configuration** = Check DNS records
   - ⏳ **Pending** = Wait for propagation

3. If invalid, Vercel will show specific error:
   - Follow the instructions provided
   - Double-check DNS records match

---

## 🎨 PHASE 6: BRANDING & .ENV

### Ensure Correct Logo Usage:

---

### 🔴 **STEP 6.1: Verify Logo Files**

Check that these exist on `main` branch:

```bash
# Check via GitHub API
curl -s "https://api.github.com/repos/Shatha-db/pizoo-dating-app/contents/frontend/src/assets/branding?ref=main" | python3 -c "import sys, json; files = json.load(sys.stdin); print('\n'.join([f['name'] for f in files]))"
```

**Expected files:**
```
pizoo-classic.png  (Classic Orange - for login/register)
pizoo-golden.png   (Golden Glow - for internal pages)
pizoo-classic.svg
pizoo-golden.svg
```

**If missing:** They need to be committed to `main` (from local workspace or conflict_071125_1347)

---

### 🔴 **STEP 6.2: Verify Logo Components**

Check React components exist:

```bash
curl -s "https://api.github.com/repos/Shatha-db/pizoo-dating-app/contents/frontend/src/components/branding?ref=main" | python3 -c "import sys, json; files = json.load(sys.stdin); print('\n'.join([f['name'] for f in files]))"
```

**Expected:**
```
PizooLogo.jsx     (Main unified component)
Wordmark.jsx      (For auth pages)
GoldenLogo.jsx    (For internal pages)
```

---

### 🔴 **STEP 6.3: Verify Logo Usage in Pages**

**Login/Register pages should use Classic Orange:**

File: `frontend/src/pages/Login.js`
```jsx
import Wordmark from '../components/branding/Wordmark';

// In render:
<Wordmark variant="classic" width={200} />
```

**Internal pages should use Golden Glow:**

File: `frontend/src/pages/Home.js`
```jsx
import CustomLogo from '../components/CustomLogo';

// In navbar:
<CustomLogo size="xs" />  // Uses Golden Glow internally
```

---

### 🔴 **STEP 6.4: Trim Logo Images (No Extra Padding)**

If logos have excess transparent space:

1. Download logo files
2. Use image editor (Photoshop, GIMP, or online tools)
3. **Trim transparent pixels** (Image → Trim → Transparent Pixels)
4. **Save as PNG** with transparency
5. **Optimize file size** (use TinyPNG or similar)
6. Replace in repo and commit

---

### 🔴 **STEP 6.5: Standardize Email Configuration**

**Backend files to check:**

File: `backend/.env.example`
```bash
EMAIL_FROM="info Pizoo <support@pizoo.ch>"
EMAIL_FROM_NAME=info Pizoo
```

File: `backend/email_service.py`
```python
EMAIL_FROM = os.getenv('EMAIL_FROM', 'support@pizoo.ch')
EMAIL_FROM_NAME = os.getenv('EMAIL_FROM_NAME', 'info Pizoo')
```

File: `backend/auth_service.py`
```python
EMAIL_FROM = os.environ.get('EMAIL_FROM', 'info Pizoo <support@pizoo.ch>')
```

---

### 🔴 **STEP 6.6: Remove Old Email References**

Search and replace in entire codebase:

```bash
# Search for old emails
grep -r "info@shatha.ch" .
grep -r "@example.com" .

# Replace with new email
# (Use IDE find-replace or manual edit)
```

**Replace with:**
```
support@pizoo.ch
```

**Exceptions:** Test files and documentation can keep example.com

---

### 🔴 **STEP 6.7: Verify .env.example (No Secrets)**

File: `backend/.env.example`

Ensure it contains:
```bash
# ✅ Good - Example values
SMTP_USER=<your-email@gmail.com>
SECRET_KEY=<generate-secure-random-key>

# ❌ Bad - Real secrets
SMTP_USER=realuser@gmail.com
SECRET_KEY=actual_secret_key_abc123
```

**If real secrets exist:**
1. Replace with placeholder values
2. Commit `.env.example`
3. **Never commit `.env`** (should be in `.gitignore`)

---

## 📊 PHASE 7: FINAL REPORT & HANDOVER

### AI Agent Will Generate:

---

### Report Contents:

1. **GitHub Consolidation Status:**
   - Merged commits/PR IDs
   - Deleted branches list
   - Archived repositories
   - Remaining active branches

2. **GitHub Actions Status:**
   - Workflow names and status
   - Fixed configurations
   - Remaining issues (if any)

3. **Vercel Deployment:**
   - Deployment ID
   - Build time and status
   - Connected repo and branch
   - Environment variables

4. **Domain Verification:**
   - pizoo.ch status (200 OK)
   - www.pizoo.ch status (redirect or 200)
   - pizoo.vercel.app status (200 OK)
   - Screenshots of login page (branding)

5. **Remaining Issues:**
   - Any unfixed problems
   - Action items for user
   - Recommendations

6. **Success Criteria Met:**
   - ✅ Single repo active
   - ✅ Single branch (main)
   - ✅ Vercel deploying correctly
   - ✅ New branding visible
   - ✅ Domains working

---

## 📋 SUMMARY OF YOUR ACTIONS REQUIRED

### 🔴 **Critical (Must Do Now):**

1. **Merge latest branch to main:**
   - [ ] Go to: https://github.com/Shatha-db/pizoo-dating-app/compare/main...conflict_071125_1347
   - [ ] Create PR and merge

2. **Reconnect Vercel to correct repo:**
   - [ ] Vercel Dashboard → Settings → Git
   - [ ] Disconnect old, connect to pizoo-dating-app (main)

3. **Deploy to production:**
   - [ ] Vercel → Redeploy
   - [ ] OR use deploy hook (AI can trigger this)

4. **Verify domains work:**
   - [ ] Visit pizoo.ch/login
   - [ ] Check for new PiZOO branding

---

### 🟡 **Important (Do After Critical):**

5. **Archive old repositories:**
   - [ ] Add deprecation notice to READMEs
   - [ ] Archive: pizoo, pizoo-subscription, pizoo-dating-app-final

6. **Delete obsolete branches:**
   - [ ] conflict_021125_1024
   - [ ] conflict_041125_1150
   - [ ] conflict_041125_1944
   - [ ] conflict_071125_1347 (after merge verified)
   - [ ] conflict_311025_* (all three)

7. **Fix GitHub Actions (if failing):**
   - [ ] Check workflow status
   - [ ] Update Node.js to 20.x
   - [ ] Fix working directories
   - [ ] Enable Actions permissions

---

### 🟢 **Optional (Nice to Have):**

8. **Update DNS if needed:**
   - [ ] Check Vercel domain settings
   - [ ] Update Hostpoint A/CNAME records
   - [ ] Wait for propagation

9. **Trim logo images:**
   - [ ] Remove excess transparent padding
   - [ ] Optimize file sizes

10. **Clean up .env files:**
    - [ ] Ensure .env.example has no secrets
    - [ ] Remove old email references

---

## 🎯 SUCCESS CRITERIA

### You'll know it's working when:

✅ **GitHub:**
- Only `main` branch active (+ any active dev branches)
- `conflict_071125_1347` merged successfully
- Old repos archived with deprecation notices
- Actions passing (or disabled temporarily)

✅ **Vercel:**
- Project connected to `Shatha-db/pizoo-dating-app` (main)
- Latest deployment shows new branding
- Build successful with no errors

✅ **Production:**
- https://pizoo.ch loads with new PiZOO logo (Classic Orange on login)
- https://www.pizoo.ch redirects or works
- https://pizoo.vercel.app works
- No 404 errors on /login, /register, /terms, etc.

✅ **Branding:**
- Login page: Classic Orange "PiZOO" text logo
- Internal pages: Golden Glow logo
- No excess transparent padding
- Clean, professional appearance

✅ **Configuration:**
- vercel.json present on main
- Email standardized to support@pizoo.ch
- No secrets in .env.example
- All old emails removed

---

## 🆘 TROUBLESHOOTING

### If domains show old branding:

1. Check GitHub `main` has latest code:
   ```bash
   curl -s "https://api.github.com/repos/Shatha-db/pizoo-dating-app/contents/vercel.json?ref=main"
   ```

2. Check Vercel is deploying from correct repo/branch:
   - Vercel Dashboard → Settings → Git

3. Trigger new deployment:
   - Vercel Dashboard → Redeploy

4. Clear browser cache:
   - Ctrl+Shift+R (hard refresh)

---

### If merge fails with conflicts:

1. **Use GitHub UI conflict resolution:**
   - GitHub will show conflicts in PR
   - Click "Resolve conflicts"
   - Choose content from `conflict_071125_1347`
   - Mark as resolved and commit

2. **Or use local Git:**
   ```bash
   git checkout main
   git merge conflict_071125_1347
   # Resolve conflicts in files
   git add .
   git commit -m "Resolve merge conflicts"
   git push origin main
   ```

---

### If Vercel build fails:

1. **Check build logs** in Vercel Dashboard

2. **Common issues:**
   - Wrong build command → Fix in Settings
   - Wrong output directory → Should be `frontend/build`
   - Missing dependencies → Check package.json
   - Node version mismatch → Use 20.x

3. **Test build locally:**
   ```bash
   cd frontend
   yarn install
   yarn build
   # Should succeed without errors
   ```

---

### If domains don't work:

1. **Check DNS records** at Hostpoint:
   - A record for @ points to Vercel IP
   - CNAME for www points to Vercel CNAME

2. **Check Vercel domain status:**
   - Settings → Domains → should show "Valid"

3. **Wait for DNS propagation:**
   - Can take up to 48 hours (usually 30 min)

4. **Test with dig:**
   ```bash
   dig pizoo.ch
   dig www.pizoo.ch
   ```

---

## 📞 NEXT STEPS

### What AI Agent Will Do Next:

Once you complete the critical steps (merge + Vercel reconnect):

1. ✅ Trigger Vercel deploy (if you provide hook URL)
2. ✅ Verify all domains respond correctly
3. ✅ Take screenshots of new branding
4. ✅ Generate final comprehensive report
5. ✅ Provide branch cleanup commands
6. ✅ Confirm success criteria met

### What You Need to Tell AI Agent:

- ✅ "Merge completed" (after Step 1)
- ✅ "Vercel reconnected" (after Step 2)
- ✅ "Ready for verification" (after Step 3)

Then AI agent will verify and generate final report!

---

**Guide Created:** November 7, 2025, 15:37 UTC  
**Status:** Ready for execution  
**Estimated Time:** 30-60 minutes (depending on DNS propagation)

---

*End of Guide*
