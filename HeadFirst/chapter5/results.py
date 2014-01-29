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

print(sorted(set([sanitize(time) for time in james]))[0:3])
print(sorted(set([sanitize(time) for time in julie]))[0:3])
print(sorted(set([sanitize(time) for time in mikey]))[0:3])
print(sorted(set([sanitize(time) for time in sarah]))[0:3])
