from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import signals

# Create your models here.

class UserType(models.Model):
	'''
	UserType: 	
	'''
	name = models.CharField("Type of User", max_length=50)

	def __str__(self):
		return self.name

class User(AbstractUser):
	'''
	Used for storing user details
	'''
	phone = models.CharField("Phone", max_length=15, null=True, blank=True)
	subjects = models.ManyToManyField("subject", blank=True)
	email = models.EmailField("Email", max_length=250, null=True, blank=True)
	sem = models.CharField("Semester", null=True, blank=True, max_length=50)
	sec = models.CharField("Section", max_length=10, null=True, blank=True)
	user_type = models.ManyToManyField('UserType')


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


class Attendance(models.Model):
	'''
	Attendance: Stores the list of students for whom attendance has to be taken
	'''
	date_time = models.DateTimeField(auto_now=True, auto_now_add=False)
	teaches = models.ForeignKey('teaches', null=True)

	def __str__(self):
		return f'{self.teaches.teacher.first_name} -> {self.date_time}'


class Absentees(models.Model):
	'''
	Absentees: Stores the list of students who are absent
	'''
	user = models.ForeignKey('user')
	attendance = models.ForeignKey('attendance')

	def __str__(self):
		return self.user.first_name

	def create_status(self, user, status):
		detail = f'{self.name} is marked {status}'
		ChangeStatus.objects.create(
				user=user,
				attendance=attendance,
				detail=detail,
			)


class ChangeStatus(models.Model):
	'''
	Stores the details of when the attendance is changed, by whom and to what
	'''
	user = models.ForeignKey('user')
	datetime = models.DateTimeField(auto_now_add=True)
	attendance = models.ForeignKey('attendance')
	detail = models.TextField()

	def __str__(self):
		return f'{self.user} changed {self.detail} at {self.datetime}'

