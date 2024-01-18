import pymysql


def get_connection():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='123lapopo123',
                                db='adogcionweb')