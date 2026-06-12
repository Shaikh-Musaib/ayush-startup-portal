from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String,
        nullable=False
    )

    phone = Column(String)

    role = Column(
        String,
        default="USER",
        nullable=False
    )

    # One User can own multiple startups
    startups = relationship(
        "Startup",
        back_populates="owner",
        cascade="all, delete-orphan"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )