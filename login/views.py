from django.shortcuts import render, redirect
from login import models
import json
# Create your views here.
# 定义函数,数据库名 websites


def host(request):
    if request.session['msg'] == "":
        if request.method == "POST":
            usrname = request.POST.get("user_name")
            passwd = request.POST.get("user_password")
            models.UserInfo.objects.create(usr=usrname, passwd=passwd)
        return render(request, "host.html")
    return redirect("/index/")
    # 防止已登录用户误访问


def login(request):
    # login 目录下找 /templates 找 html (根据 app 注册顺序，逐一去其 /templates 下找)
    # 图片,css,js 等静态文件扔进 /static 里面
    if request.session['msg'] != "":
        return redirect("/index/")
    # 防止已登录用户误访问
    request.session['msg'] = ""
    if request.method == "GET":
        return render(request, "login.html")
    usrname = request.POST.get("user")
    passwd = request.POST.get("passwd")
    user_list = models.UserInfo.objects.all()
    for i in user_list:
        if usrname == i.usr and passwd == i.passwd:
            request.session['msg'] = usrname
            return redirect("/index/")
            # 创建此 session 作过滤器，防止非法访问，且为了在 /index 显示用户名
    return render(request, "login.html", {"error_msg": "用户名或密码错误！"})


def index(request):
    # POST 代表从删除界面过来的
    if request.method == "POST":
        need_delete = request.POST.getlist("product")
        # getlist 获取多个值
        for i in need_delete:
            models.ProductInfo.objects.filter(id=i).delete()
        # 筛选并删除选中项
    flag = request.GET.get("logout")
    if flag == "登出":
        request.session['msg'] = ""
        return redirect("/")
    # 登出操作
    data_list = models.ProductInfo.objects.all()
    if data_list.count() == 0:
        cnt = 0
    else:
        cnt = 1
    # 获取表内对象集并判断是否为空
    return render(request, "index.html", {"n1": data_list, "n2": cnt})
    # request 是一个对象，封装了用户通过浏览器等发送过来的，所有请求相关的数据


def add(request):
    if request.method == "GET":
        # GET 表示从 /index 进的 /index/add，否则会是以 POST 方式，即已添加产品后进入的 /add
        if request.session['msg'] != "":
            return render(request, "add.html")
        return redirect("/index/")
        # 过滤器，排除非法访问
    product_name = request.POST.get("product_name")
    product_price = request.POST.get('product_price')
    product_ps = request.POST.get('product_ps')
    if product_ps == "":
        product_ps = "暂无备注！"
    models.ProductInfo.objects.create(name=product_name, price=product_price, ps=product_ps)
    # 创建新行
    return redirect("/index/")


def search(request):
    if request.session['msg'] == "":
        return redirect("/index/")
    # 过滤器
    if request.method == "POST":
        need_delete = request.POST.getlist("product")
        # getlist 获取多个值
        for i in need_delete:
            models.ProductInfo.objects.filter(id=i).delete()
        # 筛选并删除选中项
    cnt = 0
    product_name = request.GET.get('search')
    data_list = models.ProductInfo.objects.all()
    need_list = []
    for i in data_list:
        if i.name.find(product_name) != -1:
            need_list.append(i.name)
            cnt = 1
    # 获取数据集，便于 for 模糊搜索
    return render(request, "search.html", {"n3": need_list, "n1": product_name, "n0": data_list, "cnt": cnt})


def register(request):
    if request.session['msg'] != "":
        return redirect("/index/")
    # 防止已登录用户误访问
    user_list = models.UserInfo.objects.all()
    return render(request, "register.html", {"n1": user_list})
