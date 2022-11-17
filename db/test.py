# mongodb 연결, 데이터 1건 저장 테스트
from pymongo import MongoClient
# 연결(Connection) 정보
# DB_HOST: mongodb 접속 할 => IP + PORT
# DB_ID  : mongodb 계정
# DB_PW  : mongodb 암호


#            연결 (IP + PORT)
#              ID & PW
# Python ====================== MongoDB


# 127.0.0.1 = localhost 무조건 내 컴퓨터 IP
# port 번호 기본적으로 프로그램 고유 포트 번호
# ssh: 22
# http: 80
# mariadb: 3386
# mongodb: 27017
client = MongoClient("mongodb+srv://admin:cnu1234@cluster0.9xztpcl.mongodb.net/?retryWrites=true&w=majority")

# DBMS : 데이터베이스 관리 시스텝  -> mongdb
# DB(데이터 베이스): 데이터 자장소 -> 다수의 DB(ex> shop, Blog)
# DB: shop
# - Collection(table): 회원 정보
# - Collection(table): 상품 정보
# - Collection(table): 주문 정보
# - Collection(table): 게시글정보

# DB: movie
#  ㄴ Collection: review
db = client['movie']  # mongodb에 공간(db)
collection = db.get_collection('review')

data = {"msg": "몽고디비 데이터 테스트"}  # 데이터 1건 생성
collection.insert_one(data)  # 1건의 데이터를 저장!
