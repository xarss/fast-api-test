from sqlalchemy.orm import Session
from app.models.role_models import Role

def seed_roles(db: Session):
    if db.query(Role).filter(Role.name == "Default").first() is None:
        admin_role = Role(name="Default", description="Default access role.")
        db.add(admin_role)
        db.commit()
        db.refresh(admin_role)

    if db.query(Role).filter(Role.name == "Admin").first() is None:
        admin_role = Role(name="Admin", description="Administrator with full access.")
        db.add(admin_role)
        db.commit()
        db.refresh(admin_role)