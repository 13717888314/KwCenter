from django.shortcuts import render
import requests
import math
import time
import pymysql
import json
# Create your views here.


def testPro(request):
    return render(request,'login.html')

def testProNew(request):
    return render(request,'loginKw.html')

def testIndex1(request):
    return render(request,'index1.html')

def testIndex2(request):
    return render(request,'index2.html')

def testIndex3(request):
    return render(request,'index3.html')

def testIndex4(request):
    return render(request,'index4.html')

def apipost(request):
         global tokengl
         print(request.method)
         if request.method == 'GET':
             return render(request,'index4.html')
         elif request.method == 'POST':
           username = request.POST.get("username")
           password = request.POST.get("password")
           datas={"username":username,
                "password":password
                 }
             # datas = request.POST.get('remark')
             # header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
           url= "https://openwhy.net/api/auth/login"
           r = requests.post(url,datas)
           res =r.text
           body = r.json()
           if body["code"] == "000000":
             token = body["datas"]["token"]
             tokengl = "Bearer" + " " + token
             return render(request,"index4.html", {'token': tokengl})
           else:
             return render(request,"index4.html", {'token': res})

def testappid(request):
    # if request.method == 'GET':
    #     return render(request, 'index4.html')
    # elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
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
            return render(request, "index4.html", {'dit': dit})
        else:
            return render(request, "index4.html", {'dit': res})


def testYYid(request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        datas = {"username": username,
                 "password": password
                 }
        url = "https://openwhy.net/api/auth/login"
        r = requests.post(url, datas)
        res = r.text
        body = r.json()

        #  apd = query_data()
        #
        # print("apd::"+apd)
        if body["code"] == "000000":
            token = body["datas"]["token"]
            token2 = "Bearer" + " " + token
            header ={
            "X-Authorization": token2,
            "Content-Type": 'application/json',
            "appid": "2b24987dd59d6504"
            }
            print("header22::"+str(header))
            datas1 = '{}'
            url = "https://open.openwhy.net/api/v1/weapp/manager/reservation/list?page=1"
            r = requests.post(url, headers=header,data=datas1)
            res2 = r.text
            print ("res2:"+res2)
            body = r.json()
            data = body["datas"]
            result1= []
            result2= []
            for i in data:
                result1.append(i["name"])
                result2.append(i["id"])
            print("data:" + str(result1))
            print("data2:" + str(result2))
            dityyid = dict(zip(result1,result2))
            print("dir::"+str(dityyid))
            return render(request, "index4.html", {'dityyid': dityyid})
        else:
            return render(request, "index4.html", {'dityyid': res})


def tjyy(request):
    # 连接数据库
    conn = pymysql.connect(
        host='81.69.195.135',  # 主机名
        port=7709,  # 端口号，MySQL默认为3306
        user='zwtx',  # 用户名
        password='teb#Fn8y-3p',  # 密码
        database='openy',  # 数据库名称
    )
    timestamp = time.time()
    integer_timestamp = math.floor(timestamp)
    yyid = request.POST.get("yyid")
    try:
        # 步骤2：通过连接对象获取游标对象 ---> Cursor
        with conn.cursor() as cursor:
            # 步骤3：通过游标对象向数据库发出SQL并获取执行结果
            sql = "INSERT INTO reservation_template VALUES ("+str(integer_timestamp)+",'5',"+yyid+",'2023-08-15 14:16:09');"
            affected_rows = cursor.execute(sql)
            if affected_rows == 1:
                print('预约模板添加成功！！！')
                tjyy = "预约模板添加成功！！！"
                return render(request, "index4.html", {'tjyy': tjyy})
        # 步骤4：操作成功提交（让之前的操作生效）
        conn.commit()
    except pymysql.MySQLError as err:
        print(err)
        return render(request, "index4.html", {'tjyy': err})
        # 步骤4：操作失败回滚（撤销之前的操作）
        conn.rollback()
    finally:
        # 步骤5：关闭连接，释放资源
        conn.close()






