# モデル作成（DB設計）
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


# ユーザー
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)


# メモ
class Memo(Base):
    __tablename__ = "memos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")