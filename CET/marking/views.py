from django.shortcuts import render
from django.http import HttpResponse
from manager import db_operation
from django.shortcuts import render
from marking import models as marking_m

 
def finish(request):
    context = {}
    context['finish'] = '阅卷成功！'
    if request.POST:
        context['ans0'] = request.POST['q0']
        context['ans1'] = request.POST['q1']
        context['ans2'] = request.POST['q2']

        #更新答题记录
        sel_ids = [1,2,3]
        try:
            record = marking_m.AnswerRecord.objects.get(id=sel_ids[0])
            record.is_right = context['ans0']
            record.save()
            record = marking_m.AnswerRecord.objects.get(id=sel_ids[1])
            record.is_right = context['ans1']
            record.save()
            record = marking_m.AnswerRecord.objects.get(id=sel_ids[2])
            record.is_right = context['ans2']
            record.save()
            db_operation.sys_log('答题记录修改成功', db_operation.LOG_OK)
        except:
            db_operation.sys_log('答题记录修改失败', db_operation.LOG_ERR)

    return render(request, 'marking/finish.html', context)

def mark(request):
    sel_ids = [1,2,3]
    records = []

    for sel_id in sel_ids:
        record,status=db_operation.marking.select_AnswerRecord_by_id(sel_id)
        records.append(record)

    return render(request, 'marking/index.html', {"record_list":records})
