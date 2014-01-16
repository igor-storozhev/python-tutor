try:
	data =  open('sketch.txt')

	for each_line in data:
		if not each_line.find(':') == -1 :
			try:
				(role, line_spoken) = each_line.split(':',1)
				print(role, end='')
				print(' said: ', end = '')
				print(line_spoken, end='')
			except:
				pass
	data.close()
except:
	print('The data file is missing')
