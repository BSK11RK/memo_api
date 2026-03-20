# CRUD処理
from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas


# ユーザー作成
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# メモを新規作成
def create_memo(db: Session, memo: schemas.MemoCreate):
    db_memo = models.Memo(title=memo.title, content=memo.content)
    db.add(db_memo)
    db.commit()
    db.refresh(db_memo)
    return db_memo


# 全件取得
def get_memos(db: Session):
    return db.query(models.Memo).all()


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