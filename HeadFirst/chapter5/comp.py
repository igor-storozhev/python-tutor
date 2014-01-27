def sanitize(time_string):
	if '-' in time_string: splitter = '-'
	elif ':' in time_string: splitter = ':'
	else: return(time_string)
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

dirty = ['2-22','2:22','2.22']

clean = [float(sanitize(d)) for d in dirty]

print(clean)
