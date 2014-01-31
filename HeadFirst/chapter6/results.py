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
		return(data.strip().split(','))
	except IOError as err:
		print('File error: ' + str(err))
		return(None)

		
sarah = get_coach_data('sarah2.txt')
sarah_dict = {}
sarah_dict['Name'] = sarah.pop(0)
sarah_dict['Birthday'] = sarah.pop(0)
sarah_dict['Results'] = sarah
print(sarah_dict['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah_dict['Results']]))[0:3]))

