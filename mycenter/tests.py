from django.test import TestCase
# Create your tests here.
# import MySQLdb as mdb
import sys
import pymysql
import pandas as pd
import requests
import mysql.connector
import datetime
import math
import time

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

        sq="SELECT id FROM weapp_apply wa where wa.appName like '%开问体验版%';"
        cursor.execute(sq)
        # 获取查询结果
        result = cursor.fetchall()

        print("info:"+str(result))

        # 获取查询结果的字段名和元数据
        columns = [col[0] for col in cursor.description]

        # 将查询结果封装到 Pandas DataFrame 中
        df = pd.DataFrame(result, columns=columns)

        return df

    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()


def sq_dat():
    mydb = mysql.connector.connect(
        host='81.69.195.135',  # 主机名
        port=7709,  # 端口号，MySQL默认为3306
        user='zwtx',  # 用户名
        password='teb#Fn8y-3p',  # 密码
        database='openy',  #
    )
    cursor = mydb.cursor()

    cursor.execute("SELECT id FROM weapp_apply wa where wa.appName like '%开问体验版%';")

    results = cursor.fetchall()

    fi = str(results)[3:-4]

    return fi

    cursor.close()
    mydb.close()


def yyidnew():
        username = "13717888314"
        password = "1q2w3e4r5t6y"
        datas = {"username": username,
                 "password": password
                 }
        url = "https://openwhy.net/api/auth/login"
        r = requests.post(url, datas)
        res = r.text
        body = r.json()

        apd = sq_dat()
        print("apd:"+apd)
        if body["code"] == "000000":
            token = body["datas"]["token"]
            token2 = "Bearer" + " " + token
            header = {
                "X-Authorization": token2,
                "Content-Type": 'application/json',
                "appid": apd
            }
            print("header22::" + str(header))
            datas1 = '{}'
            url = "https://open.openwhy.net/api/v1/weapp/manager/reservation/list?page=1"
            r = requests.post(url, headers=header,data=datas1)

            res2 = r.text
            print("res2:" + res2)
            body = r.json()
            data11 = body["datas"]
            result1 = []
            result2 = []
            for i in data11:
                result1.append(i["name"])
                result2.append(i["id"])
            print("data:" + str(result1))
            print("data2:" + str(result2))
            dit = dict(zip(result1, result2))
            print("dir::" + str(dit))
            resss= str(dit)
            return resss


def testappid():
    # if request.method == 'GET':
    #     return render(request, 'index4.html')
    # elif request.method == 'POST':
        username = "13717888314"
        password = "1q2w3e4r5t6y"
        datas = {"username": username,
                 "password": password
                 }
        url = "https://openwhy.net/api/auth/login"
        r = requests.post(url, data=datas)
        res = r.text
        body = r.json()
        if body["code"] == "000000":
            token = body["datas"]["token"]
            token2 = "Bearer" + " " + token
            header ={
            "X-Authorization":token2 }
            print("header22::"+str(header))
            url = "https://open.openwhy.net/api/v1/weapp/manager/apply/list"
            r = requests.get(url,headers=header)
            res2 = r.text
            print ("res2:"+res2)
            body = r.json()

            data = body["datas"]["applyList"]
            result1= []
            result2= []
            for i in data:
                result1.append(i["appName"])
                result2.append(i["id"])
            print("data:" + str(result1))
            print("data2:" + str(result2))
            dit = dict(zip(result1,result2))
            print("dir::"+str(dit))


def yyjg():
    # 连接数据库
    conn = pymysql.connect(
        host='81.69.195.135',  # 主机名
        port=7709,  # 端口号，MySQL默认为3306
        user='zwtx',  # 用户名
        password='teb#Fn8y-3p',  # 密码
        database='openy',  # 数据库名称
    )

    yyid = '1691381191040700416'
    try:

        # 步骤2：通过连接对象获取游标对象 ---> Cursor
        with conn.cursor() as cursor:

            # 步骤3：通过游标对象向数据库发出SQL并获取执行结果
            # sql = "INSERT INTO reservation_template VALUES ('1691653895627083776','5','1691653895627083776','2023-08-15 14:16:09');"

            sql = "INSERT INTO reservation_template VALUES ("+yyid+",'5',"+yyid+",'2023-08-15 14:16:09');"
            affected_rows = cursor.execute(sql)
            if affected_rows == 1:
                print('添加预约成功！！！')
        # 步骤4：操作成功提交（让之前的操作生效）
        conn.commit()
    except pymysql.MySQLError as err:
        print(err)
        # 步骤4：操作失败回滚（撤销之前的操作）
        conn.rollback()
    finally:
        # 步骤5：关闭连接，释放资源
        conn.close()


if __name__ == '__main__':
    # sql_query='select id from reservation_template_class'
    # db_data = query_data(sql_query)
    # db_data= query_data()
    #   yyjg()
    timestamp = time.time()
    integer_timestamp = math.floor(timestamp)
    print("整数时间戳（向下取整）：", str(integer_timestamp))
     # yyidnew()
