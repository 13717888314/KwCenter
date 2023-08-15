from django.shortcuts import render
import requests
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
             return render(request,"index5.html", {'token': tokengl})
           else:
             return render(request,"index5.html",{'token': res})

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
        r = requests.post(url, datas)
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
            return render(request, "index6.html", {'dit': dit})
        else:
            return render(request, "index6.html", {'dit': res})