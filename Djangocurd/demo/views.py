from django.shortcuts import render
import json
from django.http import request,JsonResponse
from demo.models import Person,Persondetail,Class,Student,User,Auth
from django.core import serializers
# Create your views here.
def add(request):
    p=Person.objects.create(name="樊文鹏")
    pd=Persondetail.objects.create(home="张家口",p=p)
    print("一对一增加成功")

    c=Class.objects.create(cname="五班")
    s1=Student.objects.create(sname="张三",c=c)
    s2 = Student.objects.create(sname="李四",c=c)
    s2 = Student.objects.create(sname="王五",c=c)
    print("一对多增加成功")

    a1=Auth.objects.create(aname="查看")
    a2=Auth.objects.create(aname="改写")
    a3 = Auth.objects.create(aname="不知道")

    u1=User.objects.create(uname="小王")
    u2=User.objects.create(uname="小李")
    u1.a.add(a1,a2)
    u2.a.add(a1,a2,a3)
    print("多对多增加成功")

    # p=Person.objects.create(name="fanwenpeng")
    # pd=Persondetail.objects.create(home="zhangjiakou",p=p)
    # print("一对一增加成功")

    # c=Class.objects.create(cname="wuban")
    # s1=Student.objects.create(sname="zhangsan",c=c)
    # s2 = Student.objects.create(sname="lisi",c=c)
    # s2 = Student.objects.create(sname="wangwu",c=c)
    # print("一对多增加成功")
    #
    # a1=Auth.objects.create(aname="chakanquanxian")
    # a2=Auth.objects.create(aname="gaixieqianxian")
    # a3 = Auth.objects.create(aname="buzhidaoquanxian")
    #
    # u1=User.objects.create(uname="xiaowang")
    # u2=User.objects.create(uname="xiaoli")
    # u1.a.add(a1,a2)
    # u2.a.add(a1,a2,a3)
    # print("多对多增加成功")
    r={}
    r["status"]=200
    r["msg"] = "成功"
    r["data"]=None
    return JsonResponse(r)

def delete(request):
    #一对一删除
    # Persondetail.objects.filter(p__name="fanwenpeng").delete()
    # Person.objects.filter(persondetail__home="zhangjiakou").delete()

    #一对多删除
    #Student.objects.filter(c__cname="wuban").delete()

    #多对多删除
    #删除指定的关联关系
    # u=User.objects.filter(id=1).first()
    # a=Auth.objects.filter(id=1).first()
    # u.a.remove(a)

    #删除全部关联关系
    u = User.objects.filter(id=3).first()
    u.a.clear()


    r={}
    r["status"]=200
    r["msg"] = "成功"
    r["data"]=None
    return JsonResponse(r)

def select(request):
    #一对一查询
    data=Persondetail.objects.filter(p__name="fanwenpeng").values("home","p_id","p__name")
    print(data)
    data=json.dumps(list(data))

    #一对多查询
    data=Class.objects.filter(cname="五班改").values("cname","student__sname")
    data = json.dumps(list(data))

    #多对多查询
    data1=Auth.objects.filter(id=5).values("aname")
    data2=Auth.objects.filter(id=5).values("user__uname")
    data = json.dumps(list(data1)+list(data2))


    # data=serializers.serialize('json', data)
    r={}
    r["status"]=200
    r["msg"] = "成功"
    r["data"]=data
    return JsonResponse(r)

def updata(request):
    #一对一
    Persondetail.objects.filter(p__name="樊文鹏").update(home="家乡改")
    Person.objects.filter(persondetail__home="家乡改").update(name="樊文鹏改")
    #一对多
    Class.objects.filter(student__sname="张三").update(cname="五班改")
    Student.objects.filter(c__cname="wuban").update(sname="班级人员全改了")
    #多对多类似
    r = {}
    r["status"] = 200
    r["msg"] = "成功"
    r["data"] = None
    return JsonResponse(r)





