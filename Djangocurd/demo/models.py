from django.db import models

# Create your models here.
# 一对一关系
class Person(models.Model):
    name=models.CharField(max_length=20)
    # age=models.IntegerField(max_length=20)
    class Meta:
        db_table="person"
class Persondetail(models.Model):
    home=models.CharField(max_length=20)
    p=models.OneToOneField(to="Person",on_delete=True)
    class Meta:
        db_table="persondetail"

#一对多关系
class Class(models.Model):
    cname=models.CharField(max_length=20)
    class Meta:
        db_table="class"

class Student(models.Model):
    sname=models.CharField(max_length=20)
    c=models.ForeignKey(to="Class",on_delete=True)
    class Meta:
        db_table="student"

#多对多关系
class Auth(models.Model):
    aname=models.CharField(max_length=20)
    class Meta:
        db_table="auths"
class User(models.Model):
    uname=models.CharField(max_length=20)
    a=models.ManyToManyField(to="Auth")
    class Meta:
        db_table="users"
