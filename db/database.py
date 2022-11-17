from pymongo import MongoClient


# 회원
# - 회원 가입(Create)
# - 회원 목록(Read)
# - 회원 수정(update)
# - 회원 삭제(Delete)


# 상품
# - 상품 가입(Create)
# - 상품 목록(Read)
# - 상품 수정(update)
# - 상품 삭제(Delete)

# 게시판
# - 게시글 가입(Create)
# - 게시글 목록(Read)
# - 게시글 수정(update)
# - 게시글 삭제(Delete)

# -> CRUD 작업   DAO(Data Access Object) 만듬
# 게시글 -> BoardDAO.py
# 회원 -> MemverDAO.py

# 진짜 코드!

# 1. Connection 작업(공통)
def db_conn():
    client = MongoClient("127.0.0.1", 27017)  # MongoDB 찾아감
    db = client['movie']                      # Database 선택
    collection = db.get_collection('review')  # Collection 선택
    return collection


# 2. Review 저장(Create)
def create_review():
    collection = db_conn()  # MongoDB Connection
    data = {"msg": "몽고디비 커넥션 테스트"}
    collection.insert_one(data)

# 3. Reviwe 조회(Read)
def read_review():
    collection = db_conn()  # MongoDB Connection

