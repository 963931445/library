"""项目 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  .bigtype import *
from .view import *
from .tyni import *
from .book import *
from .catalog import *
from .flag import *
from .ajaxs import *
from .pillow import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",index),
    path('regist/', regist),
    path('login/', login),
    path("code/",mycode),
    # path('login/',login),
    path("userlogin/", userlogin),
    path("userreg/", userreg),
    path("del_cookie/", del_cookie),
    path("get_session/",get_session),
    # 大分类
    path("biginfo/",biginfo.as_view()),
    path("bigtyadd/",bigtyadd.as_view()),
    path("bigtydel/",bigtydel.as_view()),
    path("bigtyedit/", bigtyedit.as_view()),

    # 小分类
    path("tyniinfo/",tyniinfo.as_view()),
    path("tyniadd/",tyniadd.as_view()),
    path("tyniedit/",tyniedit.as_view()),
    path("tynidel/",tynidel.as_view()),
    path("ajax_bigtyid/",ajax_bigtyid.as_view()),
    path("ajax_bigtyname/",ajax_bigtyname.as_view()),
    path("ajax_tyniname/", ajax_tyniname.as_view()),
    path("ajax_tyniid/", ajax_tyniid.as_view()),

    # 书
    path("bookinfo/",bookinfo.as_view()),
    path("bookadd/", bookadd.as_view()),
    path("bookdel/", bookdel.as_view()),
    path("ajax_tyni/",ajax_tyni.as_view()),
    path("bookedit/",bookedit.as_view()),

    # 章节
    path("catainfo/",catainfo.as_view()),
    path("catadd/",catadd.as_view()),
    path("catedit/",catedit.as_view()),
    path("catdel/",catdel.as_view()),
    path("ajax_bookname1/",ajax_bookname1.as_view()),
    path("ajax_bookname/",ajax_bookname.as_view()),

    # 标识符管理
    path("flaginfo/",flaginfo.as_view()),
    path("flagadd/",flagadd.as_view()),
    path("flagedit/",flagedit.as_view()),
    path("flagdel/",flagdel.as_view()),

    # client
    # ajax
    path("ajax/register/",register.as_view()),
    path("ajax/checkUser/",checkUser.as_view()),
    path("ajax/userindex/",userindex.as_view()),
    path("ajax/password/",password.as_view()),
    path("ajax/uspa/",uspa.as_view()),
    path("ajax/shuben/", shuben.as_view()),
    path("ajax/shuji/", shuji.as_view()),
    path("ajax/lookbook/", lookbook.as_view()),
    path("ajax/shujione/", shujione.as_view()),
    path("ajax/xiangqing/", xiangqing.as_view()),
    path("ajax/duoshu/", duoshu.as_view()),
    path("ajax/fenlei/", fenlei.as_view()),
    path("ajax/shu/", shu.as_view()),
    #lunbo
    path("ajax/lunbo/", lunbo.as_view()),

]
