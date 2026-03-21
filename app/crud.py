# CRUD処理
from sqlalchemy.orm import Session
from app.auth import hash_password
import app.models as models, app.schemas as schemas


# ユーザー作成
def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(
        username=user.username, 
        password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# メモを新規作成
def create_memo(db: Session, memo: schemas.MemoCreate, user_id: int):
    db_memo = models.Memo(
        title=memo.title, 
        content=memo.content, 
        user_id=user_id
    )
    db.add(db_memo)
    db.commit()
    db.refresh(db_memo)
    return db_memo


# 全件取得
def get_memos(db: Session, user_id: int):
    return db.query(models.Memo).filter(
        models.Memo.user_id == user_id
    ).all()


# 1件取得
def get_memo(db: Session, memo_id: int):
    return db.query(models.Memo).filter(models.Memo.id == memo_id).first()


# 更新
def update_memo(db: Session, memo_id: int, memo: schemas.MemoUpdate):
    db_memo = db.query(models.Memo).filter(models.Memo.id == memo_id).first()
    if db_memo:
        db_memo.title = memo.title
        db_memo.content = memo.content
        db.commit()
        db.refresh(db_memo)
    return db_memo


# 削除
def delete_memo(db: Session, memo_id: int):
    db_memo = db.query(models.Memo).filter(models.Memo.id == memo_id).first()
    if db_memo:
        db.delete(db_memo)
        db.commit()
    return db_memo


# 検索機能
def search_memos(db: Session, keyword: str):
    return db.query(models.Memo).filter(
        models.Memo.title.contains(keyword)
    ).all()