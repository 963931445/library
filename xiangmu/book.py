from django.views import View
from django.shortcuts import HttpResponse,render,redirect
from .database import *
import sys
import time
import random
import json
import os
from .page import *
from django import forms

class mychecks(forms.Form):
    # name = forms.CharField(required=True,min_length=5)
    file = forms.FileField(required=True,error_messages={"required":"这个必选"})
    # pidinfo = forms.CharField(required=True, error_messages={"required": "这个必选"})
    # gidinfo = forms.CharField(required=True, error_messages={"required": "这个必选"})
class bookinfo(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 5
        sql="select book.bookimg as bookimg,tyni.tyniid as tyniid,tyni.tyniname as tyniname,book.bookid as bookid,book.bookname as bookname,book.author as author,book.introinfo as introinfo,bigtype.bigtyid as bigtyid,bigtype.bigtyname as bigtyname from book LEFT JOIN tyni on book.tyniid=tyni.tyniid LEFT JOIN bigtype on tyni.bigtyid=bigtype.bigtyid limit %s,%s"
        sql2="select count(*) as t from book LEFT JOIN tyni on book.tyniid=tyni.tyniid LEFT JOIN bigtype on tyni.bigtyid=bigtype.bigtyid"
        db=database()
        result = db.selectAll(sql,[page * num, num])
        total=db.selectOne(sql2)
        db.close()
        total = total["t"]
        print(total)
        total = math.ceil(total / num)
        stupage = getpages(total, page, num, "/bookinfo/")
        return render(request,"book/bookinfo.html",{"data":result,"page":stupage})

class bookadd(View):
    def get(self,request):
        sql="select * from bigtype"
        db=database()
        big = db.selectAll(sql)
        flag=db.selectAll("select * from flag")
        db.close()
        return render(request, "book/bookadd.html",{"big":big,"flag":flag})
    def post(self,request):
        # print("11111111111111111111book")
        tyniid = request.POST.get("tyniid")
        introinfo = request.POST.get("introinfo")
        author = request.POST.get("author")
        bookname = request.POST.get("bookname")
        img = request.FILES["img"]
        # print(introinfo,222222222222222222222222)
        # print(request.POST.getlist("flagid"),"22222222222222222222222222222222")
        flagid="" if not request.POST.getlist("flagid") else ",".join(request.POST.getlist("flagid"))
        imgpath="http://localhost:8000/static/image/book/"+str(random.randint(1,1000))+str(int(time.time()*1000))+".jpg"
        # print(flagid,"111111111111111111111")
        im = open(imgpath,"wb")
        for item in img.chunks():
            im.write(item)
        im.close()
        sql="insert into book (introinfo,bookname,author,bookimg,tyniid)values(%s,%s,%s,%s,%s)"
        sql1="insert into tyni_book(tyniid,bookid)values(%s,%s)"
        sql2="insert into arc(bookid,flagid)values(%s,%s)"
        db=database()
        id = db.insert(sql,[introinfo,bookname,author,imgpath,tyniid])
        db.insert(sql1,[tyniid,id])
        db.insert(sql2,[id,flagid])
        db.close()
        return redirect("/bookinfo/")

class bookedit(View):
    def get(self,request):
        bookid = request.GET.get("bookid")
        sql="select book.bookimg as bookimg,flag.flagid as flagid,flag.flagname as flagname,tyni.tyniid as tyniid,tyni.tyniname as tyniname,book.bookid as bookid,book.bookname as bookname,book.author as author,book.introinfo as introinfo,bigtype.bigtyid as bigtyid,bigtype.bigtyname as bigtyname from book LEFT JOIN tyni on book.tyniid=tyni.tyniid LEFT JOIN bigtype on tyni.bigtyid=bigtype.bigtyid  LEFT JOIN arc on book.bookid=arc.bookid LEFT JOIN flag on flag.flagid=arc.flagid where book.bookid=%s"
        db=database()
        result = db.selectOne(sql,[bookid])
        big=db.selectAll("select * from bigtype")
        tyni = db.selectAll("select * from tyni")
        flag=db.selectAll("select * from flag")
        db.close()
        return render(request,"book/bookedit.html",{"data":result,"big":big,"tyni":tyni,"flag":flag})
    def post(self,request):
        # print("11111111111111111111book")
        tyniid = request.POST.get("tyniid")
        introinfo = request.POST.get("introinfo")
        author = request.POST.get("author")
        bookname = request.POST.get("bookname")
        bookid = request.POST.get("bookid")
        flagid = "" if not request.POST.getlist("flagid") else ",".join(request.POST.getlist("flagid"))
        img = request.FILES["img"]

        if img:
            imgpath = "static/image/book/" + str(random.randint(1, 1000)) + str(int(time.time() * 1000)) + ".jpg"
            im = open(imgpath, "wb")
            for item in img.chunks():
                im.write(item)
            im.close()
            # UPDATE book left join tyni_book on book.bookid = tyni_book.bookid set book.bookid = 4, book.bookid = 4 where book.bookid = 2
            sql5="select bookimg from book where bookid=%s"
            sql1 = "update book set introinfo=%s,bookname=%s,author=%s,bookimg=%s,tyniid=%s where bookid=%s"
            sql2 = "update tyni_book set tyniid=%s where bookid=%s"

            db = database()
            os.remove(db.selectOne(sql5, [bookid])["bookimg"])
            db.updata(sql1, [introinfo, bookname, author,imgpath,tyniid, bookid])
            db.updata(sql2, [tyniid,bookid])
            db.updata("update arc set flagid=%s where bookid=%s", [flagid, bookid])
            db.close()
        else:
            sql3 = "update book set introinfo=%s,bookname=%s,author=%s,tyniid=%s where bookid=%s"
            sql4 = "update tyni_book set tyniid=%s where bookid=%s"
            db = database()
            db.updata(sql3, [introinfo, bookname, author,tyniid, bookid])
            db.updata(sql4, [tyniid, bookid])
            db.close()
        return redirect("/bookinfo/")

class bookdel(View):
    def get(self,request):
        bookid = request.GET.get("bookid")
        sql="delete from book where bookid = %s"
        sql1="delete from cat where bookid=%s"
        sql2="select bookimg from book where bookid=%s"
        db=database()
        path =db.selectOne(sql2,[bookid])["bookimg"]
        os.remove(path)
        db.updata(sql,[bookid])
        db.updata(sql1, [bookid])
        db.updata("delete from arc where bookid=%s",[bookid])
        db.close()
        return redirect("/bookinfo/")

class ajax_tyni(View):
    def get(self,request):
        bigtyid = request.GET.get("bigtyid")
        sql="select tyni.id as id,tyni.tyniid as tyniid,tyni.tyniname as tyniname,tyni.bigtyid as bigtyid,bigtyname from tyni LEFT JOIN bigtype on bigtype.bigtyid=tyni.bigtyid where tyni.bigtyid = %s"
        db=database()
        result = db.selectAll(sql,[bigtyid])
        print(result,1111111111111111111111111111)
        db.close()
        return HttpResponse(json.dumps(result))

class ajax_bookname(View):
    def get(self,request):
        bookname = request.GET.get("bookname")
        print("book",bookname)
        sql="select * from book where bookname=%s"
        db=database()
        result = db.selectOne(sql,[bookname])
        # print(result)
        db.close()
        if result:
            return HttpResponse("ok")
        else:
            return HttpResponse("err")

class ajax_bookname1(View):
    def get(self,request):
        bookname = request.GET.get("bookname")
        db=database()
        result = db.selectOne("select * from book where bookname=%s",[bookname])
        db.close()
        if result:
            return HttpResponse("false")
        else:
            return HttpResponse("true")


