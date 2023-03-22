from django.db import models


# Create your models here.

class SchoolSubj(models.Model):
    name = models.CharField(max_length=200)


class Students(models.Model):
    fullname = models.CharField(max_length=200)
    old = models.IntegerField()
    schoolSubj = models.ForeignKey(SchoolSubj, on_delete=models.CASCADE)
    estimation = models.IntegerField()


class SchoolClass(models.Model):
    classname = models.CharField(max_length=200)
    studyYear = models.IntegerField()
    students = models.ForeignKey(Students, on_delete=models.CASCADE)