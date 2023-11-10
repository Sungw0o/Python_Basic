
from db.common.connection import conn_mongodb

def add_news(data):
    conn = conn_mongodb()
    conn.insert_one(data)


