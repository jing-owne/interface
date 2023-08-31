"""
===============
    NAME = guxiaoyu
    2020年 月 26日 小时 分
    E-email:18339435211@139.com
================
"""

import mysql.connector


class MysqlHander:

    def __init__(self):  # 构造器

        try:  # 尝试连接数据库
            self.db = mysql.connector.connect(
                user="fanmao",
                passwd="fanmao",
                host="49.233.108.117",
                database="sm_app"
            )

        except Exception as err:
            print("Error:连接失败")
        except TimeoutError as err:
            print("Error:响应超时连接失败")
        else:
            print("连接数据库成功")
            self.db.close()

    def create_table(self):
        SQl = """
        create table guxiaoyu(
            id int not null auto_increment primary key,
            username varchar(255) not null,
            age int not null,
            phone varchar(11) not null
        )
        """

        cnx = self.db.cursor()
        cnx.execute(SQl)
        # 提交操作
        self.db.commit()
        print(cnx.rowcount, "创建成功。")


if __name__ == '__main__':
    MysqlHander()
    MysqlHander.create_table

    # MysqlHander.db.close()
