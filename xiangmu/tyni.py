from django.views import View
from django.shortcuts import HttpResponse,render,redirect
from .database import *
import json
import math
from .page import *

class tyniinfo(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 5
        sql="select tyni.id as id,tyni.tyniname as tyniname,tyni.tyniid as tyniid,tyni.bigtyid as bigtyid,bigtype.bigtyname as bigtyname from tyni left join bigtype on tyni.bigtyid=bigtype.bigtyid limit %s,%s"
        db=database()
        result = db.selectAll(sql,[page * num,num])
        sql2 = "select count(*) as t from tyni left join bigtype on tyni.bigtyid=bigtype.bigtyid"
        total = db.selectOne(sql2)
        db.close()
        total = total["t"]
        print(total)
        total = math.ceil(total / num)
        stupage = getpages(total, page, num, "/tyniinfo/")
        return render(request,"tyni/tyniinfo.html",{"data":result,"page":stupage})

class tyniadd(View):
    def get(self,request):
        db=database()
        result = db.selectAll("select * from bigtype")
        db.close()
        return render(request,"tyni/tyniadd.html",{"big":result})

    def post(self,request):
        tyniid = request.POST.get("tyniid")
        tyniname = request.POST.get("tyniname")
        bigtyid = request.POST.get("bigtyid")
        sql="insert into tyni (tyniid,tyniname,bigtyid) values(%s,%s,%s)"
        db=database()
        db.insert(sql,[tyniid,tyniname,bigtyid])
        db.close()
        return redirect("/tyniinfo/")

class tyniedit(View):
    def get(self,request):
        id = request.GET.get("id")
        sql="select tyni.id as id,tyni.tyniname as tyniname,tyni.tyniid as tyniid,tyni.bigtyid as bigtyid,bigtype.bigtyname as bigtyname from tyni left join bigtype on tyni.bigtyid=bigtype.bigtyid where tyni.id =%s"
        db=database()
        big=db.selectAll("select * from bigtype")
        result = db.selectOne(sql,[id])
        db.close()
        return render(request,"tyni/tyniedit.html",{"data":result,"big":big})

    def post(self,request):
        id = request.POST.get("id")
        bigtyid = request.POST.get("bigtyid")
        tyniid = request.POST.get("tyniid")
        tyniname = request.POST.get("tyniname")
        print(id,bigtyid,tyniid,tyniname)
        sql="update tyni set tyniid=%s,tyniname=%s,bigtyid=%s where id=%s"
        db=database()
        db.updata(sql,[tyniid,tyniname,bigtyid,id])
        db.close()
        return redirect("/tyniinfo/")

class tynidel(View):
    def get(self,request):
        id = request.GET.get("id")

        sql="delete from tyni where id=%s"
        db=database()
        db.updata(sql,[id])
        db.close()
        return redirect("/tyniinfo/")

class ajax_tyniid(View):
    def get(self,request):
        tyniid = request.GET.get("tyniid")
        sql="select * from tyni where tyniid=%s"
        db=database()
        result = db.selectOne(sql,[tyniid])
        db.close()
        if result:
            return HttpResponse("false")
        else:
            return HttpResponse("true")

class ajax_tyniname(View):
    def get(self,request):
        tyniname = request.GET.get("tyniname")
        sql="select * from tyni where tyniname=%s"
        db=database()
        result = db.selectOne(sql,[tyniname])
        db.close()
        if result:
            return HttpResponse("false")
        else:
            return HttpResponse("true")