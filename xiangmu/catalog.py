from django.views import View
from django.shortcuts import HttpResponse,render,redirect
from .database import *
import sys
import time
import random 
import json
import math
from .page import *

class catainfo(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 5
        sql = "select book.bookid as bookid,book.bookname as bookname,cat.catinfo as catinfo, cat.catid as catid,cat.catname as catname,cat.catinfo as catinfo from cat LEFT JOIN book on cat.bookid = book.bookid limit %s,%s"
        db = database()
        result = db.selectAll(sql,[page*num,num])
        sql2="select count(*) as t from cat LEFT JOIN book on cat.bookid = book.bookid"
        total = db.selectOne(sql2)
        db.close()
        total = total["t"]
        print(total)
        total = math.ceil(total / num)
        stupage = getpages(total, page, num, "/catainfo/")
        return render(request,"catalog/cataloginfo.html",{"data":result,"page":stupage})

# class catsearch(View):
#     def get(self,request):
#         return render(request, "catalog/catsearch.html")
#
#     def post(self,request):
#         bookname = request.POST.get("bookname")
#         sql="select book.bookid as bookid,book.bookname as bookname,cat.catinfo as catinfo, cat.catid as catid,cat.catname as catname from cat LEFT JOIN book on cat.bookid = book.bookid where book.bookname=%s"
#         db=database()
#         result = db.selectAll(sql,[bookname])
#         return render(request, "catalog/cataloginfo.html",{"data":result})
#
class catadd(View):
    def get(self,request):
        return render(request, "catalog/catadd.html")
    def post(self,request):
        catname = request.POST.get("catname")
        bookname = request.POST.get("bookname")
        catid = request.POST.get("catid")
        file = request.FILES["catainfo"]
        str1=""
        for item in file.chunks():
            str1+=item.decode('gbk')
            # f.write(item.decode('gbk'))
        # f.close()
        print(str1)
            # return redirect("/paper/")
            # print(type(item.decode('gbk')))
            # print()

            # f.write(item.decode('gbk'))

        # print(dictdata)
        # f.close()
        sql = "select bookid from book where bookname=%s"
        sql1="insert into cat(catname,catid,catinfo,bookid)values(%s,%s,%s,%s)"
        db=database()
        id = db.selectOne(sql,[bookname])["bookid"]
        print("id",id)
        db.insert(sql1,[catname,catid,str1,id])
        db.close()
        return redirect("/catainfo/")

class catedit(View):
    def get(self,request):
        catid=request.GET.get("catid")
        db=database()
        result= db.selectOne("SELECT book.bookid as bookid,book.bookname as bookname,cat.catinfo as catinfo,cat.id as id,cat.catid as catid, cat.catname as catname from book LEFT JOIN cat on cat.bookid =book.bookid where catid=%s",[catid])
        db.close()
        return render(request,"catalog/cataedit.html",{"data":result})
    def post(self,request):
        id = request.POST.get("id")
        catid = request.POST.get("catid")
        catname = request.POST.get("catname")
        catinfo = request.POST.get("catinfo")
        sql="update cat set catid=%s,catname=%s,catinfo=%s,catid=%s where id=%s"
        db=database()
        db.updata(sql,[catid,catname,catinfo,catid,id])
        db.close()
        return redirect("/catainfo/")


class catdel(View):
    def get(self,request):
        catid = request.GET.get("catid")
        sql="delete from cat where catid=%s"
        db=database()
        db.updata(sql,[catid])
        db.close()
        return redirect("/catainfo/")



