def sanitize(time_string):
	if '-' in time_string: splitter = '-'
	elif ':' in time_string: splitter = ':'
	else: return(time_string)
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

def get_coach_data(file_name):
	try:
		with open(file_name) as file_data:
			data =  file_data.readline()
		templ = data.strip().split(',')
		return({'Name': templ.pop(0),
			'DOB': templ.pop(0),
			'Time': str(sorted(set([sanitize(t) for t in templ]))[0:3])})
	except IOError as err:
		print('File error: ' + str(err))
		return(None)

james = get_coach_data('james2.txt')		
julie = get_coach_data('julie2.txt')		
mikey = get_coach_data('mikey2.txt')		
sarah = get_coach_data('sarah2.txt')

print(james['Name'] + "'s fastest times are: " + james['Time'])
print(julie['Name'] + "'s fastest times are: " + julie['Time'])
print(mikey['Name'] + "'s fastest times are: " + mikey['Time'])
print(sarah['Name'] + "'s fastest times are: " + sarah['Time'])

