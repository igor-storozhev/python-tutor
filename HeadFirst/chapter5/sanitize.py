def sanitize(time_string):
	print('start')
	print(time_string)
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		print('before return ')
		return(time_string)
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

str1 = '2-22'
str2 = '2.34'
str3 = '2:01'

print(sanitize(str1))
print(sanitize(str2))
print(sanitize(str3))
