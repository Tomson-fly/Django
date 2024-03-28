
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from house import models

# 注册
def to_login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        use = models.user()
        use.name = request.POST.get("name")
        use.password = request.POST.get("password")
        use.save()  # save新增，如果当前对象在数据库中有对应，并且id值也有对应
    return render(request, 'register.html')

# 首页，登录
def to_denglu(request):
    return render(request, 'register.html')

def Login(request):
    if request.method == "POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        res = models.user.objects.filter(name=name).filter(password=password)
        if res.exists():
            # 登录验证成功
            # return HttpResponse("感谢你的访问！")
            res = serializers.serialize("json", res)
            # print('*'*30)
            # print(eval(res)[0]["fields"]["name"])
            # print(type(eval(res)))
            # res   [{"model": "house.user", "pk": 1, "fields": {"name": "123", "password": "123"}}]

            request.session["loginUser"] = eval(res)[0]["fields"]["name"] # 将res存储在session中
            # print(eval(res)[0]["fields"]["name"])
            return HttpResponseRedirect('/first/index/')
        else:
            # 登录失败
            data={
                'flag':1,
                'error':'您输入的用户名或者密码有误，请重新输入'
            }
            return render(request, 'register.html',context=data)
    return HttpResponse("感谢你的访问！")

def to_index(request):
    return render(request, 'test.html')

def show_all_bypage(request):
    users = models.user.objects.all()
    lis = []
    for user in users:
        data = dict()
        data["id"]=user.id
        data['name'] = user.name
        data['password'] = user.password
        lis.append(data)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里
    user_info = [x for x in data]
    userinfos = {"code": 0, "msg": "", "count": users.count(), "data": user_info}
    return JsonResponse(userinfos)

# test
def show_all_bypage_rent(request):
    # rents = models.rent.objects.all()
    community = request.GET.get("community")
    if community == None:
        rents = models.rent.objects.all()
    elif community != None:
        rents = models.rent.objects.filter(community__contains=community)
    lis = []
    for info in rents:
        data = dict()
        data["id"]=info.id
        if len(info.joint)==1:
            data['joint']="合租"
        else:
            data['joint']="整租"
        data['price'] = info.price
        data['type'] = info.type
        data['area'] = info.area
        data['orientation'] = info.orientation
        data['community'] = info.community
        if len(info.metro)==1:
            data['metro'] = "近"
        else:
            data['metro'] = "远"
        if len(info.heating)==1:
            data['heating'] = "√"
        else:
            data['heating'] = "×"
        if len(info.decoration)==1:
            data['decoration'] = "√"
        else:
            data['decoration'] = "×"
        if len(info.showing)==1:
            data['showing'] = "√"
        else:
            data['showing'] = "×"
        lis.append(data)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里
    rent_info = [x for x in data]
    rentinfos = {"code": 0, "msg": "", "count": rents.count(), "data": rent_info}
    return JsonResponse(rentinfos)


def show_all_bypage_second(request):
    # seconds = models.sec.objects.all()
    community = request.GET.get("community")
    if community == None:
        seconds = models.sec.objects.all()
    elif community != None:
        seconds = models.sec.objects.filter(community__contains=community)
    lis = []
    for info in seconds:
        data = dict()
        data["id"]=info.id
        data['price'] = info.price
        data['type'] = info.type
        data['area'] = info.area
        data['community'] = info.community
        lis.append(data)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里
    second_info = [x for x in data]
    secondsinfos = {"code": 0, "msg": "", "count": seconds.count(), "data": second_info}
    return JsonResponse(secondsinfos)


def show_all_bypage_new(request):
    # price = request.GET.get("price")
    # if price == None:
    #     news = models.new.objects.all()
    #     # print(type(news))
    # elif price != None:
    #     news = models.new.objects.filter(price=price)
    #     # print(type(news))

    # type = request.GET.get("type")
    # if type == None:
    #     news = models.new.objects.all()
    # elif type!=None:
    #     news = models.new.objects.filter(type=type)
    #
    # area = request.GET.get("area")
    # if area == None:
    #     news = models.new.objects.all()
    # elif area!=None:
    #     news = models.new.objects.filter(area=area)


    community = request.GET.get("community")
    price1= request.GET.get("price1")
    price2= request.GET.get("price2")
    if price1 and price2:
        news = models.new.objects.filter(price__lte=price2).filter(price__gte=price1)
    elif community:
        news = models.new.objects.filter(community__contains=community)
    else:
        news = models.new.objects.all()


    lis = []
    for info in news:
        data = dict()
        data["id"] = info.id
        data['price'] = info.price
        data['type'] = info.type
        data['area'] = info.area
        data['community'] = info.community
        lis.append(data)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里
    new_info = [x for x in data]
    newinfos = {"code": 0, "msg": "", "count": news.count(), "data": new_info}
    return JsonResponse(newinfos)

