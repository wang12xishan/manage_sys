from django.db import models

# Create your models here.



class Classes(models.Model):
    """班级"""
    name = models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers")

class Teachers(models.Model):

    """老师"""
    name = models.CharField(max_length=32)

# class CtoT(models.Model):

#   班级老师 多对多表
#     cid = models.ForeignKey(Classes)
#     tid = models.ForeignKey(Teachers)

class Students(models.Model):
    """学生表"""

    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # gender = models.NullBooleanField()  可以为空的boolean值
    gender  = models.BooleanField()
    cs = models.ForeignKey("Classes")


