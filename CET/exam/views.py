from django.shortcuts import render
from django.http import HttpResponse
from exam import models as exam_m
from manager import db_operation


"""
    在进行考试之前需要有manage对用户登录的凭证(如session等)进行验证，这里是合法性验证后的情况
    * exam_info: 
        判断的对应的用户已经报名的考试信息，如果某一项满足考试要求（如可以参加考试的时间），则有可以
        进行跳转的按钮，进入考试页面。
    
    * exam_detail:
        显示对应的考试试题，支持用户进行答题操作。并且有考试最大作答时间的约束，超时自动提交作答情况。

    * exam_submit:
        对应试者的答题情况进行统计展示，包括每道题作答的答案，整套试卷的作答时间等信息。浏览结束后跳
        转到exam_info对应的界面

"""
def exam_info(request):
    # 模拟session
    # request.session['stu_id']='123456';
    stu_id=request.session.get('stu_id')
    exams,status=db_operation.exam.select_all_exam_by_stu(stu_id)
    print(exams)
    if status==db_operation.SUCCESS:
        return render(request,'exam/exam_info.html',{'exams':exams})
    else:
        return HttpResponse("您没有报名的考试，请通过报考系统报名后重试！")
    

def exam_detail(request,exam_id):
    exam,status=db_operation.exam.select_exam_by_id(exam_id)
    if status!=db_operation.SUCCESS:
        return HttpResponse("在线考试载入错误，请稍后重试！")
    
    paper,status=db_operation.exam.select_paper_by_id(exam.paper)
    if status!=db_operation.SUCCESS:
        return HttpResponse("在线考试试卷载入错误，请稍后重试！")   
    
    questions=paper.question_ids
    questions=questions[1:-1] # 去除首尾的"["、"]"
    items=questions.split(',')
    question_ids=[(int)(item) for item in items]
    
    paper_questions=[]
    for question_id in question_ids:
        question_info,status=db_operation.exam.select_question_by_id(question_id)
        if status==db_operation.SUCCESS:
            paper_questions.append(question_info)
    
    if paper_questions==[]:
        return HttpResponse("在线考试试卷题目载入错误，请稍后重试！")
    
    return render(request,'exam/exam_detail.html',{'questions':paper_questions})
def exam_d(request):
    return render(request,'exam/exam_detail.html')
def exam_s(request):
    if request.method=='POST':
        return render(request,'exam/exam_submitted.html')
    return HttpResponse("在线考试提交信息载入错误，请稍后重试！")
def exam_submit(request,exam_id,use_time):
    exam,status=db_operation.exam.select_exam_by_id(exam_id)
    if status!=db_operation.SUCCESS:
        return HttpResponse("在线考试信息获取错误，请稍后重试！")
    
    return render(request,'exam/exam_submitted.html',{'exam':exam},{'use_time':use_time})
















