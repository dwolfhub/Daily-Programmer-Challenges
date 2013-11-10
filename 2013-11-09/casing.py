def get_formatting_id():
	'''
	Prompt the user to give us the formatting id they require.

	Returns: string
	'''

	return input("Enter formatting ID\n0=CamelCase 1=snake_case 2=CAPITALIZED_SNAKE_CASE\nFormatting ID:")

def get_input_val():
	'''
	Prompt the user to give us the string they wish to format

	Returns: string
	'''

	return input("Enter Input To Case\nInput:")

def camel_case(input_val):
	'''
	Takes the input and returns a camel cased format

	Keyword arguments:
	input_val -- the input string

	Returns: string
	'''

	input_arr = input_val.split(' ') # split input by spaces
	for i, value in enumerate(input_arr): # loop through words and title case them
		if i > 0:
			input_arr[i] = value.title()
	return ''.join(input_arr) # join words and return as string

def snake_case(input_val, capitalize = False):
	'''
	Takes the input and returns a snake cased format either capitalized or lower cased

	Keyword arguments:
	input_val -- the input string
	capitalize -- the bool whether the input should be capitalized, default False

	Returns: string
	'''

	if capitalize: # capitalize or lower case the string
		input_val = input_val.upper()
	else:
		input_val = input_val.lower()
	input_arr = input_val.split(' ') # split string by spaces
	return '_'.join(input_arr) # join string with _

# empty input variables
format_id = None
input_val = None

# ask for a format id until a proper one is given
while format_id != '0' and format_id != '1' and format_id != '2':
	format_id = get_formatting_id()

# ask for an input string until a proper one is given
while not input_val:
	input_val = get_input_val()

# return the string with proper formatting, dependent on format id given
if format_id == '0': # camel case
	print(camel_case(input_val))
elif format_id == '1': # snake case, lower cased
	print(snake_case(input_val))
elif format_id == '2': # snake case, upper cased
	print(snake_case(input_val, True))