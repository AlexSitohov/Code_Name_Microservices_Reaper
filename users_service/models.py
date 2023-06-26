from sqlalchemy import Column, String, TIMESTAMP, text, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid as _uuid
from datetime import datetime

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=_uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String, nullable=False)
    email = Column(String(30), unique=True)
    phone = Column(String, unique=True)
    city = Column(String(30), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    email_confirmed_date_time = Column(DateTime, nullable=True)
