from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject, Student, Exam
from .forms import ExamForm
# Create your views here.

def subject(request):
    return render(request,"project/subject.jinja",{
        'subjects': Subject.objects.all()
    })

def student(request):
    return render(request,"project/student.jinja",{
        'students': Student.objects.all()
    })

def exam(request):
    return render(request,"project/exam.jinja",{
        'exams': Exam.objects.all()
    })


def form_page(request):
    form=ExamForm(request.POST)
    if form.is_valid():
        form.save()
    form=ExamForm()
    return render(request,"project/form.jinja",{
        'form':form,
    })
    

def exams_by_subject(request):
    subjects = Subject.objects.all()

    selected_subject = request.GET.get('subject')

    exams = []

    if selected_subject:
        exams = Exam.objects.filter(subject__name=selected_subject)

    return render(request, 'project/exams_by_subject.jinja', {
        'subjects': subjects,
        'exams': exams,
        'selected_subject': selected_subject,
    })




def students_by_exam(request):
    subject_name = request.GET.get('subject')  
    exam_date = request.GET.get('date')       

    exams = Exam.objects.all()

    if subject_name:
        exams = exams.filter(subject__name__icontains=subject_name)  
    if exam_date:
        exams = exams.filter(date=exam_date)

    return render(request, 'project/student_list.jinja', {'exams': exams})


def first_five(request):
    first=Exam.objects.all()[:5]
    return render(request,"project/exam.jinja",{
        'exams': first,
    })