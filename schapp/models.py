from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=20)
    staff_img = models.FileField()
    staff_desc = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    date = models.DateField()
    image = models.FileField()

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=30)
    hod = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=30)
    patron = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Mission(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Vision(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Anthem(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Motto(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Sport(models.Model):
    name = models.CharField(max_length=30)
    coach = models.CharField(max_length=20)
    desc = models.TextField(default="anything")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    cover_image = models.FileField()
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    Comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Comment

    def get_absolute_url(self):
        return reverse('schapp:index')



class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('schapp:send-message')

