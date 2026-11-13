import sqlite3
import os

# Get path to database
base_dir = r"c:\Users\mdadi\Downloads\Salespulse\backend"
db_path = os.path.join(base_dir, "salespulse.db")

print(f"Checking database at: {db_path}")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if users table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    if not cursor.fetchone():
        print("Table 'users' does not exist.")
    else:
        cursor.execute("SELECT id, email, username, full_name, role FROM users;")
        users = cursor.fetchall()
        print(f"Found {len(users)} users:")
        for user in users:
            print(user)
            
    conn.close()
except Exception as e:
    print(f"Error: {e}")
