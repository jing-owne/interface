"""
===============
    jishubu
    NAME = guxiaoyu
    2020年 月 04日 小时 分
    E-email:18339435211@139.com
================
"""
import pymysql


# import mysql.connector
class MysqlHander:
    def __init__(self):
        self.db = pymysql.connect(
            host='49.233.108.117',
            port=3306,
            user='fanmao56',
            passwd='fanmao',
            db='fanmao_students',
            charset='utf8')
        db = self.db
        print('连接数据库成功')

    def Create_table(self):
        Create_sql = """
        create table ytcj(
            `id` int(0) NOT NULL AUTO_INCREMENT,
            `name` varchar(255) NULL,
            `sex` int(0) NULL,
            `age` int(0) NOT NULL,
            `phone` varchar(255) NULL,
            PRIMARY KEY (`id`));
                            """

        cursor = self.db.cursor()
        cursor.execute(Create_sql)
        # 提交数据表操作
        self.db.commit()
        print('创建表成功')

    def insert_table(self):
        insert_sql = """
        insert into 
        ytcj(name,sex,age,phone)
        values
    ('guixaoyu',1,25,18339435200),
    ('liuxuekai',1,26,17888888888),
    ('zhaoxinlei',1,27,18999999999),
    ('liwanwan',0,18,13000000000),
    ('wujingjing',0,17,16677777777)
"""

        cursor = self.db.cursor()
        cursor.execute(insert_sql)
        # 提交数据表操作
        self.db.commit()
        print('插入数据成功')

    def select_table(self):
        drop_table = """
        select * from ytcj;
        """
        cursor = self.db.cursor()
        cursor.execute(drop_table)
        # return cursor
        print(cursor.fetchall())

    def select_age(self,age):
        age_sql = f"""
        select * from ytcj 
        where age < {age}
        
        """
        cursor = self.db.cursor()
        cursor.execute(age_sql)
        print(cursor.fetchall())


if __name__ == '__main__':
    mysql = MysqlHander()
    # mysql.Create_table()
    # mysql.insert_table()
    # mysql.select_table()
    mysql.select_age(20)
    # mysql.db.close()

