import sqlite3
import os
import time
import datetime

def getDB():
    # db = pymysql.connect("localhost", "root", "123456", "RentInfo")
    base_path = os.path.abspath(os.path.dirname(__file__))
    sqlite_filename = os.path.join(base_path, 'rto.db')
    pwd = os.getcwd()
    # 当前文件的父路径
    # father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
    # sqlite_filename = os.path.join(father_path, 'yeeyitable.db')
    db=sqlite3.connect(sqlite_filename)
    return db

def is_in_table(column_name, val):
    db = getDB()
    cur = db.cursor()
    sql='select count(%s) from mytable where %s = ?' % (column_name, column_name)
    cur.execute(sql, [val])
    counts = cur.fetchall()
    cur.close()
    db.close()
    if (int(counts[0][0]) >= 1):
        return True
        # print('重复了', index_a.getText())
    else:
        return False

getDB()