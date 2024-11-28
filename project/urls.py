from django.urls import path
from . import views

urlpatterns = [
    path('',views.student,name="student"),
    path('student/',views.student,name="student_"),
    path('subject/',views.subject,name="subject"),
    path('exam/',views.exam,name="exam"),
    path('form/',views.form_page,name="form"),


    path('exforsub/',views.exams_by_subject,name="exams_by_subject"),
    path('stforex/',views.students_by_exam,name="students_by_exam"),
    path('first_five/',views.first_five,name="first_five"),

]
