from django.shortcuts import render
from django.http import HttpResponse
from manager import models as manager_m
# Create your views here.

def hello(request):
    return render(request, 'index.html')

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        test = request.POST.get('test')
        item = manager_m.TestTable(name=name, test=test)
        item.save()
        print("Item added successfully")
        return HttpResponse('<script>alert("Item added successfully")</script>')
    else:
        return render(request, 'test.html')

def test(request): # test function
    items = manager_m.TestTable.objects.all()
    return render(request, 'test.html', {'items': items})