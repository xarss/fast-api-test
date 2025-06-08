from sqlalchemy.orm import Session
from app.models.user import User

def seed_users(db: Session):
    admin = db.query(User).filter(
        User.username == "admin",
        User.email == "admin@root.com",
        User.role_id == 2
    ).first()
    
    if admin is None:
        admin = User(username="admin", email="admin@root.com", role_id=2)
        db.add(admin)
        db.commit()
        db.refresh(admin)