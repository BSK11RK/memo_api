# スキーマ（入力・出力）
from pydantic import BaseModel
from datetime import datetime


# ユーザー
class UserCreate(BaseModel):
    username: str
    password: str


# 入力（作成）
class MemoCreate(BaseModel):
    title: str
    content: str
    

# 出力   
class MemoResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    
    class Config:
        from_attributes = True
        
        
# 入力（更新）
class MemoUpdate(BaseModel):
    title: str
    content: str