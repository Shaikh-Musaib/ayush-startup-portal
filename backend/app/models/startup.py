from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Startup(Base):
    __tablename__ = "startups"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    startup_name = Column(
        String,
        nullable=False
    )

    ayush_category = Column(
        String,
        nullable=False
    )

    founder_name = Column(
        String,
        nullable=False
    )

    description = Column(Text)

    website = Column(String)

    address = Column(String)

    registration_number = Column(
        String,
        unique=True
    )

    status = Column(
        String,
        default="Pending",
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    # Many Startups belong to One User
    owner = relationship(
        "User",
        back_populates="startups"
    )