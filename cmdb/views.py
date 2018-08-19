from django.shortcuts import render
from cmdb import models
# Create your views here.
from django.shortcuts import HttpResponse


def index(request):
    # 直接返回字符串
    # return HttpResponse("hello world! I'am coming")

    #  通过html文件返回
    return render(request, "index.html")


user_list = [
    {"user": "jack", "pwd": "abc"},
    {"user": "rose", "pwd": "hha"},
]


def contact(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        new_user = {"user": username, "pwd": password}
        user_list.append(new_user)

    return render(request, "form.html", {"data": user_list})


def database(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)

    # 从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()

    return render(request, "form_database.html", {"data": user_list})
