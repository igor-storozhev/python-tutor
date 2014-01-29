def get_file_data(file_name):
	try:
		with open(file_name) as file_data:
			data =  file_data.readline()
		return(data.strip().split(','))
	except IOError as err:
		print('File error: ' + str(err))
		return(None)

print(get_file_data('james.txt'))
		
