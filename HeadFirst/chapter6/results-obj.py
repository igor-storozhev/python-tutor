def sanitize(time_string):
	if '-' in time_string: splitter = '-'
	elif ':' in time_string: splitter = ':'
	else: return(time_string)
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

class Athlete:
	def __init__(self, a_name, a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times
	def top3(self):
		return (sorted(set([sanitize(t) for t in self.times]))[0:3])
	def add_time(self, time_value=None):
		self.times.append(time_value)
	def add_times(self, list_of_times=[]):
		self.times.extend(list_of_times)

def get_coach_data(file_name):
	try:
		with open(file_name) as file_data:
			data =  file_data.readline()
		templ = data.strip().split(',')
		return Athlete(templ.pop(0), templ.pop(0), templ)
	except IOError as err:
		print('File error: ' + str(err))
		return(None)

james = get_coach_data('james2.txt')		
julie = get_coach_data('julie2.txt')		
mikey = get_coach_data('mikey2.txt')		
sarah = get_coach_data('sarah2.txt')

james.add_time('1.11')
james.add_times(['1.09','1.10'])

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))