def show_all_bypage_quanzi(request):
    name = request.GET.get("name")
    if name == None:
        buyinfos = models.buyinfo.objects.all()
    elif name != None:
        buyinfos = models.buyinfo.objects.filter(name=name)
    # buyinfos = models.buyinfo.objects.all()
    lis = []
    for info in buyinfos:
        data = dict()
        data["id"] = info.id
        data['name'] = info.name
        data['idcard'] = info.idcard
        data['phone'] = info.phone
        data['money'] = info.money
        data['renttime'] = info.renttime
        lis.append(data)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里
    buy_info = [x for x in data]
    buyinfos = {"code": 0, "msg": "", "count": buyinfos.count(), "data": buy_info}
    return JsonResponse(buyinfos)

def find_all(request):
    name=request.GET.get("name")
    user = models.user.objects.all().values()
    user_info=[]
    for i in user:
        user_info.append(i)
    msg={
        'info':user_info,
        'username':name,
    }
    return render(request,'test.html',context=msg)


def modify_stu_ajax(request):
    if request.method=='POST':
        id = request.POST.get("id")
        user = models.user.objects.get(pk=id)
        user.name=request.POST.get("name")
        user.password=request.POST.get("password")
        user.save()
        data={
            'msg':"成功"
        }
        return JsonResponse(data)

def modify_stu_ajax_sec(request):
    if request.method=='POST':
        id = request.POST.get("id")
        second = models.sec.objects.get(pk=id)
        second.community=request.POST.get("community")
        second.price=request.POST.get("price")
        second.type=request.POST.get("type")
        second.area=request.POST.get("area")
        second.save()
        data={
            'msg':"成功"
        }
        return JsonResponse(data)


def modify_stu_ajax_new(request):
    if request.method=='POST':
        id = request.POST.get("id")
        new = models.new.objects.get(pk=id)
        new.community=request.POST.get("community")
        new.price=request.POST.get("price")
        new.type=request.POST.get("type")
        new.area=request.POST.get("area")
        new.save()
        data={
            'msg':"成功"
        }
        return JsonResponse(data)

def modify_stu_ajax_rent(request):
    if request.method=='POST':
        id = request.POST.get("id")
        rent = models.rent.objects.get(pk=id)
        rent.community=request.POST.get("community")
        rent.price=request.POST.get("price")
        rent.type=request.POST.get("type")
        rent.area=request.POST.get("area")
        if request.POST.get("joint")=="整租":
            rent.joint=0
        elif request.POST.get("joint")=="合租":
            rent.joint=1
        rent.orientation=request.POST.get("orientation")
        if request.POST.get("metro")=="远":
            rent.metro=0
        else:
            rent.metro=1
        if request.POST.get("heating")=="×":
            rent.heating=0
        else:
            rent.heating=1
        if request.POST.get("decoration")=="×":
            rent.decoration=0
        else:
            rent.decoration=1
        if request.POST.get("showing")=="×":
            rent.showing=0
        else:
            rent.showing=1
        rent.save()
        data={
            'msg':"成功"
        }
        return JsonResponse(data)

def modify_stu_ajax_buy(request):
    if request.method=='POST':
        id = request.POST.get("id")

        buy = models.buyinfo.objects.get(pk=id)
        buy.name=request.POST.get("name")
        buy.idcard=request.POST.get("idcard")
        buy.phone=request.POST.get("phone")
        buy.money=request.POST.get("money")
        buy.renttime=request.POST.get("renttime")
        buy.save()
        data={
            'msg':"成功"
        }
        return JsonResponse(data)

def drop_stu_ajax(request):
    if request.method=='POST':
        id=request.POST.get("id")
        user=models.user.objects.get(pk=id)
        user.delete()
        data = {
            'msg': "成功"
        }
        return JsonResponse(data)

def drop_sec_ajax(request):
    if request.method=='POST':
        id=request.POST.get("id")
        second=models.sec.objects.get(pk=id)
        second.delete()
        data = {
            'msg': "成功"
        }
        return JsonResponse(data)


def drop_new_ajax(request):
    if request.method=='POST':
        id=request.POST.get("id")
        new=models.new.objects.get(pk=id)
        new.delete()
        data = {
            'msg': "成功"
        }
        return JsonResponse(data)


def drop_rent_ajax(request):
    if request.method=='POST':
        id=request.POST.get("id")
        rent=models.rent.objects.get(pk=id)
        rent.delete()
        data = {
            'msg': "成功"
        }
        return JsonResponse(data)

def drop_buy_ajax(request):
    if request.method=='POST':
        id=request.POST.get("id")
        buy=models.buyinfo.objects.get(pk=id)
        buy.delete()
        data = {
            'msg': "成功"
        }
        return JsonResponse(data)

