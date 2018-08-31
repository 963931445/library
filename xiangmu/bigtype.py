from django.views import View
from django.shortcuts import HttpResponse,render,redirect
from .database import *
import json
from .page import *
class biginfo(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 5

        # up=page-1 if page-1>0 else 0
        db=database()
        result = db.selectAll("select * from bigtype  limit %s,%s",[page * num, num])

        total= db.selectOne("select count(*) as t from bigtype")
        db.close()
        total = total["t"]
        print(total)
        total = math.ceil(total / num)
        stupage = getpages(total, page, num, "/biginfo/")
        return render(request,"big/biginfo.html",{"data":result,"page":stupage})

class bigtyadd(View):
    def get(self,request):
        return render(request, "big/bigtyadd.html")
    def post(self,request):
        bigtyid = request.POST.get("bigtyid")
        bigtyname = request.POST.get("bigtyname")
        sql="insert into bigtype (bigtyid,bigtyname) values(%s,%s)"
        db=database()
        db.insert(sql,[bigtyid,bigtyname])
        db.close()
        return  redirect("/biginfo/")

class bigtydel(View):
    def get(self,request):
        bigtyid = request.GET.get("bigtyid")
        sql="delete from bigtype where bigtyid = %s"
        # print(bigtyid)
        db=database()
        db.updata(sql,[bigtyid])
        db.close()
        return redirect("/biginfo/")

class bigtyedit(View):
    def get(self,request):
        id = request.GET.get("id")
        sql="select * from bigtype where id=%s"
        db=database()
        result = db.selectOne(sql,[id])
        db.close()
        return render(request,"big/bigtyedit.html",{"data":result})
    def post(self,request):
        id = request.POST.get("id")
        bigtyid = request.POST.get("bigtyid")
        bigtyname = request.POST.get("bigtyname")
        sql="update bigtype set bigtyid=%s,bigtyname=%s where id=%s"
        db=database()
        db.updata(sql,[bigtyid,bigtyname,id])
        db.close()
        return redirect("/biginfo/")

class ajax_bigtyid(View):
    def get(self,request):
        bigtyid = request.GET.get("bigtyid")
        db=database()
        result = db.selectOne("select * from bigtype where bigtyid=%s",[bigtyid])
        if result:
            return HttpResponse("false")
        else:
            return HttpResponse("true")

class ajax_bigtyname(View):
    def get(self,request):
        bigtyname = request.GET.get("bigtyname")
        print("bigname",bigtyname)
        db=database()
        result = db.selectOne("select * from bigtype where bigtyname=%s",[bigtyname])
        if result:
            return HttpResponse("false")
        else:
            return HttpResponse("true")


