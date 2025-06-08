from sqlalchemy.orm import Session
from app.models.user import User

def seed_users(db: Session):
    chico = db.query(User).filter(
        User.username == "admin",
        User.email == "admin@root.com",
        User.role_id == 2
    ).first()
    
    if chico is None:
        chico = User(username="Chico", email="guichiwawa@gmail.com", role_id=2)
        db.add(chico)
        db.commit()
        db.refresh(chico)