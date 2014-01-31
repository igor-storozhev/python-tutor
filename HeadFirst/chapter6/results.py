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
			data = data.strip().split(',')
		data_dict = {}
		data_dict['Name'] = data.pop(0)
		data_dict['Birthday'] = data.pop(0)
		data_dict['Results'] = str(sorted(set([sanitize(t) for t in data]))[0:3])
		return(data_dict)
	except IOError as err:
		print('File error: ' + str(err))
		return(None)

		
sarah_dict = get_coach_data('sarah2.txt')
print(sarah_dict['Name'] + "'s fastest times are: " + sarah_dict['Results'])

