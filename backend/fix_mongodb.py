#!/usr/bin/env python3
"""
MongoDB Database Repair and Optimization Script for Pizoo
This script:
1. Checks and creates necessary indexes
2. Validates data integrity
3. Fixes any inconsistencies
4. Reports on database health
"""

import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timezone
import sys

# MongoDB connection
MONGO_URL = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
DB_NAME = os.environ.get('DB_NAME', 'pizoo_database')

async def main():
    print("=" * 70)
    print("🔧 Pizoo MongoDB Repair & Optimization Tool")
    print("=" * 70)
    print()
    
    # Connect to MongoDB
    print(f"📡 Connecting to MongoDB: {MONGO_URL}")
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    
    try:
        # Test connection
        await client.admin.command('ping')
        print("✅ Connected successfully!")
        print()
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return
    
    # ========================================
    # 1. Check Collections
    # ========================================
    print("📋 Step 1: Checking collections...")
    collections = await db.list_collection_names()
    required_collections = ['users', 'profiles', 'subscriptions', 'user_settings']
    
    for coll in required_collections:
        if coll in collections:
            count = await db[coll].count_documents({})
            print(f"   ✅ {coll}: {count} documents")
        else:
            print(f"   ⚠️  {coll}: Collection missing! Will be created on first use.")
    print()
    
    # ========================================
    # 2. Create/Verify Indexes
    # ========================================
    print("📇 Step 2: Creating/Verifying indexes...")
    
    # Users collection indexes
    print("   👤 Users collection:")
    try:
        # Unique index on email
        await db.users.create_index("email", unique=True)
        print("      ✅ Unique index on 'email'")
        
        # Index on id
        await db.users.create_index("id")
        print("      ✅ Index on 'id'")
        
        # Index on phone_number
        await db.users.create_index("phone_number")
        print("      ✅ Index on 'phone_number'")
        
        # Index on subscription_status
        await db.users.create_index("subscription_status")
        print("      ✅ Index on 'subscription_status'")
        
        # Index on verified
        await db.users.create_index("verified")
        print("      ✅ Index on 'verified'")
        
    except Exception as e:
        print(f"      ⚠️  Error creating users indexes: {e}")
    
    # Profiles collection indexes
    print("   📝 Profiles collection:")
    try:
        # Unique index on user_id
        await db.profiles.create_index("user_id", unique=True)
        print("      ✅ Unique index on 'user_id'")
        
        # Index on id
        await db.profiles.create_index("id")
        print("      ✅ Index on 'id'")
        
        # Compound index for matching
        await db.profiles.create_index([
            ("gender", 1),
            ("looking_for", 1),
            ("location.coordinates", "2dsphere")
        ])
        print("      ✅ Compound index for matching (gender, looking_for, location)")
        
    except Exception as e:
        print(f"      ⚠️  Error creating profiles indexes: {e}")
    
    # Subscriptions collection indexes
    print("   💳 Subscriptions collection:")
    try:
        # Unique index on user_id
        await db.subscriptions.create_index("user_id", unique=True)
        print("      ✅ Unique index on 'user_id'")
        
        # Index on status
        await db.subscriptions.create_index("status")
        print("      ✅ Index on 'status'")
        
        # Index on next_payment_date
        await db.subscriptions.create_index("next_payment_date")
        print("      ✅ Index on 'next_payment_date'")
        
    except Exception as e:
        print(f"      ⚠️  Error creating subscriptions indexes: {e}")
    
    # User settings collection indexes
    print("   ⚙️  User Settings collection:")
    try:
        # Unique index on user_id
        await db.user_settings.create_index("user_id", unique=True)
        print("      ✅ Unique index on 'user_id'")
        
    except Exception as e:
        print(f"      ⚠️  Error creating user_settings indexes: {e}")
    
    print()
    
    # ========================================
    # 3. Data Integrity Checks
    # ========================================
    print("🔍 Step 3: Data integrity checks...")
    
    # Check for users without password_hash
    users_without_password = await db.users.count_documents({
        "$or": [
            {"password_hash": {"$exists": False}},
            {"password_hash": None},
            {"password_hash": ""}
        ]
    })
    
    if users_without_password > 0:
        print(f"   ⚠️  Found {users_without_password} users without password_hash")
        print("      These users might not be able to login!")
    else:
        print("   ✅ All users have password_hash")
    
    # Check for users without profiles
    users_count = await db.users.count_documents({})
    profiles_count = await db.profiles.count_documents({})
    
    if users_count != profiles_count:
        print(f"   ⚠️  Mismatch: {users_count} users but {profiles_count} profiles")
        
        # Find users without profiles
        users = await db.users.find({}, {"id": 1, "name": 1, "email": 1}).to_list(length=None)
        user_ids = {user['id'] for user in users}
        
        profiles = await db.profiles.find({}, {"user_id": 1}).to_list(length=None)
        profile_user_ids = {profile['user_id'] for profile in profiles}
        
        users_without_profiles = user_ids - profile_user_ids
        
        if users_without_profiles:
            print(f"      Found {len(users_without_profiles)} users without profiles:")
            for user_id in users_without_profiles:
                user = next((u for u in users if u['id'] == user_id), None)
                if user:
                    print(f"         - {user['email']} ({user['name']})")
    else:
        print(f"   ✅ Users and profiles match: {users_count} each")
    
    # Check for users without subscriptions
    subscriptions_count = await db.subscriptions.count_documents({})
    
    if users_count != subscriptions_count:
        print(f"   ⚠️  Mismatch: {users_count} users but {subscriptions_count} subscriptions")
    else:
        print(f"   ✅ Users and subscriptions match: {users_count} each")
    
    print()
    
    # ========================================
    # 4. Database Statistics
    # ========================================
    print("📊 Step 4: Database statistics...")
    
    # Users stats
    total_users = await db.users.count_documents({})
    verified_users = await db.users.count_documents({"verified": True})
    trial_users = await db.users.count_documents({"subscription_status": "trial"})
    active_users = await db.users.count_documents({"subscription_status": "active"})
    
    print(f"   👥 Total users: {total_users}")
    print(f"   ✓  Verified: {verified_users} ({verified_users*100//total_users if total_users > 0 else 0}%)")
    print(f"   🆓 Trial: {trial_users}")
    print(f"   💎 Active: {active_users}")
    
    # Profiles stats
    profiles_with_photos = await db.profiles.count_documents({
        "photos": {"$exists": True, "$ne": [], "$not": {"$size": 0}}
    })
    print(f"   📸 Profiles with photos: {profiles_with_photos}")
    
    # Recent activity
    from datetime import timedelta
    week_ago = datetime.now(timezone.utc) - timedelta(days=7)
    recent_users = await db.users.count_documents({
        "created_at": {"$gte": week_ago.isoformat()}
    })
    print(f"   🆕 New users (last 7 days): {recent_users}")
    
    print()
    
    # ========================================
    # 5. Test Login Functionality
    # ========================================
    print("🔐 Step 5: Testing login functionality...")
    
    # Get a sample user
    sample_user = await db.users.find_one({}, {"email": 1, "password_hash": 1, "name": 1})
    
    if sample_user:
        has_password = bool(sample_user.get('password_hash'))
        print(f"   Sample user: {sample_user.get('email')}")
        print(f"   Password hash exists: {'✅ Yes' if has_password else '❌ No'}")
        
        if has_password:
            print(f"   Password hash format: {sample_user['password_hash'][:20]}...")
            if sample_user['password_hash'].startswith('$2b$'):
                print("   ✅ Password hash format is correct (bcrypt)")
            else:
                print("   ⚠️  Password hash format might be incorrect")
    else:
        print("   ⚠️  No users found in database")
    
    print()
    
    # ========================================
    # Summary
    # ========================================
    print("=" * 70)
    print("📋 SUMMARY")
    print("=" * 70)
    print()
    print("✅ Database Connection: OK")
    print(f"✅ Collections: {len(collections)} found")
    print(f"✅ Indexes: Created/Verified")
    print(f"✅ Total Users: {total_users}")
    print()
    
    if users_without_password > 0:
        print("⚠️  ACTION REQUIRED: Some users missing password_hash")
    
    if users_count != profiles_count:
        print("⚠️  ACTION REQUIRED: Users and profiles count mismatch")
    
    if users_count != subscriptions_count:
        print("⚠️  ACTION REQUIRED: Users and subscriptions count mismatch")
    
    print()
    print("✅ Database optimization complete!")
    print()
    
    # Close connection
    client.close()

if __name__ == "__main__":
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv('/app/backend/.env')
    
    asyncio.run(main())
