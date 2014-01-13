"""This is the "neter.py" module, and it provides one function called
        print_lol() wich prints list that may or may not include nested lists"""
def print_lol(the_list, tab = 0):
        """This function takes a positional arguments called "the list", which is an
                Python list (of, possibly, nested lists). Each data item in the provided list
                is (recursively) printed to screen on its own line"""
        for each_item in the_list :
                if isinstance(each_item,list) :
                        print_lol(each_item)
                else:
                	if tab > 0 :
                		for num in range(tab):
                			print("\t", end='')
                	print(each_item)
