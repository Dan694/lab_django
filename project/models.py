from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)  
    semester = models.PositiveSmallIntegerField()  
    credits = models.PositiveSmallIntegerField()  

    def __str__(self):
        return f"Semester: {self.name} {self.semester} {self.credits} "


class Student(models.Model):
    first_name = models.CharField(max_length=50)  
    last_name = models.CharField(max_length=50)  
    birth_date = models.DateField()  
    gender = models.CharField(max_length=1)  

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} {self.birth_date} {self.gender}"


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    date = models.DateField()  
    mark = models.IntegerField()  

    def __str__(self):
        return f"Exam: {self.subject} {self.student} {self.date} {self.mark} "