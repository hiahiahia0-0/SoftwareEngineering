from user import models as user_m
from exam import models as exam_m
from marking import models as marking_m

import time
from datetime import datetime
from django.utils import timezone
from django.db  import models
from typing import List, Optional,Tuple


'''
本文件功能：
    封装如下的数据库操作: ( * 代表已完成, - 代表未完成 )
    * user
        * 学生的增删改查(主键)
        * 学生查(通过手机号)
        * 老师的增删改查(主键)
        * 老师查(通过手机号)
    * exam
        * 题目的增删改查
        * 试卷的增删改查
        * 考试安排的增删改查 (注意外键约束)
        * 订单记录的增删查 (注意外键约束)
<<<<<<< HEAD
        * 获取所有考试安排
=======
        * 查询所有题目
        * 查询所有试卷
        * 查询所有考试安排
>>>>>>> 48b74f5179aa582ffcf10e77a1531744ad15fcc4
        * 获取某学生的所有考试安排
    * marking
        * 答题情况的增删改查 (注意外键约束)
        * 考试成绩的增删改查 (注意外键约束)
        * 获取所有的考试成绩
        * 获取某学生的所有考试成绩
    - reg
        - 暂时不需要单独的数据库
    - manager
        - 暂时不需要单独的数据库
    
    此外, 还有:
    * 异常捕获
    * 日志记录
    
    注意: 
    * 返回值代表不同信息, 请开发者根据返回值判断是否成功
'''

NOT_EXIST = -1
DUPLICATE = -2
FAIL = 0
SUCCESS = 1

LOG_ERR = 0
LOG_OK = 1

def sys_log(msg, type):
    # 高亮打印当前时间和信息
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if type == LOG_ERR:
        print("\033[1;31m LOG_ERR:" + now + ": " + msg + "\033[0m")
    else:
        print("\033[1;32m LOG:" + now + ": " + msg + "\033[0m")

