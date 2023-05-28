from django.shortcuts import render, get_object_or_404
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
    request.session['stu_id']='123456';
    stu_id=request.session.get('stu_id');
    exams,status=db_operation.exam.select_all_exam_by_stu(stu_id);
    if status==db_operation.SUCCESS:
        return render(request,'exam/exam_info.html',{'examns':exams});
    else:
        return get_object_or_404(exam_m.Exam);
    

def exam_detail(request):
    return render(request,'exam/exam_detail.html');

def exam_submit(request):
    return render(request,'exam/exam_submit.html');
















