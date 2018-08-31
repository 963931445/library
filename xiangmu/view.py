from django.views import View
from django.shortcuts import HttpResponse,render,redirect
from .database import *
import hashlib
from .pillow import *
import math
def checks(callback):
    def abc(request):
        if request.session.get('name') == "yes":
            return callback(request)
        else:
            return redirect(login)
    return abc

def session(request):
    return HttpResponse(request.session.get('name'))

def mycode(request):
    obj=code()
    obj.font="arial.ttf"
    con=obj.output()
    request.session["code"]=obj.str
    return HttpResponse(con,"image/png")
def index(request):
    if request.session.get('login')=="yes":
        return render(request,"index.html")
    else:
        return redirect("/login/")

def get_session(request):
    return HttpResponse(request.session.get("name"))

def del_cookie(request):
    del request.session['name']
    del request.session['login']
    request.session.clear()
    return redirect("/")

def md5(obj):
    h = hashlib.md5()
    t= obj.encode("utf8")
    h.update(t)
    return h.hexdigest()


def userlogin(request):
    # print(request.method)
    if request.method=="POST":
        # print("post1")
        name = request.POST.get("username")
        password = request.POST.get("password")
        week=request.POST.get("save")
        idcode = request.POST.get("idcode").lower()
        print("11111111111",name)
        # print("week",week)
        # db = pymysql.connect("localhost","root","root","w1810",charset='utf8',cursorclass= pymysql.cursors.DictCursor)
        if idcode!=request.session["code"]:
            return HttpResponse("err")
        db = database()
        sql = "select * from admi where uname=%s and upass=%s"
        result =db.selectAll(sql, [name,md5(password)])
        # 使用 fetchone() 方法获取单条数据.
        # result = cursor.fetchall()
        # cursor.close()
        db.close()
# and idcode=="hello world"
        if result :
            request.session['name']=name
            request.session['login']="yes"
            if week=="week":
                request.session.set_expiry(604800)
            else:
                request.session.set_expiry(0)
            return redirect("/")
            # return "ok"
        else:
            print("post2")
            return redirect(login)
    elif request.method=="GET":
        return redirect("/")

def login(request):
    if request.session.get('login'):
        return redirect("/")
    return render(request,"login.html")
    # return "ok"

def userreg(request):
    return render(request,"regist.html")

def regist(request):
    if request.method=="POST":
        print(12)
        print(request.method)
        name = request.POST.get("name")
        password = request.POST.get("pass")
        password1 = request.POST.get("pass1")
        print("name",name)
        print("pass",password)
        db = pymysql.connect("localhost","root","root","library",charset='utf8',cursorclass= pymysql.cursors.DictCursor)
        # 使用 cursor() 方法创建一个游标对象 cursor
        sql = "insert into admi (uname,upass) values('%s','%s')" % (name, md5(password))
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        # cursor.execute(sql, [name,md5(password)])
        # 使用 fetchone() 方法获取单条数据.
        # result = cursor.fetchall()
        # return render(request,"login.html")
        return redirect("/login/")
        # return render(request,"login.html")

# def index(request):
#     return render(request,"index.html")
def index(request):
    if request.session.get('login')=="yes":
        return render(request,"index.html")
    else:
        return redirect("/login/")
    # def get(self,request):
    #     return render(request,"index.html")