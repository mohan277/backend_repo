from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    started_at = models.DateField()
    hq_location = models.TextField()
    share_vaule = models.IntegerField()

# class Mobile(models.Model):
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     ram = models.IntegerField()
#     price_in_inr = models.IntegerField()

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     no_of_credits = models.IntegerField()
#     students = models.ManyToManyField(Student, through='CourseStudent')

# class CourseStudent(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     grade = models.CharField(max_length=2)