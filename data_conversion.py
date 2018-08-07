import sys, csv

filename = sys.argv[1]
file_to_write = sys.argv[2]

file = open(filename, 'r')
file_write = open(file_to_write, 'w')

reader = csv.reader(file)
writer = csv.writer(file_write)
writer.writerow(['id','username','password', 'email', 'first_name', 'phone', 'sem', 'father', 'mother', 'phone_parent'])

firstrow = True

counter = 10

for row in reader:
	if firstrow:
		firstrow = False
		continue
	writer.writerow([
		counter,
		row[3].split('@')[0], 
		row[3].split('@')[0],
		row[3],
		row[1],
		row[2].split('/')[0],
		'1',
		row[4],
		row[5],
		row[6].split(',')[0]
		])
	counter += 1
