def sanitize(time_string):
	if '-' in time_string: splitter = '-'
	elif ':' in time_string: splitter = ':'
	else: return(time_string)
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

try:
	with open('james.txt') as james_file: line = james_file.readline()
	james = line.strip().split(',')
	with open('julie.txt') as julie_file: line = julie_file.readline()
	julie = line.strip().split(',')
	with open('mikey.txt') as mikey_file: line = mikey_file.readline()
	mikey = line.strip().split(',')
	with open('sarah.txt') as sarah_file: line = sarah_file.readline()
	sarah = line.strip().split(',')
except IOError as err:
	print('File error: '+str(err))

james = sorted([sanitize(time) for time in james])
unique_james = []
for time in james:
	if time not in unique_james:
		unique_james.append(time);
print(unique_james[0:3])
julie = sorted([sanitize(time) for time in julie])
unique_julie = []
for time in julie:
	if time not in unique_julie:
		unique_julie.append(time);
print(unique_julie[0:3])
mikey = sorted([sanitize(time) for time in mikey])
unique_mikey = []
for time in mikey:
	if time not in unique_mikey:
		unique_mikey.append(time);
print(unique_mikey[0:3])
sarah = sorted([sanitize(time) for time in sarah])
unique_sarah = []
for time in sarah:
	if time not in unique_sarah:
		unique_sarah.append(time);
print(unique_sarah[0:3])
