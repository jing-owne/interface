import pymysql

connect = pymysql.connect(
    host='precloud.sysgq.com',
    user='root',  # 用户名
    passwd='Gemii!@1234',  # 密码
    port=13306,  # 端口，默认为3306
    charset='utf8',  # 字符编码
    db ='liz_qywechat_event'
)

curs = connect.cursor()

if connect:
    print("连接成功..")
else:
    print('连接失败..')


def SelectSQL(sql):
    sql = sql
    curs.execute(sql)
    rs = curs.fetchall()
    print(rs)

