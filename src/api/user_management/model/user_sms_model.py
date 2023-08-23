from database.base import Base
from sqlalchemy import Column, DateTime, String, Date, Boolean, ForeignKey, Integer
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy.orm import relationship
from db.db_session import engine

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

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

session.add_all([
   SmsModel(message = 'Hello', number = 9327707507), 
   SmsModel(message = 'test', number = 7894561230)]
)
