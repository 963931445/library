from django.views import View
from django.shortcuts import HttpResponse,render,redirect
from .database import *

class flaginfo(View):
    def get(self,request):
        sql="select * from flag"
        db=database()
        result = db.selectAll(sql)
        db.close()
        return render(request,"flag/flaginfo.html",{"data":result})

class flagadd(View):
    def get(self,request):
        return render(request,"flag/flagadd.html")
    def post(self,requset):
        flagid=requset.POST.get("flagid")
        flagname = requset.POST.get("flagname")
        sql="insert into flag(flagid,flagname)values(%s,%s)"
        db=database()
        db.insert(sql,[flagid,flagname])
        db.close()
        return redirect("/flaginfo/")

class flagedit(View):
    def get(self,request):
        id=request.GET.get("id")
        db=database()
        result = db.selectOne("select * from flag where id=%s",[id])
        db.close()
        return render(request,"flag/flagedit.html",{"data":result})
    def post(self,request):
        id = request.POST.get("id")
        flagid=request.POST.get("flagid")
        flagname = request.POST.get("flagname")
        sql="update flag set flagid=%s,flagname=%s where id=%s"
        db=database()
        db.insert(sql,[flagid,flagname,id])
        db.close()
        return redirect("/flaginfo/")

class flagdel(View):
    def get(self,request):
        flagid=request.GET.get("flagid")
        db=database()
        db.updata("delete from flag where flagid=%s",[flagid])
        # db.updata("delete from arc where find_in_set(%s,catid)", [catid])
        result = db.selectAll("select * from arc where FIND_IN_SET(%s,flagid)",[flagid])
        print(result, "result")
        for item in result:
            str1 = ""
            for item1 in item["flagid"].split(","):
                if item1 != flagid:
                    str1 += ",".join(item1)
            db.updata("update arc set flagid=%s where id=%s",[str1,item["id"]])
        db.close()
        return redirect("/flaginfo/")