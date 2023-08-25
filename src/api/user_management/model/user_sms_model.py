from sqlalchemy import Column, DateTime, String, Boolean, Integer
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from database.db import Base
    

class SmsModel(Base):
    __tablename__ = 'sms_data'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    message = Column(String)
    number = Column(Integer)

    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow())    
    created_by = Column(String, default=False)
    modify_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    modify_by = Column(String)
