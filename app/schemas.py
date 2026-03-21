# スキーマ（入力・出力）
from pydantic import BaseModel, Field
from datetime import datetime


# ユーザー
class UserCreate(BaseModel):
    username: str
    password: str


# 入力（作成）
class MemoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="メモのコンテンツ")
    content: str = Field(..., min_length=1, max_length=1000, description="メモの内容")
    

# 出力   
class MemoResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
        
        
# 入力（更新）
class MemoUpdate(BaseModel):
    title: str
    content: str