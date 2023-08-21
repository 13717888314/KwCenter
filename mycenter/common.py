import pymysql
import pandas as pd
import requests

def testapd(request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        datas = {"username": username,
                 "password": password
                 }
        url = "https://openwhy.net/api/auth/login"
        r = requests.post(url, datas)
        res = r.text
        body = r.json()
        return body


def query_data():
    # 连接数据库
    conn = pymysql.connect(
        host='81.69.195.135',  # 主机名
        port=7709,         # 端口号，MySQL默认为3306
        user='zwtx',       # 用户名
        password='teb#Fn8y-3p', # 密码
        database='openy',   # 数据库名称
    )

    try:
        # 创建游标对象
        cursor = conn.cursor()
        # 执行 SQL 查询语句
        sql_query="SELECT id FROM weapp_apply wa where wa.appName like '%开问体验版%';"
        cursor.execute(sql_query)

        # 获取查询结果
        result = cursor.fetchall()
        # print("res::"+str(result))

        print("res22:"+pd.DataFrame(result))
        # 获取查询结果的字段名和元数据
        columns = [col[0] for col in cursor.description]

        # 将查询结果封装到 Pandas DataFrame 中
        df = pd.DataFrame(result, columns=columns)

        return df

    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()

if __name__ == '__main__':
    db_data = query_data()
    # print("db:::::"+db_data)