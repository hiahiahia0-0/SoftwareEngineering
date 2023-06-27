from django.shortcuts import render
from django.http import HttpResponse
from manager import db_operation
from django.shortcuts import render
from marking import models as marking_m
from django.db.models import Avg,Max,Min,Count,Sum  #   引入函数

sel_ids = []

def finish(request):
    print("sel_ids:")
    print(sel_ids)
    context = {}
    context['finish'] = '阅卷成功！'
    if request.POST:
        context['ans0'] = request.POST['q0']
        context['ans1'] = request.POST['q1']
        context['ans2'] = request.POST['q2']

        #更新答题记录
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
    # session验证
    # phone_id=request.session.get("user_tea")
    # print(phone_id)
    # tea_info,state=db_operation.user.select_tea_by_phone(phone_id)
    # if state!=db_operation.SUCCESS:
    #     return HttpResponse("用户不存在")

    exam_ids = []
    marking_exam = marking_m.AnswerRecord.objects.values("exam_id").annotate(exam_num = Count("id"))
    print(marking_exam)
    for marking_exams in marking_exam :
        if marking_exams["exam_num"]>=3:
            exam_ids.append(marking_exams['exam_id'])
    if len(exam_ids) <2:
        return HttpResponse("不存在符合阅卷标准的考卷")

    exams = []
    for exam_id in exam_ids:
        exam,status = db_operation.exam.select_exam_by_id(exam_id)
        exams.append(exam)

    return render(request, 'marking/index.html', {"exam_list":exams})


def mark_exam(request):
    # print("ex:")
    # print(request.POST['ex'])
    records = []
    sel_ids.clear()
    sel_ids_t = marking_m.AnswerRecord.objects.filter(exam_id=request.POST['ex'])
    for sel_ids_t0 in sel_ids_t:
        sel_ids.append(sel_ids_t0.id)
    # print(sel_ids)

    for sel_id in sel_ids:
        record,status=db_operation.marking.select_AnswerRecord_by_id(sel_id)
        records.append(record)

    return render(request, 'marking/mark_exam.html', {"record_list":records})
