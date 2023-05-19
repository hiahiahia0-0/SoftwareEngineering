from django.shortcuts import render
from django.http import HttpResponse
from manager import models as manager_m
# Create your views here.

def hello(request):
    return HttpResponse("<center><h1>Hello world ! </h1></center>")

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        test = request.POST.get('test')
        item = manager_m.TestTable(name=name, test=test)
        item.save()
        print("Item added successfully")
        return HttpResponse('Item added successfully')
    else:
        return render(request, 'test.html')

def show_items(request):
    items = manager_m.TestTable.objects.all()
    return render(request, 'test.html', {'items': items})