from django.views import View
from django.shortcuts import HttpResponse,render,redirect
from .database import *
import json
import hashlib
def md5(str):
    md5=hashlib.md5()
    md5.update(str.encode("utf8"))
    return md5.hexdigest()
class register(View):
    def post(self,req):
        # print('======----------------===========')
        uid=req.POST.get("uid")
        uname=req.POST.get("uname")
        upass=req.POST.get("upass")
        upass1=req.POST.get("upass1")
        print("users",uid)
        print("password",upass)
        print("pass1",upass1)
        print("names",uname)
        if uid!=""and upass==upass1 and uname!="":
            print(uid,uname,upass,upass1)
            sql = "insert into user (uid,upass,uname)values(%s,%s,%s)"
            db = database()
            db.insert(sql, [uid,md5(upass),uname])
            db.close()
            return HttpResponse("ok")
        else:
            return HttpResponse("err")
class checkUser(View):
    def get(self,req):
        print("--------------------------")
        uid = req.GET.get("uid")
        print(uid)
        db = database()
        # cursor = db.cursor()
        sql = "select * from user where uid=%s"
        # db.cursor(sql,[uid])
        result=db.selectAll(sql,[uid])

        db.close()
        # result=cursor.execute(sql);
        if(result):
            return HttpResponse("err")
        else:
            return HttpResponse("ok")
class userindex(View):
    def post(self,req):
        uid=req.POST.get("uid")
        upass=req.POST.get("upass")
        print(uid,upass)
        db=database()
        sql = "select * from user where uid=%s and upass=%s"
        result=db.selectAll(sql, [uid, md5(upass)])
        print(result)
        if len(result) > 0:
            # arr = {"upass": result[0]["upass"], "uid": result[0]["uid"], "message": "ok"}
            return HttpResponse("ok")
        else:
            return HttpResponse("err")
class uspa(View):
    def post(self,req):
        uid = req.POST.get("uid")
        uname = req.POST.get("uname")
        print(uid,uname)
        db = database()
        sql = "select * from user where uid=%s and uname=%s"
        result = db.selectAll(sql, [uid,uname])
        print(result,"11111111111111111")
        db.close()
        if len(result) > 0:
            return HttpResponse("ok")
        else:
            return HttpResponse("err")

class password(View):
    def post(self,req):
        uid=req.POST.get("uid")
        upass= req.POST.get("upass")
        print(uid,upass)
        # sql="update user set upass=%s where uid=%s"
        # db=database()
        # db.updata(sql,[upass,uid])
        # db.close()
        return HttpResponse("ok")

class shuben(View):
    def get(self, req):
        db = database()
        sql = "select * from book"
        result = db.selectAll(sql)
        print(result)
        db.close()
        #需要和用户关联
        return HttpResponse(json.dumps(result))
class shuji(View):
    def get(self, req):
        # print("+++++++++++++++++++++++++++++++++++++++++")
        # tyniid=req.GET.get("tyniid")
        # print(tyniid)
        tyniid=req.session.get("tyniid")
        # print(tyniid,"9999999999999999999999999999")
        db = database()
        sql = "select * from book where tyniid=%s"
        result = db.selectAll(sql,[tyniid])
        db.close()
        # print(result)
        return HttpResponse(json.dumps(result))

class lookbook(View):
    def get(self, req):
        bookid=req.GET.get("bookid")
        print(bookid,111111111111111111111111111111111)
        req.session["bookid"]=bookid
        return HttpResponse("ok")
class shujione(View):
    def get(self, req):
        bookid=req.session.get("bookid")
        # print(bookid,"9999999999999999999999999999")
        db = database()
        sql = "select * from book where bookid=%s"
        result = db.selectOne(sql,[bookid])
        db.close()
        # print(result)
        return HttpResponse(json.dumps(result))
class xiangqing(View):
    def get(self,req):
        bookid=req.GET.get("bookid")
        req.session["bookid"] = bookid
        # print(req.session["bookid"],"22222222222222")
        return HttpResponse("ok")
class duoshu(View):
    def get(self,req):
        name=req.GET.get("name")
        sql="select tyniid from tyni where tyniname=%s"
        db=database()
        id = db.selectOne(sql,[name])["tyniid"]
        # print(id,"5555555555555")
        db.close()
        req.session["tyniid"]=id
        return HttpResponse("ok")
class fenlei(View):
    def get(self,req):
        # coding=gbk
        # bigtyid=req.GET.get("bigtyid")
        # print("bigtyid",bigtyid)
        db=database()
        # sql="select * from bigtype"
        sql="SELECT tyniid,tyniname,bigtype.bigtyid as bigtyid,bigtyname from tyni LEFT JOIN bigtype on tyni.bigtyid=bigtype.bigtyid"
        data=db.selectAll(sql)
        # print(data,"====================+++++")
        obj = {}
        for item in data:
            # print(item["tyniname"])
            if not item["bigtyname"] in obj:
                obj[item["bigtyname"]] = []
                obj[item["bigtyname"]].append(item["tyniname"])
            else:
                # print(item["bigtyname"])
                obj[item["bigtyname"]].append(item["tyniname"])
                # pass
        print(obj)
        db.close()
        return HttpResponse(json.dumps(obj))
class shu(View):
    def get(self,req):
        bookid = req.session.get("bookid")
        print("bookid",00000000000000)
        db = database()
        sql = "select * from cat where bookid=%s"
        result = db.selectAll(sql, [bookid])
        db.close()
        # print(result)
        return HttpResponse(json.dumps(result))

#lunbo
class lunbo(View):
    def get(self,req):
        # print(11111111111111111)
        pass


