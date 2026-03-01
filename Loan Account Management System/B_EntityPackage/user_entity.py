from A_DatabasePackage.secure_database_connection import BASE
from sqlalchemy import Column, Integer, String, DateTime, Date
from datetime import datetime
from sqlalchemy.sql import func

class UserMasterTable(BASE):
    __tablename__ = 'user_account'

    user_id = Column(Integer, primary_key=True, index=True) # Need to Delete from Schema
    user_username = Column(String, nullable=False, unique=True)
    user_password = Column(String, nullable=False)
    user_email = Column(String, nullable=False, unique=True)
    user_created_ts = Column(DateTime, nullable=False, default=datetime.utcnow) # Need to Delete from Schema
    user_created_date = Column(Date, nullable=False, server_default=func.current_date()) # Need to Delete from Schema