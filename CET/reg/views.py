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
            return render(request, 'checkinformation.html',fullinformation)
        #已报名
        else :
            return render(request, 'reg_main.html')
    else:
        #todo 根据错误状态返回不同的页面码
        if information['flag']==1:
            return HttpResponse("ConfirmRegState错误状态码1")
    return render(request, 'reg_main.html',information)

def SelectSite(request):
    return None