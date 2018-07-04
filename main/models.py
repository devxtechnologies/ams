from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	'''
	Used for teachers
	'''
	phone = models.CharField("Phone", max_length=15, null=True, blank=True)
	subjects = models.ManyToManyField("subject", blank=True)


class Student(models.Model):
	'''
	TODO://
	'''
	name = models.CharField("Name", max_length=250, null=True, blank=True)
	phone = models.CharField("Phone", max_length=20, null=True, blank=True)
	email = models.EmailField("Email", max_length=250, null=True, blank=True)

	sem = models.IntegerField("Semester", null=True, blank=True)
	sec = models.CharField("Section", max_length=10, null=True, blank=True)

	subjects = models.ManyToManyField("subject", blank=True)
# 	department = models.ForeignKey("Department", on_delete=models.CASCADE, null=True)
# 	date_of_joining = models.DateField("Date of Joining", null=True, blank=True)
# 	ug = models.BooleanField(default=False)
# 	batch = models.CharField("Lab Batch", max_length=50, null=True, blank=True)
# 	sub_batch = models.CharField("Lab Sub Batch", max_length=50, null=True, blank=True)
	
	def __str__(self):
		return self.first_name


class Subject(models.Model):
	'''
	Subject: Holds details about each subject
	'''
	name = models.CharField("Subject Name", max_length=50)
	code = models.CharField("Subject Code", max_length=50)

	theory = models.BooleanField(default=True)
	elective = models.BooleanField(default=False)

	def __str__(self):
		return str(self.name + '->' + self.code)


class Teaches(models.Model):
	'''
	Teaches: Holds details about the subject that the teacher teaches.
	It links the Subject and the Teacher with the sem, sec and department that they are teaching.
	We are storing sem, sec, deaprtment of the student to get the name of the teacher by matching the
	details with the user table.
	'''
	teacher = models.ForeignKey('user')
	subject = models.ForeignKey('subject')

	sem = models.CharField("Student's Semester", max_length=50)
	sec = models.CharField("Student's Section", max_length=50)
# 	department = models.ForeignKey('department')

# 	batch = models.CharField("Student's Batch", max_length=50, null=True, blank=True)
# 	sub_batch = models.CharField("Student's sub batch", max_length=50, null=True, blank=True)
# 	ug = models.BooleanField(default=False)

	count = models.IntegerField("Student Count", default=0, null=True, blank=True)

	def __str__(self):
		return self.teacher.first_name + ' -> '  + self.subject.name + '->' + self.sem + " " + self.sec