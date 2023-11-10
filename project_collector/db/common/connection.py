# 데이터베이스(DB): 데이터를 효율적으로 저장하는 시스템


from pymongo import MongoClient


def conn_mongodb():
    # ip, port, id, pw
    DB_ID = "root"
    DB_PW = "1234"
    client = MongoClient(f"mongodb+srv://{DB_ID}:{DB_PW}@daumcluster.xgbylri.mongodb.net/")
    db = client["daum"]
    collection = db.get_collection("news")
    return collection


