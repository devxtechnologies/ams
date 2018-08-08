from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from main.models import Department, Subject, UserType
import sys, csv

User = get_user_model()

file = open("data.csv", 'r')

reader = csv.reader(file)

firstrow = True

# for i in reader:
# 	print(i[6])

counter = 0
count = 0
try:
	for row in reader:
		# print(row[6])
		if count == 0:
			firstrow = False
			count += 1
		else:
			print(type(row[17]))
			if row[17] != '':
				print("hello")
				dept = Department.objects.get(id = row[17])
			else:
				print('hello_brother')
				dept = None

			if dept != None:
				counter += 1
				user = User(password = make_password(row[1]), is_superuser = row[3], username = row[6], first_name = row[7], is_staff = row[9], is_active = row[10], phone = row[12], email = row[14], sem = row[15], sec = row[16], department = dept,  father = row[19], mother = row[20], phone_parent = row[21])
				print(user)
			else:
				count += 1
				user = User(password = make_password(row[1]), is_superuser = row[3], username = row[6], first_name = row[7], is_staff = row[9], is_active = row[10], phone = row[12], email = row[14], sem = row[15], sec = row[16], father = row[19], mother = row[20], phone_parent = row[21])
				print(user)

			# if row[18] != '':
			# 	for i in row[18].split(','):
			# 		usertype = UserType(id = i)
			# 		if usertype:
			# 			user.usertype.add(usertype)
			user.save()
			if row[13] != '':
				sub_list = row[13].split(',')
				user.subjects.add(*sub_list)
			# counter += 1
			# print(row[6])
except Exception as e:
	print(e)

finally:
	print(counter, count)
