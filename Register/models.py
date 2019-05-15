from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse


# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

FORM=(
    ('Form1', 'form1'),
    ('Form2', 'form2'),
    ('Form3', 'form3'),
    ('Form4', 'form4'),
    ('Unknown', 'unknown'),
)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=30)
    form = models.CharField(choices=FORM,max_length=10,default='Unknown')

    def __str__(self):
        return self.user


"""
class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    maths = models.IntegerField()
    english = models.IntegerField()
    kiswahili = models.IntegerField()
    chemistry = models.IntegerField()
    biology = models.IntegerField()
    geography = models.IntegerField()
    total_mark = models.IntegerField(total =int(input("maths" + "english" + "kiswahili" + "chemistry" + "biology" + "geography"))

    def __str__(self):
        return self.student

    def get_absolute_url(self):
        return reverse('Register:index')


class Teacher(models.Model):
    Subject= models.ForeignKey(Subject, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    maths = models.IntegerField()
    english = models.IntegerField()
    kiswahili = models.IntegerField()
    chemistry = models.IntegerField()
    biology = models.IntegerField()
    geography = models.IntegerField()
    total_mark = models.IntegerField( "maths" + "english" + "kiswahili" + "chemistry" + "biology" + "geography")

    def __str__(self):
        return self.Mark

    def get_absolute_url(self):
        return reverse('Register:index')
        """