def to_buyissue(request):
    return render(request,"buy_issue.html")

def to_rentissue(request):
    return render(request,"rent.html")

def to_buyinfo(request):
    return render(request,"add_buyinfo.html")

def to_aboutus(request):
    return render(request,"about.html")

def to_quanzi(request):
    return render(request, "quanzi.html")

def to_buyhouse(request):
    return render(request, "buy_house.html")

def to_unsoldhouse(request):
    return render(request, "Unsold_house.html")

def to_Secondhandhouse(request):
    return render(request, "Secondhand_house.html")

def to_addnew(request):
    return render(request,"add_newhouse.html")

def to_addrent(request):
    return render(request,"add_renthouse.html")

def to_addsec(request):
    return render(request,"add_sechouse.html")

def add_tablenew(request):
    if request.method == "POST":
        new = models.new()
        new.community = request.POST.get("community")
        new.price = request.POST.get("price")
        new.type = request.POST.get("type")
        new.area = request.POST.get("area")
        new.save()
        return render(request,"add_newhouse.html")
    return HttpResponse("添加成功！")


def add_tablesec(request):
    if request.method == "POST":
        second = models.sec()
        second.community = request.POST.get("community")
        second.price = request.POST.get("price")
        second.type = request.POST.get("type")
        second.area = request.POST.get("area")
        second.save()
        return render(request,"add_sechouse.html")
    return HttpResponse("添加成功！")

def add_tablerent(request):
    if request.method == "POST":
        rent = models.rent()
        rent.community = request.POST.get("community")
        rent.price = request.POST.get("price")
        rent.type = request.POST.get("type")
        rent.area = request.POST.get("area")
        rent.joint = eval(request.POST.get("joint"))
        rent.orientation = request.POST.get("orientation")
        rent.metro=eval(request.POST.get("metro"))
        rent.heating=eval(request.POST.get("heating"))
        rent.decoration=eval(request.POST.get("decoration"))
        rent.showing=eval(request.POST.get("showing"))
        rent.save()
        return render(request,"add_renthouse.html")
    return HttpResponse("添加成功！")

def to_test(request):
    return render(request,"test.html")

def add_tablebuy(request):
    if request.method == "POST":
        buy = models.buyinfo()
        buy.name = request.POST.get("name")
        buy.idcard = request.POST.get("idcard")
        buy.phone = request.POST.get("phone")
        buy.money = request.POST.get("money")
        buy.renttime = request.POST.get("renttime")
        buy.save()
        return render(request,"add_buyinfo.html")
    return HttpResponse("添加成功！")

def to_new(request):
    return render(request,"new.html")


def echarts(request):
    return render(request, 'echarts_over.html')

def echarts_json(request):
    results = models.new.objects.raw("SELECT AVG(price/house_new.`area`) AS areap,location AS id FROM `house_new` GROUP BY location;")
    data = []
    for re in results:
        area = re.id
        price = re.areap
        if area:
            data.append({'name':area,'value':price})
        # print(re.id,re.areap)
    return JsonResponse({'data':data})

def multy(request):
    results = models.new.objects.raw(
        "SELECT COUNT(*) AS cnt,TYPE AS id,AVG(price) AS avgprc,AVG(AREA) AS avgare FROM `house_rent` GROUP BY TYPE ORDER BY id;")
    data = {
        'id': [],
        'avgp': [],
        'avga': [],
        'cnt': [],
    }
    for re in results:
        data['id'].append(re.id)
        data['avga'].append(re.avgare)
        data['avgp'].append(float(re.avgprc))
        data['cnt'].append(re.cnt)
        # print(re.id,re.areap)
    return JsonResponse({'data': data})

def barstack(request):
    tags = ["延庆", "平谷", "房山", "丰台", "通州", "密云", "门头沟",
     "朝阳", "昌平", "怀柔", "大兴", "顺义", "海淀", "石景山"]
    sets = {
        'f03': {},
        'f34': {},
        'f46': {},
        'f68': {},
        'f8': {}
    }
    for tag in tags:
        for s in sets:
            sets[s].update({tag: 0})
    new_data = models.new.objects.raw("SELECT (@i:=@i+1) AS id,location,ELT(INTERVAL(price/AREA,0,3,4,6,8,10000), 'f03', 'f34','f46','f68', 'f8') AS idd, COUNT(*) AS cnt FROM `house_new` s,(SELECT @i:=0)t GROUP BY idd,location;")
    for d in new_data:
        print(d.idd,{d.location:d.cnt})
        sets[d.idd].update({d.location:d.cnt})
    data = {
        'f03': [],
        'f34': [],
        'f46': [],
        'f68': [],
        'f8': []
    }
    # all = {"延庆": 0, "平谷": 0, "房山": 0, "丰台": 0, "通州": 0, "密云": 0, "门头沟": 0,
    #  "朝阳": 0, "昌平": 0, "怀柔": 0, "大兴", "顺义", "海淀", "石景山"}
    for tag in tags:
        for s in sets:
            data[s].append(sets[s][tag])
    # for tag in tags:
    #     for s in sets:
    #         data[s].append(sets[s][tag])
    return JsonResponse(data)

