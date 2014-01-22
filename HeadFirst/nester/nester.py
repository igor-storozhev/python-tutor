"""This is the "nester.py" module, and it provides one function called
print_lol() wich prints list that may or may not include nested lists.
A second argument called "level" is used to insert tab-stops when a nested
list encountered. A third argument "output" defines where output will be streamed."""
import sys
def print_lol(the_list, indent=False,level=0,output=sys.stdout):
	"""This function takes a positional arguments called "the list", which is an
	Python list (of, possibly, nested lists). Each data item in the provided list
	is (recursively) printed to screen on its own line"""
	for each_item in the_list :
		if isinstance(each_item,list) :
			print_lol(each_item, indent, level+1,output)
		else:
			if indent :
				for num in range(level):
					print("\t",end='',file=output)
			print(each_item,file=output)
