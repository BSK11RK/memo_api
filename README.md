# メモ管理API（FastAPI）


## 1. 概要
FastAPIを使用して作成したメモ管理APIです。
ユーザー登録・認証（JWT）・メモのCRUD機能を実装しています。


## 2. 機能

- ユーザー登録
- ログイン（JWT認証）
- メモの作成・取得・更新・削除
- メモ検索機能
- ユーザーごとのデータ分離
- パスワードのハッシュ化
- バリデーション


## 3. 技術スタック

- FastAPI
- SQLite
- SQLAlchemy
- JWT認証
- passlib（bcrypt）
- Docker / docker-compose


## 4. ディレクトリ構成

memo_api/
├── app/
│   ├── main.py        # エントリーポイント
│   ├── models.py      # DBモデル
│   ├── schemas.py     # バリデーション
│   ├── crud.py        # DB操作
│   ├── auth.py        # 認証・JWT処理
│   └── database.py    # DB接続
├── data/              # SQLiteデータ（gitignore対象）
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md


## 5. API例

### ログイン

POST /login

request:
{
  "username": "test",
  "password": "test123"
}

response:
{
  "access_token": "xxxxx",
  "token_type": "bearer"
}


## 6. 実行方法

### Dockerで起動

docker-compose up --build

### APIドキュメント

http://localhost:8000/docs


## 7. 工夫した点

- JWT認証を導入し、認証付きAPIを実装した
- パスワードをハッシュ化してセキュリティを強化した
- ユーザーごとにメモを分離する設計にした
- バリデーションを追加し、不正な入力を防止した


## 8. 今後の改善

- PostgreSQLへの対応
- ページネーション機能の追加
- テストコードの追加