import pymysql

from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2,
    maxcached=5,
    blocking=True,
    setsession=[],
    ping=0,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='bilibili',
    charset='utf8',
)

def fetch_login(sql,params):
    #conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='bilibili')
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    res = cursor.fetchone()
    cursor.close()
    conn.close()
    return res