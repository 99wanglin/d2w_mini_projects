from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
	array = []
	random.seed(seed)
	for i in range(number):
		array.append(i)
	random.shuffle(array)
	return array

def create_array_str():
	array_str = ''
	for i, v in enumerate(array):
		array_str += v
		if i < len(array)-1:
			array_str += ', '
		else:
			array_str += '.'
	return array_str

def generate():
	global array

	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	

	array = gen_random_int(number, seed)
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	

	array_str = create_array_str()
	
	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and 
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	
	n = len(array)
	for i in range(n):
		index = i
		temporary = array[i]
		while index > 0 and temporary < array[index-1]:
			if array[index] < array[index-1] :
				array[index], array[index - 1] = array[index-1], array[index]
				index -=1
		temporary = array[index]

	array_str = create_array_str()
	

	document.getElementById("sorted").innerHTML = array_str
	return array_str

def sortnumber2():
	global array
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	pass

	

	new_value = value.replace(" ", '')
	array = list(new_value.split(','))
	for i, v in enumerate(array):
		array[i] = int(v)
	
	array_str = sortnumber1()

	document.getElementById("sorted").innerHTML = array_str


