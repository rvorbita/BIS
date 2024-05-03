from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa 
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    

class Entry(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    firstname: so.Mapped[str] = so.mapped_column(sa.String(100))
    lastname: so.Mapped[str] = so.mapped_column(sa.String(100))
    middlename: so.Mapped[str] = so.mapped_column(sa.String(100))
    age: so.Mapped[int] = so.mapped_column(sa.Integer(100))
    address: so.Mapped[str] = so.mapped_column(sa.String(100))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):

        return 'Entry {}>'.format(self.firstname)
    
    