class user:
    def __init__(self):
        pass
    
    @staticmethod
    def select_stu_by_phone(phone) -> Tuple[Optional[user_m.Student], int]:
        try:
            try:
                stu =  user_m.Student.objects.get(phone=phone)
            except user_m.Student.DoesNotExist:
                sys_log('学生查询不存在', LOG_ERR)
                return None ,NOT_EXIST
            sys_log('学生查询成功', LOG_OK)
            return stu , SUCCESS
        except:
            sys_log('学生查询失败', LOG_ERR)
            return None,FAIL
    
    @staticmethod
    def select_tea_by_phone(phone) -> Tuple[Optional[user_m.Teacher], int]:
        try:
            try:
                tea =  user_m.Teacher.objects.get(phone=phone)
            except user_m.Teacher.DoesNotExist:
                sys_log('教师查询不存在', LOG_ERR)
                return None,NOT_EXIST
            sys_log('教师查询成功', LOG_OK)
            return tea ,SUCCESS
        except:
            sys_log('教师查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def select_stu_by_id(id) -> tuple[Optional[user_m.Student] , int]:
        try:
            try :
                stu =  user_m.Student.objects.get(id=id)
            except user_m.Student.DoesNotExist:
                sys_log('学生查询不存在', LOG_ERR)
                return None ,NOT_EXIST
            sys_log('学生查询成功', LOG_OK)
            return stu , SUCCESS
        except:
            sys_log('学生查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def select_tea_by_id(id) -> Tuple[Optional[user_m.Teacher], int]:
        try:
            try :
                tea =  user_m.Teacher.objects.get(id=id)
            except user_m.Teacher.DoesNotExist:
                sys_log('教师查询不存在', LOG_ERR)
                return None,NOT_EXIST
            sys_log('教师查询成功', LOG_OK)
            return tea ,SUCCESS
        except:
            sys_log('教师查询失败', LOG_ERR)
            return None, FAIL

    @staticmethod
    def insert_stu(self_num: int, name: str, school: str, password: str, phone: str, email: str) -> tuple[Optional[user_m.Student] , int] : # id是自增的，不用管
        try:
            check = user_m.Student.objects.get(phone=phone)
            if check:
                sys_log('学生已存在', LOG_ERR)
                return None, DUPLICATE
        except :
            pass

        try:
            stu = user_m.Student(self_number=self_num, name=name, school=school, password=password, phone=phone, email=email)
            stu.save()
            sys_log('学生添加成功', LOG_OK)
            return stu, SUCCESS
        except Exception as e:
            # 显示错误
            # print(e)
            sys_log('学生添加失败',LOG_ERR)
            return None, FAIL



    @staticmethod
    def insert_tea(name: str, phone: str, password: str) -> tuple[Optional[user_m.Teacher] , int]: # id自增
        try:
            check = user_m.Teacher.objects.get(phone=phone)
            if check:
                sys_log('教师已存在', LOG_ERR)
                return None, DUPLICATE
        except:
            pass
        
        try:
            tea = user_m.Teacher(name=name, phone=phone, password=password)
            tea.save()
            sys_log('教师添加成功', LOG_OK)
            return tea, SUCCESS
        except:
            sys_log('教师添加失败', LOG_ERR)
            return None, FAIL

    @staticmethod
    def update_stu(self_number:int,name: str, school: str, password: str, phone: str, email: str,id: int) -> int:
        try:
            try:
                stu = user_m.Student.objects.get(id=id)
            except user_m.Student.DoesNotExist:
                sys_log('学生查询不存在', LOG_ERR)
                return NOT_EXIST
            stu.name = name
            stu.self_number = self_number
            stu.school = school
            stu.password = password
            stu.phone = phone
            stu.email = email
            stu.save()
            sys_log('学生修改成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('学生修改失败', LOG_ERR)
            return FAIL

    @staticmethod
    def update_tea(id: int, name: str, phone: str, password: str) -> int:
        try:
            try:
                tea = user_m.Teacher.objects.get(id=id)
            except user_m.Teacher.DoesNotExist:
                sys_log('教师查询不存在', LOG_ERR)
                return NOT_EXIST
            tea.name = name
            tea.phone = phone
            tea.password = password
            tea.save()
            sys_log('教师修改成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('教师修改失败', LOG_ERR)
            return FAIL

    @staticmethod
    def delete_stu(id) -> int:
        try:
            try:
                stu = user_m.Student.objects.get(id=id)
            except user_m.Student.DoesNotExist:
                sys_log('学生查询不存在', LOG_ERR)
                return NOT_EXIST
            stu.delete()
            sys_log('学生删除成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('学生删除失败', LOG_ERR)
            return FAIL

    @staticmethod
    def delete_tea(id) -> int:
        try:
            try:
                tea = user_m.Teacher.objects.get(id=id)
            except user_m.Teacher.DoesNotExist:
                sys_log('教师查询不存在', LOG_ERR)
                return NOT_EXIST
            tea.delete()
            sys_log('教师删除成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('教师删除失败', LOG_ERR)
            return FAIL

class exam:
    def __init__(self):
        pass
    
    @staticmethod
    def select_all_exam() -> Tuple[Optional[models.QuerySet[exam_m.Exam]], int]:
        try:
            try:
                exams = exam_m.Exam.objects.all()
            except exam_m.Exam.DoesNotExist:
                sys_log('所有考试查询不存在', LOG_ERR)
                return None,NOT_EXIST
            sys_log('所有考试查询成功', LOG_OK)
            
            return exams, SUCCESS
        except:
            sys_log('所有考试查询失败', LOG_ERR)
            return None,FAIL
    
    @staticmethod
    def select_all_que() -> Tuple[Optional[models.QuerySet[exam_m.Question]], int]:
        try:
            try:
                que = exam_m.Question.objects.all()
            except exam_m.Question.DoesNotExist:
                sys_log('所有题目查询不存在', LOG_ERR)
                return None,NOT_EXIST
            sys_log('所有题目查询成功', LOG_OK)
            return que, SUCCESS
        except:
            sys_log('所有题目查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def select_all_paper() -> Tuple[Optional[models.QuerySet[exam_m.Paper]], int]:
        try:
            try:
                paper = exam_m.Paper.objects.all()
            except exam_m.Paper.DoesNotExist:
                sys_log('所有试卷查询不存在', LOG_ERR)
                return None,NOT_EXIST
            sys_log('所有试卷查询成功', LOG_OK)
            return paper, SUCCESS
        except:
            sys_log('所有试卷查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def select_all_exam_by_stu(stu_id) -> Tuple[Optional[List[Optional[exam_m.Exam]]], int]:
        # for debug use
        # try:
        #     try:
        #         exams = exam_m.Exam.objects.all()
        #     except exam_m.Exam.DoesNotExist:
        #         sys_log('所有考试查询不存在', LOG_ERR)
        #         return None,NOT_EXIST
        #     sys_log('所有考试查询成功', LOG_OK)
            
        #     return exams, SUCCESS
        # except:
        #     sys_log('所有考试查询失败', LOG_ERR)
        #     return None,FAIL

        # true operate
        try:
            try:
                exam_odrs = exam_m.ExamOrder.objects.filter(student_id=stu_id)
            except exam_m.Exam.DoesNotExist:
                sys_log('学生考试查询不存在', LOG_ERR)
                return None,NOT_EXIST
            sys_log('学生所有考试查询成功', LOG_OK)
            exams = [exam_odr.exam for exam_odr in exam_odrs]
            return exams,SUCCESS if exams != None and len(exams)>0 else NOT_EXIST
        except:
            sys_log('所有考试查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def select_exam_by_id(id) -> Tuple[Optional[exam_m.Exam], int]:
        try:
            try :
                exam =  exam_m.Exam.objects.get(id=id)
            except exam_m.Exam.DoesNotExist:
                sys_log('考试查询不存在', LOG_ERR)
                return None,NOT_EXIST
            else:
                sys_log('考试查询成功', LOG_OK)
                return exam ,SUCCESS
        except:
            sys_log('考试查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def insert_exam(date:datetime, place:str, paper:int, max_students:int) -> int:
        try:
            try:
                p = exam_m.Paper.objects.get(id=paper)
            except exam_m.Paper.DoesNotExist:
                sys_log('外键约束：试卷不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：试卷', LOG_ERR)
                return FAIL
            exam = exam_m.Exam(date=date, place=place, paper=p, max_students=max_students)
            exam.save()
            sys_log('考试添加成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('考试添加失败', LOG_ERR)
            return FAIL

    @staticmethod
    def update_exam(id: int, date: datetime, place: str, paper_id: int, max_students: int) -> int:
        try:
            try:
                exam = exam_m.Exam.objects.get(id=id)
            except exam_m.Exam.DoesNotExist:
                sys_log('考试查询不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：考试', LOG_ERR)
                return FAIL

            exam.date = date
            exam.place = place

            try:
                exam.paper = exam_m.Paper.objects.get(id=paper_id)
            except exam_m.Paper.DoesNotExist:
                sys_log('试卷不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：试卷', LOG_ERR)
                return FAIL

            exam.max_students = max_students
            exam.save()
            sys_log('考试修改成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('考试修改失败', LOG_ERR)
            return FAIL

    @staticmethod
    def delete_exam(id) -> int:
        try:
            try:
                exam = exam_m.Exam.objects.get(id=id)
            except exam_m.Exam.DoesNotExist:
                sys_log('考试查询不存在', LOG_ERR)
                return NOT_EXIST
            exam.delete()
            sys_log('考试删除成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('考试删除失败', LOG_ERR)
            return FAIL

    @staticmethod
    def select_question_by_id(id) -> Tuple[Optional[exam_m.Question], int]:
        try:
            try :
                question =  exam_m.Question.objects.get(id=id)
            except exam_m.Question.DoesNotExist:
                sys_log('题目查询不存在', LOG_ERR)
                return None,NOT_EXIST
            
            sys_log('题目查询成功', LOG_OK)
            return question ,SUCCESS
        except:
            sys_log('题目查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def insert_question(type:int, question:str, answer:str) -> int:
        try:
            q =  exam_m.Question(type=type, question=question, answer=answer)
            q.save()
            sys_log('题目添加成功', LOG_OK)
            return  SUCCESS
        except:
            sys_log('题目添加失败', LOG_ERR)
            return FAIL

    @staticmethod
    def update_question(id:int, type:int, question:str, answer:str) -> int:
        try:
            try:
                q = exam_m.Question.objects.get(id=id)
            except exam_m.Question.DoesNotExist:
                sys_log('题目查询不存在', LOG_ERR)
                return NOT_EXIST
            q.type = type
            q.question = question
            q.answer = answer
            q.save()
            sys_log('题目修改成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('题目修改失败', LOG_ERR)
            return FAIL

    @staticmethod
    def delete_question(id) -> int:
        try:
            try:
                q = exam_m.Question.objects.get(id=id)
            except exam_m.Question.DoesNotExist:
                sys_log('题目查询不存在', LOG_ERR)
                return NOT_EXIST
            q.delete()
            sys_log('题目删除成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('题目删除失败', LOG_ERR)
            return FAIL

    @staticmethod
    def select_paper_by_id(id) -> Tuple[Optional[exam_m.Paper], int]:
        try:
            try :
                paper =  exam_m.Paper.objects.get(id=id)
            except exam_m.Paper.DoesNotExist:
                sys_log('试卷查询不存在', LOG_ERR)
                return None,NOT_EXIST
            sys_log('试卷查询成功', LOG_OK)
            return paper ,SUCCESS
        except:
            sys_log('试卷查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def insert_paper(question_ids:str, type:int) -> int:
        try:
            paper = exam_m.Paper(question_ids=question_ids, type=type)
            paper.save()
            sys_log('试卷添加成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('试卷添加失败', LOG_ERR)
            return FAIL

    @staticmethod
    def update_paper(id:int, question_ids:str, type:int) -> int:
        try:
            try:
                p = exam_m.Paper.objects.get(id=id)
            except exam_m.Paper.DoesNotExist:
                sys_log('试卷查询不存在', LOG_ERR)
                return NOT_EXIST
            p.question_ids = question_ids
            p.type = type
            p.save()
            sys_log('试卷修改成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('试卷修改失败', LOG_ERR)
            return FAIL

    @staticmethod
    def delete_paper(id) -> int:
        try:
            try:
                p = exam_m.Paper.objects.get(id=id)
            except exam_m.Paper.DoesNotExist:
                sys_log('试卷查询不存在', LOG_ERR)
                return NOT_EXIST
            p.delete()
            sys_log('试卷删除成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('试卷删除失败', LOG_ERR)
            return FAIL

    @staticmethod
    def select_ExamOder_by_id(id) -> Tuple[Optional[exam_m.ExamOrder], int]:
        try:
            try :
                exam_order =  exam_m.ExamOrder.objects.get(id=id)
            except exam_m.ExamOrder.DoesNotExist:
                sys_log('考试订单查询不存在', LOG_ERR)
                return None,NOT_EXIST
            else:
                sys_log('考试订单查询成功', LOG_OK)
                return exam_order ,SUCCESS
        except:
            sys_log('考试订单查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def insert_ExamOder(exam_id:int, student_id:int, paid:bool, payment:float) -> int:
        try:
            try:
                e = exam_m.Exam.objects.get(id=exam_id)
            except exam_m.Exam.DoesNotExist:
                sys_log('外键约束：考试不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：考试', LOG_ERR)
                return FAIL
            try :
                s = user_m.Student.objects.get(id=student_id)
            except user_m.Student.DoesNotExist:
                sys_log('外键约束：学生不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：学生', LOG_ERR)
                return FAIL

            exam_order = exam_m.ExamOrder(exam=e, student=s, paid=paid, payment=payment ,pay_time=timezone.now())
            exam_order.save()
            sys_log('考试订单添加成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('考试订单添加失败', LOG_ERR)
            return FAIL

    @staticmethod
    def delete_ExamOder(id) -> int:
        try:
            try:
                exam_order = exam_m.ExamOrder.objects.get(id=id)
            except exam_m.ExamOrder.DoesNotExist:
                sys_log('考试订单查询不存在', LOG_ERR)
                return NOT_EXIST
            exam_order.delete()
            sys_log('考试订单删除成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('考试订单删除失败', LOG_ERR)
            return FAIL

class marking:
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def select_all_EScore() -> Tuple[Optional[models.QuerySet[marking_m.ExamScore]], int]:
        try:
            try:
                exam_scores = marking_m.ExamScore.objects.all()
            except marking_m.ExamScore.DoesNotExist:
                sys_log('所有考试成绩查询不存在', LOG_ERR)
                return None,NOT_EXIST
            sys_log('所有考试成绩查询成功', LOG_OK)
            return exam_scores, SUCCESS
        except:
            sys_log('所有考试成绩查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def select_all_EScore_by_stu(stu_id) -> Tuple[Optional[models.QuerySet[marking_m.ExamScore]], int]:
        try:
            try:
                exam_scores = marking_m.ExamScore.objects.filter(student_id=stu_id)
            except marking_m.ExamScore.DoesNotExist:
                sys_log('学生考试成绩查询不存在', LOG_ERR)
                return None,NOT_EXIST
            sys_log('学生考试成绩查询成功', LOG_OK)
            return exam_scores, SUCCESS
        except:
            sys_log('学生考试成绩查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def select_AnswerRecord_by_id(id) -> Tuple[Optional[marking_m.AnswerRecord], int]:
        try:
            try :
                answer_record =  marking_m.AnswerRecord.objects.get(id=id)
            except marking_m.AnswerRecord.DoesNotExist:
                sys_log('答题记录查询不存在', LOG_ERR)
                return None,NOT_EXIST
            else:
                sys_log('答题记录查询成功', LOG_OK)
                return answer_record ,SUCCESS
        except:
            sys_log('答题记录查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def insert_AnswerRecord(exam_id:int, student_id:int , question_id:int, is_right:bool) -> int:
        try:
            try:
                e = exam_m.Exam.objects.get(id=exam_id)
            except exam_m.Exam.DoesNotExist:
                sys_log('外键约束：考试不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：考试', LOG_ERR)
                return FAIL
            try :
                s = user_m.Student.objects.get(id=student_id)
            except user_m.Student.DoesNotExist:
                sys_log('外键约束：学生不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：学生', LOG_ERR)
                return FAIL
            try :
                q = exam_m.Question.objects.get(id=question_id)
            except exam_m.Question.DoesNotExist:
                sys_log('外键约束：题目不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：题目', LOG_ERR)
                return FAIL

            answer_record = marking_m.AnswerRecord(exam=e, student_id=s, question_id=q, is_right=is_right)
            answer_record.save()
            sys_log('答题记录添加成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('答题记录添加失败', LOG_ERR)
            return FAIL

    @staticmethod
    def delete_AnswerRecord(id) -> int:
        try:
            try:
                answer_record = marking_m.AnswerRecord.objects.get(id=id)
            except marking_m.AnswerRecord.DoesNotExist:
                sys_log('答题记录查询不存在', LOG_ERR)
                return NOT_EXIST
            answer_record.delete()
            sys_log('答题记录删除成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('答题记录删除失败', LOG_ERR)
            return FAIL

    @staticmethod
    def update_AnswerRecord(id:int, eaxm_id:int , student_id:int, question_id:int, is_right:bool) -> int:
        try:
            try:
                answer_record = marking_m.AnswerRecord.objects.get(id=id)
            except marking_m.AnswerRecord.DoesNotExist:
                sys_log('答题记录查询不存在', LOG_ERR)
                return NOT_EXIST

            try:
                e = exam_m.Exam.objects.get(id=eaxm_id)
            except exam_m.Exam.DoesNotExist:
                sys_log('外键约束：考试不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：考试', LOG_ERR)
                return FAIL
            try :
                s = user_m.Student.objects.get(id=student_id)
            except user_m.Student.DoesNotExist:
                sys_log('外键约束：学生不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：学生', LOG_ERR)
                return FAIL
            try :
                q = exam_m.Question.objects.get(id=question_id)
            except exam_m.Question.DoesNotExist:
                sys_log('外键约束：题目不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：题目', LOG_ERR)
                return FAIL

            answer_record.exam = e
            answer_record.student_id = s
            answer_record.question_id = q
            answer_record.is_right = is_right
            answer_record.save()
            sys_log('答题记录修改成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('答题记录修改失败', LOG_ERR)
            return FAIL

    @staticmethod
    def select_ExamScore_by_id(id) -> Tuple[Optional[marking_m.ExamScore], int]:
        try:
            try :
                exam_score =  marking_m.ExamScore.objects.get(id=id)
            except marking_m.ExamScore.DoesNotExist:
                sys_log('考试成绩查询不存在', LOG_ERR)
                return None,NOT_EXIST
            else:
                sys_log('考试成绩查询成功', LOG_OK)
                return exam_score ,SUCCESS
        except:
            sys_log('考试成绩查询失败', LOG_ERR)
            return None,FAIL

    @staticmethod
    def insert_ExamScore(exam_id:int, student_id:int, teacher_id:int, score:int) -> int:
        try:
            try:
                e = exam_m.Exam.objects.get(id=exam_id)
            except exam_m.Exam.DoesNotExist:
                sys_log('外键约束：考试不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：考试', LOG_ERR)
                return FAIL
            try :
                s = user_m.Student.objects.get(id=student_id)
            except user_m.Student.DoesNotExist:
                sys_log('外键约束：学生不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：学生', LOG_ERR)
                return FAIL
            try :
                t = user_m.Teacher.objects.get(id=teacher_id)
            except user_m.Teacher.DoesNotExist:
                sys_log('外键约束：老师不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：老师', LOG_ERR)
                return FAIL

            exam_score = marking_m.ExamScore(exam_id=e, student_id=s, teacher_id=t, score=score)
            exam_score.save()
            sys_log('考试成绩添加成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('考试成绩添加失败', LOG_ERR)
            return FAIL

    @staticmethod
    def delete_ExamScore(id) -> int:
        try:
            try:
                exam_score = marking_m.ExamScore.objects.get(id=id)
            except marking_m.ExamScore.DoesNotExist:
                sys_log('考试成绩查询不存在', LOG_ERR)
                return NOT_EXIST
            exam_score.delete()
            sys_log('考试成绩删除成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('考试成绩删除失败', LOG_ERR)
            return FAIL

    @staticmethod
    def update_ExamScore(id:int, exam_id:int, student_id:int, teacher_id:int, score:int) -> int:
        try:
            try:
                exam_score = marking_m.ExamScore.objects.get(id=id)
            except marking_m.ExamScore.DoesNotExist:
                sys_log('考试成绩查询不存在', LOG_ERR)
                return NOT_EXIST

            try:
                e = exam_m.Exam.objects.get(id=exam_id)
            except exam_m.Exam.DoesNotExist:
                sys_log('外键约束：考试不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：考试', LOG_ERR)
                return FAIL
            try :
                s = user_m.Student.objects.get(id=student_id)
            except user_m.Student.DoesNotExist:
                sys_log('外键约束：学生不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：学生', LOG_ERR)
                return FAIL
            try :
                t = user_m.Teacher.objects.get(id=teacher_id)
            except user_m.Teacher.DoesNotExist:
                sys_log('外键约束：老师不存在', LOG_ERR)
                return NOT_EXIST
            except:
                sys_log('未知错误：老师', LOG_ERR)
                return FAIL

            exam_score.exam_id = e
            exam_score.student_id = s
            exam_score.teacher_id = t
            exam_score.score = score
            exam_score.save()
            sys_log('考试成绩修改成功', LOG_OK)
            return SUCCESS
        except:
            sys_log('考试成绩修改失败', LOG_ERR)
            return FAIL