import sys
import os

# Add backend to sys.path
backend_path = r"c:\Users\mdadi\Downloads\Salespulse\backend"
sys.path.append(backend_path)

from database import SessionLocal, init_db
from models import User
from utils.auth import get_password_hash

def create_user():
    db = SessionLocal()
    try:
        # Check if user already exists
        user = db.query(User).filter(User.username == "adil_r146").first()
        if user:
            print(f"User adil_r146 already exists. Updating password...")
            user.hashed_password = get_password_hash("Adil@146")
        else:
            print("Creating user adil_r146...")
            user = User(
                email="adil_r146@salespulse.com",
                username="adil_r146",
                hashed_password=get_password_hash("Adil@146"),
                full_name="Adil",
                role="Admin",
                is_active=True
            )
            db.add(user)
        
        db.commit()
        print("Success!")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_user()
