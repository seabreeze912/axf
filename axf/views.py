from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms.login import LoginForm
from django.http import HttpResponse
from django.contrib.auth import logout
import time
import random
from django.conf import settings
import os
from .models import Wheel, Nav, Mustbuy, Shop, FoodTypes, Goods, User, Cart, Order

def home(request):
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustbuyList = Mustbuy.objects.all()

    shoplist = Shop.objects.all()
    shop1 = shoplist[0]
    shop2 = shoplist[1:3]
    shop3 = shoplist[3:7]
    shop4 = shoplist[7:11]

    return render(request, 'axf/home.html', {'title': '主页',
                                             'wheelsList': wheelsList,
                                             'navList': navList,
                                             'mustbuyList': mustbuyList,
                                             'shop1': shop1,
                                             'shop2': shop2,
                                             'shop3': shop3,
                                             'shop4': shop4,
                                             })

# 产品市场 ****************************************************

def market(request, categoryid, cid, sortid):
    leftslider = FoodTypes.objects.all()

    if cid == '0':
        productlist = Goods.objects.filter(categoryid=categoryid)
    else:
        productlist = Goods.objects.filter(categoryid=categoryid, childcid=cid)

    if sortid == '1':
        productlist = productlist.order_by('productnum')
    elif sortid == '2':
        productlist = productlist.order_by('productnum')
    elif sortid == '3':
        pass

    group = leftslider.get(typeid=categoryid)
    childlist = []
    childnames = group.childtypenames
    # 0#进口水果：11#国产水果12
    arr1 = childnames.split('#')
    for str in arr1:
        arr2 = str.split('：')
        obj = {'childname': arr2[0], 'childid': arr2[1]}
        childlist.append(obj)
    print(childlist)

    # 判断用户是否登录
    cartlist = []
    token = request.session.get('token')
    if token:
        user = User.objects.get(usertoken=token)
        cartlist = Cart.objects.filter(useraccount=user.useraccount)
    cartlistnum = len(cartlist)

    for p in productlist:
        for c in cartlist:
            if c.productid == p.productid:
                p.num = c.productnum
                continue

    return render(request, 'axf/market.html', {'title': '闪送市场',
                                               'leftslider': leftslider,
                                               'productlist': productlist,
                                               'childlist': childlist,
                                               'categoryid': categoryid,
                                               'cid': cid,
                                               'cartlist': cartlist,
                                               'cartlistnum ': cartlistnum,
                                               })

# *************购物车****************************


def cart(request):
    # 判断用户是否登录
    token = request.session.get('token')
    print('token: ', token)
    if token != None:
        user = User.objects.get(usertoken=token)
        cartslist = Cart.objects.filter(useraccount=user.useraccount)

    return render(request, 'axf/cart.html', {'title': '购物车',
                                             'cartslist': cartslist})


def changecart(request, flag):
    # 判断用户是否登录
    token = request.session.get('token')
    print('token: ', token)
    print('flag: ', flag)
    if token == None:
    # 未登录
        return JsonResponse({'data': -1, 'status': 'error'})
    productid = request.POST.get('productid')
    print(productid)
    product = Goods.objects.get(productid=productid)
    user = User.objects.get(usertoken=token)

    # # 按 + 号增加1条订单  ******************************************************
    if flag == '0':
        # 检查库存是否足够
        if product.storenums == 0:
            return JsonResponse({'data': -2, 'status': 'error'})

        carts = Cart.objects.filter(useraccount=user.useraccount)
        print('carts: ', carts)
        c = None

        if carts.count() == 0:
        # 完全没有订单，增加新订单

            c = Cart.createcart(user.useraccount, productid, 1, product.price, True,
                                product.productimg, product.productlongname, False)
            c.save()

        else:
            try:
                # 有了，就再增加一件商品
                c = carts.get(productid=productid)
                c.productnum += 1
                c.productprice = '%.2f' % (float(c.productnum) * float(product.price))
                c.save()

            except Cart.DoesNotExist as e:
                # 没有该商品的订单，创建一个新商品订单
                c = Cart.createcart(user.useraccount, productid, 1, product.price, True,
                                    product.productimg, product.productlongname, False)
                c.save()
        # 库存减1，销量+1
        product.storenums -= 1
        product.save()
        return JsonResponse({'data': c.productnum, 'status': 'success'})

    # 按 - 号减商品订单  *****************************************************
    elif flag == '1':
        carts = Cart.objects.filter(useraccount=user.useraccount)
        print('carts: ', carts)
        c = None

        if carts.count() == 0:
            # 完全没有订单
            return JsonResponse({'data': -2, 'status': 'error'})

        else:
            try:
                # 有，就减少一件商品
                c = carts.get(productid=productid)
                c.productnum -= 1
                c.productprice = '%.2f' % (float(c.productnum) * float(product.price))

                if c.productnum == 0:
                    c.delete()
                else:
                    c.save()

            except Cart.DoesNotExist as e:
                # 没有该商品的订单，随便返回一个数
                return JsonResponse({'data': -2, 'status': 'error'})

        # 库存+1，销量-1
        product.storenums += 1
        product.save()
        return JsonResponse({'data': c.productnum, 'status': 'success'})



    elif flag == '2':
        pass
    elif flag == '3':
        pass

