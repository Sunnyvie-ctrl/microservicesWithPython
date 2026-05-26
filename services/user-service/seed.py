from app.database import SessionLocal
from app.models import User

db = SessionLocal()

existing = db.query(User).count()

if existing == 0:
    users = [
        User(
            username="alice",
            email="alice@example.com",
            hashed_password="password",
        ),
        User(
            username="bob",
            email="bob@example.com",
            hashed_password="password",
        ),
    ]

    db.add_all(users)
    db.commit()

    print("Seeded users")

else:
    print("Users already exist")

db.close()