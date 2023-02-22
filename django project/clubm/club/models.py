from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    dept = models.CharField(max_length=5)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    year = models.CharField(max_length=10)
    roll = models.BigIntegerField()
    postv=models.IntegerField(default=0)
    clubsinterested=models.CharField(max_length=100)


class club(models.Model):
    club_id = models.IntegerField()
    club_name = models.CharField(max_length=40)
    club_description = models.CharField(max_length=4000)
    club_head_id = models.IntegerField()
    club_img = models.CharField(max_length=1000)



class club_details(models.Model):
    club_det_id = models.IntegerField()
    student_name = models.CharField(max_length=30)
    role = models.CharField(max_length=20)


class request(models.Model):
    dept = models.IntegerField()
    task_name = models.CharField(max_length=25)
    assignee = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    current_date = models.DateField()
    due_date = models.DateField()


class comments(models.Model):
    comments_id = models.IntegerField()
    date = models.DateField(default='2019-01-01')
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=10000)
    student_id = models.IntegerField()

class threads(models.Model):
    comments_id = models.IntegerField(default=0)
    thread= models.CharField(max_length=10000,default='')
    date = models.DateField(default='2019-01-01')


class event(models.Model):
    student_id = models.BigIntegerField()
    club_id = models.IntegerField()
    description_event = models.CharField(max_length=40000)
    club_name = models.CharField(max_length=15)
    event_name = models.CharField(max_length=15)
    volunteers = models.IntegerField()
    date = models.DateField(default='2019-01-01')
    status = models.IntegerField(default=0)