# **********我的*********************************

def mine(request):
    username = request.session.get('username', '登录')

    return render(request, 'axf/mine.html', {'title': '我的',
                                             'username': username, })


def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            # 正常登录。信息格式没有问题，验证账号密码正确性
            nameid = str(f.cleaned_data['username'])
            pswd = str(f.cleaned_data['passwd'])

            try:
                user = User.objects.get(useraccount=nameid)
                if pswd != user.userpasswd:
                    return redirect('/login/')
            except User.DoesNotExist as e:
                return redirect('/login/')

            # 登录成功
            usertoken = str(time.time() + random.randrange(1, 1000000))
            user.usertoken = usertoken
            user.save()

            request.session['username'] = user.username
            request.session['token'] = user.usertoken

            return redirect('/mine/')

        else:
            return render(request, 'axf/login.html', {'title': '登录',
                                                      'form': f,
                                                      'error': f.errors, })
    else:
        # 不登录，要显示表单
        f = LoginForm()
        return render(request, 'axf/login.html', {'title': '登录',
                                                  'form': f, })


def quit(request):
    logout(request)
    return redirect('/mine/')


def regist(request):
    if request.method == 'POST':
        useraccount = str(request.POST.get('useraccount'))
        userpasswd = request.POST.get('userpasswd')
        username = request.POST.get('username')
        userphone = request.POST.get('userphone')
        useradderss = request.POST.get('useradderss')
        userrank = 0

        # 创建token***************************
        usertoken = str(time.time() + random.randrange(1, 1000000))

        f = request.FILES['userimg']
        userimg = os.path.join(settings.MEDIA_ROOT, useraccount + '.png')
        with open(userimg, 'wb') as fp:
            for data in f.chunks():
                fp.write(data)

        user = User.createuser(useraccount, userpasswd, username, userphone,
                useradderss, userimg, userrank, usertoken)
        user.save()

        request.session['username'] = username
        request.session['token'] = usertoken

        return redirect('/mine/')

    else:
        return render(request, 'axf/regist.html', {'title': '注册', })


def checkuserid(request):
    userid = str(request.POST.get('userid'))

    try:
        user = User.objects.get(useraccount=userid)
        return JsonResponse({'data': '该用户已经被注册', 'status': 'error'})
    except User.DoesNotExist as e:
        return JsonResponse({'data': '可以注册', 'status': 'success'})


# 保存订单******************************************
def saveorder(request):
    token = request.session.get('token')
    if token == None:
        # 未登录
        return JsonResponse({'data': -1, 'status': 'error'})

    user = User.objects.get(usertoken=token)
    carts = Cart.objects.filter(ischose=True)

    if carts.count() == 0:
        return JsonResponse({'data': -1, 'status': 'error'})
    old = str('%d' % (time.time() + random.randrange(1, 10000000)))
    o = Order.createorder(old, user.useraccount, 0)
    o.save()

    for item in carts:
        item.isdelete = True
        item.orderid = old
        item.save()




