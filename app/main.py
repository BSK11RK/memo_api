# FastAPI起動
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.auth import create_access_token, get_current_user, verify_password
import app.models as models, app.schemas as schemas, app.crud as crud


# テーブル作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DBセッション
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.post("/login")     
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(
        models.User.username == form_data.username
    ).first()
    
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


# メモを作成（認証必須）
@app.post("/memos")
def create_memo(
    memo: schemas.MemoCreate, 
    db: Session =  Depends(get_db),
    username: str = Depends(get_current_user)
):
    user = db.query(models.User).filter(
        models.User.username == username
    ).first()
    return crud.create_memo(db, memo, user.id)


# 全件取得
@app.get("/memos")
def read_memos(
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user)
):
    user = db.query(models.User).filter(
        models.User.username == username
    ).first()
    return crud.get_memos(db, user.id)


# 1件取得
@app.get("/memos/{memo_id}", response_model=schemas.MemoResponse)
def read_memo(memo_id: int, db: Session = Depends(get_db)):
    memo = crud.get_memo(db, memo_id)
    if memo is None:
        raise HTTPException(status_code=404, detail="Memo not found")
    return memo


# 更新
@app.put("/memos/{memo_id}", response_model=schemas.MemoResponse)
def update_memo(memo_id: int, memo: schemas.MemoUpdate, db: Session = Depends(get_db)):
    updated = crud.update_memo(db, memo_id, memo)
    if updated is None:
        raise HTTPException(status_code=404, detail="Memo not found")
    return updated


# 削除
@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_memo(db, memo_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Memo not found")
    return {"message": "Deleted"}


# 検索機能（認証必須）
@app.get("/memos/search", response_model=list[schemas.MemoResponse])
def search_memos(
    q: str, 
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return crud.search_memos(db, q)