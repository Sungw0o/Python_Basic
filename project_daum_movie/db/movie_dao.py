from common.connection import connection

# 리뷰 데이터 저장


def add_review(data):
    # 1)Connection
    conn = connection()

    try:
        pass
    except Exception as e:
        print(e)
    finally:
        # 자원 반납
        conn.close()