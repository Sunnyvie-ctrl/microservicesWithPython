from app.database import SessionLocal
from app.models import Game

db = SessionLocal()

existing = db.query(Game).count()

if existing == 0:
    games = [
        Game(
            title="Cyberpunk 2077",
            genre="RPG",
            platform="PC",
        ),
        Game(
            title="Minecraft",
            genre="Sandbox",
            platform="PC",
        ),
    ]

    db.add_all(games)
    db.commit()

    print("Seeded games")

else:
    print("Games already exist")

db.close()