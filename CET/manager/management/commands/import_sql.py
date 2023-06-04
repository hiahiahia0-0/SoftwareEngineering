from django.core.management.base import BaseCommand
from django.db import connection
from manager import db_operation as db
from datetime import datetime ,time


class Command(BaseCommand):
    help = 'Import Test SQL file'

    def handle(self, *args, **options):
        print("\033[1;32mStarting Importing Test SQL file\033[0m")

        stu1,err = db.user.insert_stu(11111, '学生1', 'NKU', '123456',
                           '111', '1@mail.nankai.edu.cn')
        stu2,err = db.user.insert_stu(22222, '学生2', 'NKU', '123456',
                           '112', '2@mail.nankai.edu.cn')
        stu3,err = db.user.insert_stu(33333, '学生3', 'NKU', '123456',
                           '113', '3@mail.nankai.edu.cn')
        stu4,err = db.user.insert_stu(44444, '学生4', 'NKU', '123456',
                           '114', '4@mail.nankai.edu.cn')
        stu5,err = db.user.insert_stu(55555, '学生5', 'NKU', '123456',
                           '115', '5@mail.nankai.edu.cn')

        tea1,err = db.user.insert_tea('老师1', '121', '123456')
        tea2,err = db.user.insert_tea('老师2', '122', '123456')
        print("\033[1;32mFinished Importing Users\033[0m")

        db.exam.insert_question(0, '选择题:请选A\nA.请选A\nB.请选A\nC.请选A\nD.请选A\n', 'A')
        db.exam.insert_question(0, '选择题:请选B\nA.请选B\nB.请选B\nC.请选B\nD.请选B\n', 'B')
        db.exam.insert_question(0, '选择题:请选C\nA.请选C\nB.请选C\nC.请选C\nD.请选C\n', 'C')
        db.exam.insert_question(0, '选择题:请选D\nA.请选D\nB.请选D\nC.请选D\nD.请选D\n', 'D')
        db.exam.insert_question(1, '填空题:请输入1', '1')
        db.exam.insert_question(1, '填空题:请输入2', '2')
        db.exam.insert_question(1, '填空题:请输入3', '3')
        db.exam.insert_question(1, '填空题:请输入4', '4')
        que_id = db.exam_m.Question.objects.latest('id').id
        if que_id:
            db.exam.insert_paper(','.join([str(que_id-7), str(que_id-6), str(que_id-5), str(que_id-4)]), 0)
            db.exam.insert_paper(','.join([str(que_id-3), str(que_id-2), str(que_id-1), str(que_id)]), 1)
        else:
            print("\033[1;31mError Importing Papers\033[0m")

        date_string = "2077-01-01 12:00:00"
        date_format = "%Y-%m-%d %H:%M:%S"
        date_1 = datetime.strptime(date_string, date_format)
        papers, err = db.exam.select_all_paper()
        pid1 = 0
        pid2 = 0
        if papers and papers.count()>1 and err:
            pid1 = papers[papers.count()-1].id
            pid2 = papers[papers.count()-2].id
            start_time = time(9, 0, 0)
            end_time = time(10, 0, 0)
            db.exam.insert_exam('eTJU',date_1,start_time,end_time,True,False, 'TJU', pid1, 10)
            db.exam.insert_exam('eNKU',datetime.now(),start_time,end_time,True,False, 'NKU', pid2, 10)
        else :
            print("\033[1;31mError Importing Exam\033[0m")
        
        exams, err = db.exam.select_all_exam()
        eid1 = 0
        eid2 = 0
        stu1_id = stu1.id if stu1 else 0
        stu2_id = stu2.id if stu2 else 0
        if exams and exams.count()>1 and err and stu1_id and stu2_id:
            eid1 = exams[exams.count()-1].id
            eid2 = exams[exams.count()-2].id
            db.exam.insert_ExamOder(eid1, stu1_id, True, 25.0)
            db.exam.insert_ExamOder(eid2, stu2_id, False, 0.0)
        else:
            print("\033[1;32mError Importing Exam oder\033[0m")

        print("\033[1;32mFinished Importing Exam\033[0m")

        # stu 2 joined exam 2
        ques , err = db.exam.select_all_que()
        if ques and ques.count()>1 and err:
            db.marking.insert_AnswerRecord(eid2,stu2_id,ques[ques.count()-1].id,True)
            db.marking.insert_AnswerRecord(eid2,stu2_id,ques[ques.count()-2].id,False)
            db.marking.insert_AnswerRecord(eid2,stu2_id,ques[ques.count()-3].id,False)
            db.marking.insert_AnswerRecord(eid2,stu2_id,ques[ques.count()-4].id,False)
            db.marking.insert_ExamScore(eid2,stu2_id,tea1.id if tea1 else 0,25)
        else :
            print("\033[1;32mError Importing Question\033[0m")
        print("\033[1;32mFinished Importing Marking\033[0m")

        print("\033[1;32mFinished Importing Test SQL file\033[0m")