# 租房整饼状图
def rosepie(request):
    # [
    #     {value: 40, name: 'rose 1'},
    #     {value: 33, name: 'rose 2'},
    # ]
    data = {'joint':[],'complete':[]}
    tags = ['近地铁','集中供暖','精装修','随时看房']
    lis = [[i1,i2,i3,i4] for i1 in [0,1] for i2 in [0,1] for i3 in [0,1] for i4 in [0,1]]
    for tag in lis:
        name = '-'.join([tag[i] * tags[i] for i in range(4) if tag[i]])
        joint = models.rent.objects.filter(
            metro=tag[0],heating=tag[1],decoration=tag[2],showing=tag[3],joint=1
        )
        complete = models.rent.objects.filter(
            metro=tag[0],heating=tag[1],decoration=tag[2],showing=tag[3],joint=0
        )
        data['joint'].append({'name':name,'value':len(joint)})
        data['complete'].append({'name':name,'value':len(complete)})
    return JsonResponse(data)
    # sec_data = models.sec.objects.all()

def ring(request):
    data = {
        'new': len(models.new.objects.all()),
        'sec': len(models.sec.objects.all()),
        'rent': len(models.rent.objects.all()),
    }
    return JsonResponse(data)

def priceandarea(request):
    new_data = models.new.objects.all()
    sec_data = models.sec.objects.all()
    new_data_lis = []
    sec_data_lis = []
    for data in new_data:
        new_data_lis.append([data.area,data.price])
    for data in sec_data:
        sec_data_lis.append([data.area,data.price])
    data = {
        'new': new_data_lis,
        'sec': sec_data_lis,
    }
    return JsonResponse(data)

def testadd(request):
    communitys = {}
    count = 0
    new_lis = models.new.objects.all()
    rent_lis = models.rent.objects.all()
    sec_lis = models.sec.objects.all()
    for l in new_lis:

        if l.location == '亦庄开发区':
            l.location = '大兴'
            l.save()

    #     print(count,end='')
    #     count += 1
    #     comm = l.community.split('·')[0]
    #     url = "https://bj.fang.ke.com/loupan/search/sug?query="+comm
    #     headers = {
    #         'Accept': 'application/json, text/javascript, */*; q=0.01',
    #         'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    #     }
    #     if communitys.get(l.community):
    #         l.location = communitys[l.community]
    #     else:
    #         try:
    #             json_data = requests.get(url=url,headers=headers)
    #             json_data = json_data.content.decode(json_data.encoding)
    #             json_data = json.loads(json_data)
    #             l.location = json_data['data'][0]['region']
    #             communitys.update({l.community:l.location})
    #             time.sleep(1+random.random())
    #         except Exception as e:
    #             print(e)
    #     l.save()
    # print(1)
    # for l in sec_lis:
    #     print(count,end='')
    #     count += 1
    #     comm = l.community.split('·')[0]
    #     url = "https://bj.fang.ke.com/loupan/search/sug?query=" + comm
    #     headers = {
    #         'Accept': 'application/json, text/javascript, */*; q=0.01',
    #         'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    #     }
    #     if communitys.get(l.community):
    #         l.location = communitys[l.community]
    #     else:
    #         try:
    #             json_data = requests.get(url=url, headers=headers)
    #             json_data = json_data.content.decode(json_data.encoding)
    #             json_data = json.loads(json_data)
    #             l.location = json_data['data'][0]['region']
    #             communitys.update({l.community: l.location})
    #             time.sleep(1 + random.random())
    #         except Exception as e:
    #             print(e)
    #     l.save()
    # print(1)
    # for l in rent_lis:
    #     print(count,end='')
    #     count += 1
    #     comm = l.community.split('·')[0]
    #     url = "https://bj.fang.ke.com/loupan/search/sug?query=" + comm
    #     headers = {
    #         'Accept': 'application/json, text/javascript, */*; q=0.01',
    #         'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    #     }
    #     if communitys.get(l.community):
    #         l.location = communitys[l.community]
    #     else:
    #         try:
    #             json_data = requests.get(url=url, headers=headers)
    #             json_data = json_data.content.decode(json_data.encoding)
    #             json_data = json.loads(json_data)
    #             l.location = json_data['data'][0]['region']
    #             communitys.update({l.community: l.location})
    #             time.sleep(1 + random.random())
    #         except Exception as e:
    #             print(e)
    #     l.save()
    # print(1)
