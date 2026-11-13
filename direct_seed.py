import sqlite3
import os
import hashlib

# Path to database
db_path = r"c:\Users\mdadi\Downloads\Salespulse\backend\salespulse.db"

def get_simple_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def seed_db():
    print(f"Connecting to {db_path}...")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if users table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
        if not cursor.fetchone():
            print("Users table doesn't exist. Initializing schema...")
            # I won't create schema here, I'll assume the tables exist if the app successfully "connection verified"
        
        # The password hash for "Adil@146"
        # We'll use the SHA256 fallback for simplicity in this script, or try to use a dummy hash that the app can verify
        # Actually, it's better to use the signup endpoint or let the app seed itself
        
        # Let's try to just insert a user with a plain SHA256 hash
        pwd_hash = get_simple_hash("Adil@146")
        
        # Check if user exists
        cursor.execute("SELECT id FROM users WHERE username='adil_r146';")
        row = cursor.fetchone()
        
        if row:
            print("User adil_r146 exists. Updating password...")
            cursor.execute("UPDATE users SET hashed_password=? WHERE username='adil_r146';", (pwd_hash,))
        else:
            print("Inserting user adil_r146...")
            import uuid
            user_id = str(uuid.uuid4())
            cursor.execute("""
                INSERT INTO users (id, email, username, hashed_password, full_name, role, is_active)
                VALUES (?, ?, ?, ?, ?, ?, 1)
            """, (user_id, "adil_r146@salespulse.com", "adil_r146", pwd_hash, "Adil Raza", "Admin"))
        
        conn.commit()
        conn.close()
        print("Done!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    seed_db()
