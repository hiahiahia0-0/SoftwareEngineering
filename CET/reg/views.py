from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse("<center><h1>reg index </h1></center>")

def template_test(request):
    return render(request, 'reg_template_test.html')

def reg_main(request):
    request.session["info"] = {'id':450450,'password':"testpassword"}
    info=request.session.get("info")
    if not info:
        return HttpResponse("请先登录!")
    return render(request, 'reg_main.html')

def ConfirmRegState(request):
    #todo 需要数据库根据用户名和密码查询是否是已报名，得到一个下面information形式的字典
    #todo 请先登录需要返回到登陆界面
    info=request.session.get("info")
    if not info:
        return HttpResponse("请先登录!")
    information={'flag':0,'state':0,'ID':450450450,'pwd':"testpassword"}
    #todo根据不同的状态码返回不同的页面
    if information['flag']==0:
        #未报名
        if information['state']==0:
            #todo 从数据库中获取全部信息
            fullinformation={'Name':'testname','school':'testschool','phone':'testphone','email':'testemail'}
            return render(request, 'checkinformation.html',{'n1':fullinformation})
        #已报名
        else :
            return render(request, 'reg_main.html')
    else:
        #todo 根据错误状态返回不同的页面码
        if information['flag']==1:
            return HttpResponse("ConfirmRegState错误状态码1")
    return render(request, 'reg_main.html',{'n1':information})

def SelectSite(request):
    #根据session信息获取用户对应的城市，然后查询数据库，返回该城市的考点信息
    info=request.session.get("info")
    if not info:
        return HttpResponse("请先登录!")
    #todo 从数据库中获取全部信息
    fullinformationlist=[
        {'Name':'testname1','school':'testschool1','phone':'testphone1','email':'testemail1'},
        {'Name':'testname2','school':'testschool2','phone':'testphone2','email':'testemail2'},
    ]
    return render(request, 'SelectSite.html',{'n1':fullinformationlist})

def TakeAnPosition(request):
    #print("启动")
    info = request.session.get("info")
    if not info:
        return HttpResponse("请先登录!")

    if request.method == 'POST':
        selectedData = request.POST.get('selectedData')  # 获取选中行的索引
        if selectedData:
            print(selectedData)
            #todo 向数据库申请一个考位，并返回申请成功与否，这里不搞这么复杂，直接生成订单
            #todo,向数据库申请创建一个订单，订单状态为未支付，订单号为随机生成的
            state=True
            order={'orderID':450450450,'examID':450450,'stuexamID':450450450,'paid':0,'payment':0}
            if state==True:
                return render(request, 'payorder.html', {'n1': order})
            else:
                return HttpResponse("申请订单失败！")
        else:
            return HttpResponse("未找到选中的数据或数据已过期！")
    else:
        return HttpResponse("请先选择考点！")

def PayOrder(request):
    info=request.session.get("info")
    if not info:
        return HttpResponse("请先登录!")
    if request.method == 'POST':
        order=request.POST.get('order')
        print(order)
        if order:
            print(order)
            #todo,向数据库申请支付一个订单，订单状态为已支付，订单号为随机生成的
            state=True
            if state==True:
                return HttpResponse("支付成功！")
            else:
                return HttpResponse("支付失败！")
        else:
            return HttpResponse("未找到订单或订单已过期！")
    else:
        return HttpResponse("请先选择考点！")
    